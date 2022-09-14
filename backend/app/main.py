from __future__ import annotations

import logging
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from .config import settings
from .db import DatabaseUnavailableError, close_driver, init_driver, run_query
from .routers import courses, paths, roles, skills

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Career Compass API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(DatabaseUnavailableError)
async def db_unavailable_handler(request: Request, exc: DatabaseUnavailableError):
    logging.getLogger("career_compass").error("Database error: %s", exc)
    return JSONResponse(
        status_code=503,
        content={
            "detail": "The graph database is unreachable right now. Please try again shortly."
        },
    )


@app.on_event("startup")
def _startup() -> None:
    init_driver()


@app.on_event("shutdown")
def _shutdown() -> None:
    close_driver()


