import os
import requests
from typing import List
from dotenv import load_dotenv

from tag_api.models import Tag
load_dotenv(".env")

AIRTABLE_BASE_ID = os.environ.get("AIRTABLE_BASE_ID")
AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
AIRTABLE_TABLE_NAME = os.environ.get("AIRTABLE_TAG_GROUPS_TABLE_NAME")

endpoint = 'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'

def get_tag_group(tag_group_id: str):
    headers = {
        "Authorization": "Bearer {AIRTABLE_API_KEY}"
    }

    r = requests.get(endpoint + tag_group_id)
    return r.json()

def get_tag_groups():
    headers = {
        "Authorization": "Bearer {AIRTABLE_API_KEY}"
    }

    r = requests.get(endpoint) # Don't have time to figure out the parameters; I'll filter things on the python side of things for now
    return r.json

def add_tag_group(name: str, description: str = None, tags: List[Tag] = []):
    headers = {
        "Authorization": "Bearer {AIRTABLE_API_KEY}",
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
    print(r.status_code())

def remove_tag_group(tag_group_id: str):
    headers = {
        "Authorization": "Bearer {AIRTABLE_API_KEY}"
    }

    r = requests.delete(endpoint + tag_group_id)
    return r.status_code()

def update_tag_group(tag_group_id: str):
    headers = {
        "Authorization": "Bearer {AIRTABLE_API_KEY}"
    }