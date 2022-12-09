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

