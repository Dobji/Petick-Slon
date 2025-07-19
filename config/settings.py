"""
Application settings and configuration.
"""
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Debug mode (set to False in production)
DEBUG = os.environ.get("DEBUG", "True").lower() == "true"

# Secret key (change in production)
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")

# Database settings
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./app.db")

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Templates
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates") 