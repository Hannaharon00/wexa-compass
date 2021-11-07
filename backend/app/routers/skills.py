from __future__ import annotations

from fastapi import APIRouter, HTTPException, Query

from .. import queries
from ..db import run_query

router = APIRouter(prefix="/api/skills", tags=["skills"])


@router.get("")
def list_skills():
    return run_query(queries.LIST_SKILLS)


