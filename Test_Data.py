from Project_Class import Project as pr
from typing import List, Union
from datetime import datetime
import Airtable_Api as airtable
from models import Tag
import json
import re

def get_project_data() -> List[pr]:
    data = airtable.get_projects()["records"]
    projects: List[pr] = []
    for project in data:
        fields = project["fields"]
# date created requires some scraping, as the airtable keeps more precise time than we need.
        year, month, day = [int(string) for string in re.split(r'-', project["createdTime"][0:10])]
        date = datetime(year, month, day)
        print(project)
        projects.append(pr(project["id"], fields["Name"], fields.get("Tags", None), fields.get("Description", None), date, fields.get("Region", None), fields.get("Primary_Contact", None)))
    return projects
    

def create_project(name: str, tags: List[Tag] = [], description: Union[str, None] = None, region: Union[str, None] = None, primary_contact: Union[int, None] = None, is_event: bool = False, event_time: Union[datetime, None] = None):
    airtable.add_project(name, tags = tags, description = description, region = region, primary_contact = primary_contact)

def remove_project(project: pr):
    airtable.remove_project(pr.get_id(project))

get_project_data()