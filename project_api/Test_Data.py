from Project_Class import Project as pr
from typing import List, Union
from datetime import datetime
import project_airtable_api as airtable
from tag_api.models import Tag
import json

def get_project_data() -> List[pr]:
    data = json.loads(airtable.get_projects())["records"]
    projects: List[pr] = []
    for project in data:
        fields = project["fields"]
        projects.append(pr(project["id"], fields["Name"], fields["Tags"], fields["Description"], fields["Region"], fields["Primary_Contact"]))
    return projects
    

def create_project(name: str, tags: List[Tag] = [], description: Union[str, None] = None, region: Union[str, None] = None, primary_contact: Union[int, None] = None, is_event: bool = False, event_time: Union[datetime, None] = None):
    airtable.add_project(name, tags = tags, description = description, region = region, primary_contact = primary_contact)

def remove_project(project: pr):
    airtable.remove_project(pr.get_id(project))
