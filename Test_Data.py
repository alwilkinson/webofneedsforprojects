from Project_Class import Project as pr
from typing import List, Union
from datetime import datetime

ids = {1, 2, 3}
website = pr(1, "Website", ["JS", "C"], "Build a website.")
church_plant = pr(2, "Church Planting", ["Evangelism"], "Planting churches in hard-to-reach areas.")
book = pr(3, "Children's Storybook", ["Creative Writing"], "Writing Bible stories in a format children can understand.")

data = [website, church_plant, book]

def get_projects() -> List[pr]:
    return data

def create_project(new_id: int, title: str, tags: List[str] = [], description: Union[str, None] = None, region: Union[str, None] = None, phone: Union[int, None] = None, email: Union[str, None] = None, is_event: bool = False, event_time: Union[datetime, None] = None):
    if not new_id in ids:
        data.append(pr(new_id, title, tags, description, region, phone, email, is_event, event_time))
        ids.add(new_id)
    else:
        print("That project ID already exists. Please try again.")

def remove_project(project: pr):
    data.remove(project)
    ids.remove(pr.get_id(project))
