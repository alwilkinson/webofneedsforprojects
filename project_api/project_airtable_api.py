from email import headerregistry
import os
import requests
from dotenv import load_dotenv
load_dotenv(".env")

AIRTABLE_BASE_ID = os.environ.get("AIRTABLE_BASE_ID")
AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
AIRTABLE_TABLE_NAME = os.environ.get("AIRTABLE_TABLE_NAME")

endpoint = 'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'

# headers = {
#     "Authorization: Bearer {AIRTABLE_API_KEY}",
#     "Content-Type: application/json"
# }
# 
# data = {
#      "records": [
#         {
#             "fields": {}
#         },
#         {
#             "fields": {}
#         }
#     ]
# }
# 
# r = requests.post(endpoint, json = data, headers = headers)
# print(r.json())



def get_project(project_id):
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

def add_project(project_id, description = None, name = None, tags = None, tag_ids = None, primary_contact = None, primary_contact_phone = None, primary_contact_email = None, primary_contact_social_media = None, image = None):
    headers = {
        "Authorization": "Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
         "records": [
            {
                "fields": {
                    "ProjectID": project_id,
                    "Description": description,
                    "Name": name,
                    "Tags": tags,
                    "TagId (from Tags)": tag_ids,
                    "PrimaryContact": primary_contact,
                    "Image": image
                }
            },
            {
                "fields": {
                    "ProjectID": project_id,
                    "Description": description,
                    "Name": name,
                    "Tags": tags,
                    "TagId (from Tags)": tag_ids,
                    "PrimaryContact": primary_contact,
                    "Image": image
                }
            }
        ]
    }

    r = requests.post(endpoint, json = data, headers = headers)
    print(r.status_code())

add_project(None, name = "Test")