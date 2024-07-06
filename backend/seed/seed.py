#!/usr/bin/env python3
"""Loads the Career Compass seed data into CognoDB.

Usage (run from the backend/ directory):
    python seed/seed.py            # merge data in (safe to re-run)
    python seed/seed.py --reset    # delete all nodes/relationships first

Reads connection details from the environment (COGNODB_URI,
COGNODB_USER, COGNODB_PASSWORD, COGNODB_DATABASE), the same variables
the application itself uses. Run this from the `backend/` directory
with a `.env` file present, or with the variables already exported.
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from neo4j import GraphDatabase

sys.path.insert(0, str(Path(__file__).resolve().parent))
from seed_data import COURSE_PREREQUISITES, COURSES, ROLES, SKILL_RELATIONSHIPS, SKILLS  # noqa: E402

URI = os.environ.get("COGNODB_URI", "")
USER = os.environ.get("COGNODB_USER", "cognodb")
PASSWORD = os.environ.get("COGNODB_PASSWORD", "")
DATABASE = os.environ.get("COGNODB_DATABASE", "neo4j")


def reset(session) -> None:
    print("Deleting all existing nodes and relationships...")
    session.run("MATCH (n) DETACH DELETE n")


def create_constraints(session) -> None:
    for label, prop in [("Skill", "skill_id"), ("Course", "course_id"), ("Role", "role_id")]:
        session.run(
            f"CREATE CONSTRAINT IF NOT EXISTS FOR (n:{label}) REQUIRE n.{prop} IS UNIQUE"
        )


def load_courses(session) -> None:
    rows = [
        {
            "course_id": cid, "title": title, "provider": provider, "level": level,
            "duration_hours": duration, "url": url,
        }
        for cid, title, provider, level, duration, url, _teaches, _requires in COURSES
    ]
    session.run(
        """
        UNWIND $rows AS row
        MERGE (c:Course {course_id: row.course_id})
        SET c.title = row.title, c.provider = row.provider, c.level = row.level,
            c.duration_hours = row.duration_hours, c.url = row.url
        """,
        rows=rows,
    )
    print(f"Loaded {len(rows)} Course nodes.")

    teaches_rows = [
        {"course_id": cid, "skill_id": skill_id}
        for cid, *_rest, teaches, _requires in COURSES
        for skill_id in teaches
    ]
    session.run(
        """
        UNWIND $rows AS row
        MATCH (c:Course {course_id: row.course_id})
        MATCH (s:Skill {skill_id: row.skill_id})
        MERGE (c)-[:TEACHES]->(s)
        """,
        rows=teaches_rows,
    )
    print(f"Loaded {len(teaches_rows)} TEACHES relationships.")

    requires_rows = [
        {"course_id": cid, "skill_id": skill_id}
        for cid, *_rest, _teaches, requires in COURSES
        for skill_id in requires
    ]
    session.run(
        """
        UNWIND $rows AS row
        MATCH (c:Course {course_id: row.course_id})
        MATCH (s:Skill {skill_id: row.skill_id})
        MERGE (c)-[:REQUIRES]->(s)
        """,
        rows=requires_rows,
    )
    print(f"Loaded {len(requires_rows)} REQUIRES relationships.")

    prereq_rows = [{"before": before, "after": after} for before, after in COURSE_PREREQUISITES]
    session.run(
        """
        UNWIND $rows AS row
        MATCH (before:Course {course_id: row.before})
        MATCH (after:Course {course_id: row.after})
        MERGE (before)-[:PREREQUISITE_OF]->(after)
        """,
        rows=prereq_rows,
    )
    print(f"Loaded {len(prereq_rows)} PREREQUISITE_OF relationships.")


