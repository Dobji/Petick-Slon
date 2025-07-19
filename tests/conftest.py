"""
Pytest configuration file.
"""
import sys
import os
import pytest

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Define fixtures here
@pytest.fixture
def app_config():
    """Return test configuration."""
    return {
        "TESTING": True,
        "DEBUG": True,
    } 