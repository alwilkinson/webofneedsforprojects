from Project_Class import Project as pr
from typing import List, Union
from datetime import datetime
import project_airtable_api as airtable
from tag_api.models import Tag

def get_project_data() -> List[pr]:
    data = airtable.get_projects()

def create_project(name: str, tags: List[Tag] = [], description: Union[str, None] = None, region: Union[str, None] = None, primary_contact: Union[int, None] = None, is_event: bool = False, event_time: Union[datetime, None] = None):
    airtable.add_project()

def remove_project(project: pr):
    airtable.remove_project(pr.get_id)
