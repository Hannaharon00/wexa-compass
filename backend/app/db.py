"""CognoDB (openCypher over Bolt) connection handling.

CognoDB speaks the same Bolt protocol as Neo4j, so the official `neo4j`
Python driver is used as-is -- no custom SDK. The driver keeps its own
internal connection pool, so a single process-wide instance is created
once and reused for every request.
"""
from __future__ import annotations

import logging
from contextlib import contextmanager
from typing import Any, Iterator

from neo4j import GraphDatabase, Driver
from neo4j.exceptions import Neo4jError, ServiceUnavailable, AuthError

from .config import settings

logger = logging.getLogger("career_compass.db")

_driver: Driver | None = None


class DatabaseUnavailableError(RuntimeError):
    """Raised whenever CognoDB cannot be reached or a query fails.

    Kept distinct from generic exceptions so the API layer can turn it
    into a clean 503 instead of leaking a driver stack trace.
    """


