from __future__ import annotations

from fastapi import APIRouter, HTTPException

from .. import queries
from ..db import run_query

router = APIRouter(prefix="/api/courses", tags=["courses"])


