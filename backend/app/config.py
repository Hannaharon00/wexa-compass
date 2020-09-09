"""Environment-driven configuration. Nothing here is a secret — the
values themselves are read from the environment, never hard-coded."""
import os
from dataclasses import dataclass
from pathlib import Path

# Load a local .env file in development. In production (Render, etc.)
# real environment variables are set in the platform dashboard instead.
try:
    from dotenv import load_dotenv

    load_dotenv(Path(__file__).resolve().parents[2] / ".env")
except ImportError:
    pass


