import os
import requests
from typing import Dict, List
from dotenv import load_dotenv
from models import Tag
load_dotenv(".env")

AIRTABLE_BASE_ID = os.environ.get("AIRTABLE_BASE_ID")
AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
AIRTABLE_TABLE_NAME = os.environ.get("AIRTABLE_TAG_GROUPS_TABLE_NAME")

endpoint = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'
auth = f"Bearer {AIRTABLE_API_KEY}"

def get_tag_group(tag_group_id: str):
    headers = {
        "Authorization": auth
    }

    r = requests.get(endpoint + tag_group_id, headers = headers)
    return r.json()

def get_tag_groups():
    headers = {
        "Authorization": auth
    }

    r = requests.get(endpoint) # Don't have time to figure out the parameters; I'll filter things on the python side of things for now
    return r.json

def add_tag_group(name: str, description: str = None, tags: List[Tag] = []):
    headers = {
        "Authorization": auth,
        "Content-Type": "application/json"
    }

    data = {
         "records": [
            {
                "fields": {
                    "Name": name,
                    "Description": description,
                    "Tags": [tag.id for tag in tags]
                }
            }
        ]
    }

    r = requests.post(endpoint, json = data, headers = headers)
    print(r.status_code)

def remove_tag_group(tag_group_id: str):
    headers = {
        "Authorization": auth
    }

    r = requests.delete(endpoint + tag_group_id, headers = headers)
    return r.status_code

def update_tag_group(changes: Dict[str, dict]):
    """Takes a dictionary with keys of tag group ids and values of dictionaries with fields as keys and their updated values as values.
    Updates the given fields."""
    headers = {
        "Authorization": auth,
        "Content-Type": "application/json"
    }

    records: List[dict] = []
    for tag_group_id, change_dict in changes:
        fields = change_dict.keys()
        records.append(
            {
                "id": tag_group_id,
                "fields": {field:change_dict[field] for field in fields}
            }
        )
    data = {
        "records": records
    }

    r = requests.patch(endpoint, json = data, headers = headers)
    print(r.status_code)