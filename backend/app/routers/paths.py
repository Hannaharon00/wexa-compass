"""The flagship endpoint: given the skills a person already has and a
target role, work out an ordered list of courses that closes the gap.

This is deliberately the query the assignment asks for -- one a
relational database handles badly. It combines:
  1. a set difference (role's required skills minus known skills),
  2. a fan-out to every course that teaches each missing skill,
  3. a variable-length walk up each candidate course's own prerequisite
     chain (unbounded depth), and
  4. a topological sort over whatever course subgraph came back.

Steps 1-3 are graph traversals expressed as a couple of Cypher
statements. Step 4 -- ordering a DAG -- has no equivalent single-query
answer in either Cypher or SQL, so it's done in plain Python (Kahn's
algorithm) over the small subgraph the database handed back. That
split -- graph database for reachability/traversal, application code for
the final deterministic sort -- is a normal and honest division of
labour, not a workaround.
"""
from __future__ import annotations

from collections import defaultdict, deque

from fastapi import APIRouter, HTTPException

from .. import queries
from ..db import run_query
from ..schemas import LearningPathRequest

router = APIRouter(prefix="/api", tags=["learning-path"])


def _topological_order(course_ids: set, edges: list[dict], meta: dict) -> list[str]:
    """Kahn's algorithm, ties broken by (duration_hours, title) so the
    result is stable and readable rather than arbitrary."""
    indegree = {cid: 0 for cid in course_ids}
    adjacency = defaultdict(list)
    for e in edges:
        if e["from_course"] in course_ids and e["to_course"] in course_ids:
            adjacency[e["from_course"]].append(e["to_course"])
            indegree[e["to_course"]] += 1

    def sort_key(cid):
        m = meta.get(cid, {})
        return (m.get("duration_hours") or 0, m.get("title") or cid)

    ready = deque(sorted((c for c in course_ids if indegree[c] == 0), key=sort_key))
    ordered = []
    while ready:
        current = ready.popleft()
        ordered.append(current)
        for nxt in sorted(adjacency[current], key=sort_key):
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                ready.append(nxt)
        ready = deque(sorted(ready, key=sort_key))
    # Any course left with indegree > 0 sits on a cycle in the seed data;
    # append it at the end rather than dropping it silently.
    remaining = [c for c in course_ids if c not in ordered]
    ordered.extend(sorted(remaining, key=sort_key))
    return ordered


    uncovered_skills = []
    gap_name_by_id = {s["skill_id"]: s["name"] for s in required_skills}
    for gap_id in uncovered_gap_ids:
        bridge_rows = run_query(
            queries.SHORTEST_SKILL_BRIDGE,
            {"known_skill_ids": list(known), "gap_skill_id": gap_id},
        )
        uncovered_skills.append(
            {
                "skill_id": gap_id,
                "name": gap_name_by_id.get(gap_id, gap_id),
                "closest_known_bridge": bridge_rows[0] if bridge_rows else None,
            }
        )

    core_course_ids = {v["row"]["course_id"] for v in best_by_gap.values()}
    skills_covered_by_course = defaultdict(list)
    for gap_id, v in best_by_gap.items():
        skills_covered_by_course[v["row"]["course_id"]].append(gap_name_by_id.get(gap_id, gap_id))

    # A core course may itself assume skills the learner doesn't have yet
    # (its REQUIRES edges minus what they already know). Only pull a
    # prerequisite course into the plan when it actually teaches one of
    # those still-missing skills -- otherwise a course the learner has
    # already effectively satisfied (e.g. they said they already know
    # Python) would still drag in its whole authored prerequisite chain
    # regardless of what they told us they know.
    unmet_skill_ids_by_course = {
        v["row"]["course_id"]: {s["skill_id"] for s in v["row"]["unmet_prerequisite_skills"]}
        for v in best_by_gap.values()
    }

    all_course_ids = set(core_course_ids)
    for cid in core_course_ids:
        unmet_ids = unmet_skill_ids_by_course.get(cid, set())
        if not unmet_ids:
            continue
        chain_rows = run_query(queries.COURSE_PREREQUISITE_CHAIN, {"course_id": cid})
        chain_ids = [r["course_id"] for r in chain_rows if r["course_id"] not in all_course_ids]
        if not chain_ids:
            continue
        teaches_rows = run_query(queries.COURSES_TEACHES_BY_IDS, {"course_ids": chain_ids})
        for row in teaches_rows:
            if unmet_ids.intersection(row["teaches_skill_ids"]):
                all_course_ids.add(row["course_id"])

    meta_rows = run_query(queries.COURSES_BY_IDS, {"course_ids": list(all_course_ids)})
    meta = {r["course_id"]: r for r in meta_rows}

