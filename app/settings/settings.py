import os


# General project settings
PROJECT_NAME: str = os.environ.get("PROJECT_NAME", "python-challenge-main")
PROJECT_VERSION: str = os.environ.get("PROJECT_VERSION", "0.0.1")
DEBUG: bool = os.environ.get("DEBUG", False)


__all__ = [
    "PROJECT_NAME",
    "PROJECT_VERSION",
    "DEBUG",
]
