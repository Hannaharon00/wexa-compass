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

from dotenv import load_dotenv
from neo4j import GraphDatabase

