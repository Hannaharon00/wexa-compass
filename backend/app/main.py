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


