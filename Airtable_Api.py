import os
import requests
from typing import Dict, List
from dotenv import load_dotenv
from models import Tag
load_dotenv(".env")

AIRTABLE_BASE_ID = os.environ.get("AIRTABLE_BASE_ID")
AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
AIRTABLE_TABLE_NAME = os.environ.get("AIRTABLE_TABLE_NAME")

endpoint = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'
auth = f"Bearer {AIRTABLE_API_KEY}"

def get_project(project_id: str):
    headers = {
        "Authorization": auth
    }

    r = requests.get(f"{endpoint}/{project_id}", headers = headers)
    return r.json()

def get_projects():
    headers = {
        "Authorization": auth
    }

    print(endpoint)

    r = requests.get(endpoint, headers = headers) # Don't have time to figure out the parameters; I'll filter things on the python side of things for now
    return r.json()

def add_project(name: str, description: str = None, tags: List[Tag] = [], primary_contact: str = None, image: str = None, region: str = None):
    headers = {
        "Authorization": auth,
        "Content-Type": "application/json"
    }

    data = {
         "records": [
            {
                "fields": {
                    "Description": description,
                    "Name": name,
                    "Tags": tags,
                    "PrimaryContact": primary_contact,
                    "Image": image,
                    "Region": region
                }
            }
        ]
    }

    r = requests.post(endpoint, json = data, headers = headers)
    print(r.status_code)

def remove_project(project_id: str):
    headers = {
        "Authorization": auth
    }

    r = requests.delete(f"{endpoint}/{project_id}", headers = headers)
    return r.status_code

def update_projects(changes: Dict[str, dict]):
    """Takes a dictionary with keys of project ids and values of dictionaries with fields as keys and their updated values as values.
    Updates the given fields."""

    headers = {
        "Authorization": auth,
        "Content-Type": "application/json"
    }

    records: List[dict] = []
    for project_id, change_dict in changes:
        fields = change_dict.keys()
        records.append(
            {
                "id": project_id,
                "fields": {field:change_dict[field] for field in fields}
            }
        )
    data = {
        "records": records
    }

    r = requests.patch(endpoint, json = data, headers = headers)
    print(r.status_code)

# add_project("Test", "this is a test")
print(get_projects())