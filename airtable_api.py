import requests
from keys import airtable_key

AIRTABLE_BASE_ID = 'appAyRuk6f9ewiH78'
AIRTABLE_API_KEY = airtable_key

AIRTABLE_TAG_GROUPS_TABLE_NAME = 'TagGroups'
AIRTABLE_TAGS_TABLE_NAME = 'Tags'
AIRTABLE_PEOPLE_TABLE_NAME = 'People'
AIRTABLE_PROJECTS_TABLE_NAME = 'Projects'

endpoint = 'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_PROJECTS_TABLE_NAME}'

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
                    "PrimaryContactEmail": primary_contact_email,
                    "PrimaryContactPhone": primary_contact_phone,
                    "PrimaryContactSocialMediaProfileUrl": primary_contact_social_media,
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
                    "PrimaryContactEmail": primary_contact_email,
                    "PrimaryContactPhone": primary_contact_phone,
                    "PrimaryContactSocialMediaProfileUrl": primary_contact_social_media,
                    "Image": image
                }
            }
        ]
    }

    r = requests.post(endpoint, json = data, headers = headers)
    print(r.status_code)

add_project(None, name = "Test")