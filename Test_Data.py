from Project_Class import Project as pr
import pandas as pd
from typing import List

ids = {1, 2, 3}
website = pr(1, "Website", ["JS", "C"])
church_plant = pr(2, "Church Planting", ["Evangelism"])
book = pr(3, "Children's Storybook", ["Creative Writing"])

data = [website, church_plant, book]

def get_projects() -> List[pr]:
    return data

def create_project(new_id: int, title: str, tags: List[str] = []):
    if not new_id in ids:
        data.append(pr(new_id, title, tags))
        ids.add(new_id)
    else:
        print("That project ID already exists. Please try again.")

def remove_project(project: pr):
    data.remove(project)
    ids.remove(pr.get_id(project))
