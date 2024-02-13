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


def init_driver() -> None:
    """Create the driver at startup. Connectivity is *not* required to
    succeed here -- if CognoDB is briefly unreachable when the app boots,
    the app still starts and each request will retry the connection and
    fail gracefully instead of crashing the whole process.
    """
    global _driver
    if not settings.cognodb_uri or not settings.cognodb_password:
        logger.warning(
            "COGNODB_URI / COGNODB_PASSWORD are not set. "
            "The API will start but every query will fail until they are configured."
        )
        return
    _driver = GraphDatabase.driver(
        settings.cognodb_uri,
        auth=(settings.cognodb_user, settings.cognodb_password),
    )
    try:
        _driver.verify_connectivity()
        logger.info("Connected to CognoDB at %s", settings.cognodb_uri)
    except Exception as exc:  # noqa: BLE001 - log and continue, don't crash boot
        logger.warning("CognoDB not reachable at startup: %s", exc)


def close_driver() -> None:
    global _driver
    if _driver is not None:
        _driver.close()
        _driver = None


