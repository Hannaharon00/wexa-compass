from __future__ import annotations

from fastapi import APIRouter, HTTPException

from .. import queries
from ..db import run_query
from ..schemas import RecommendRolesRequest

router = APIRouter(prefix="/api/roles", tags=["roles"])


