from os import environ

from pathlib import Path

import dotenv


def config(var: str) -> str:
    dotenv.load_dotenv(f"{Path(__file__).parent}/../.env")
    return environ[var]
