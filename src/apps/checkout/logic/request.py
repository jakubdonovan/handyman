from typing import Optional
import requests
from requests.models import Response


def fetch_sections() -> Optional[list[str]]:

    json = {"query": "{ sectionMany {_id, title}  }"}
    resp: Response = requests.post(
        "https://handymanjacek.com/graphql", json=json
    )
    if resp.ok and (sections := resp.json()["data"]["sectionMany"]):
        return [section["title"] for section in sections]
