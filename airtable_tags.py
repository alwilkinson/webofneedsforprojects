import os
import requests
from typing import List
from dotenv import load_dotenv
from models import Tag
load_dotenv(".env")

AIRTABLE_BASE_ID = os.environ.get("AIRTABLE_BASE_ID")
AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
AIRTABLE_TABLE_NAME = os.environ.get("AIRTABLE_TAGS_TABLE_NAME")

endpoint = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'
auth = f"Bearer {AIRTABLE_API_KEY}"

def get_tag(tag_id: str):
    headers = {
        "Authorization": auth
    }

    r = requests.get(endpoint + tag_id, headers = headers)
    return r.json()

def get_tags():
    headers = {
        "Authorization": auth
    }

    r = requests.get(endpoint, headers = headers)
    return r.json

def add_tag(name: str, description: str = None):
    headers = {
        "Authorization": auth,
        "Content-Type": "application/json"
    }

    data = {
         "records": [
            {
                "fields": {
                    "Name": name,
                    "Description": description
                }
            }
        ]
    }

    r = requests.post(endpoint, json = data, headers = headers)
    print(r.status_code())

def remove_tag(tag_id: str):
    headers = {
        "Authorization": auth
    }

    r = requests.delete(f"{endpoint}/{tag_id}", headers = headers)
    return r.status_code()