import os
import requests
from typing import List
from dotenv import load_dotenv

from tag_api.models import Tag
load_dotenv(".env")

AIRTABLE_BASE_ID = os.environ.get("AIRTABLE_BASE_ID")
AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
AIRTABLE_TABLE_NAME = os.environ.get("AIRTABLE_TABLE_NAME")

endpoint = 'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'

def get_project(project_id: str):
    headers = {
        "Authorization": "Bearer {AIRTABLE_API_KEY}"
    }

    r = requests.get(endpoint + project_id)
    return r.json()

def get_projects():
    headers = {
        "Authorization": "Bearer {AIRTABLE_API_KEY}"
    }

    r = requests.get(endpoint) # Don't have time to figure out the parameters; I'll filter things on the python side of things for now
    return r.json

def add_project(name: str, description: str = None, tags: List[Tag] = [], primary_contact: str = None, image: str = None, region: str = None):
    headers = {
        "Authorization": "Bearer {AIRTABLE_API_KEY}",
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
                    "Image": image
                }
            }
        ]
    }

    r = requests.post(endpoint, json = data, headers = headers)
    print(r.status_code())

def remove_project(project_id: str):
    headers = {
        "Authorization": "Bearer {AIRTABLE_API_KEY}"
    }

    r = requests.delete(endpoint + project_id)
    return r.status_code()