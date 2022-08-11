from fastapi import FastAPI, status, Response, HTTPException
from fastapi.staticfiles import StaticFiles
from Project_Class import Project as pr
from typing import List, Union
from datetime import datetime
import Airtable_Api as airtable
from models import Tag
import json
import re

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# models.Base.metadata.create_all(engine)

@app.post('/project', status_code = status.HTTP_201_CREATED, projects = ['projects'])
def create_project(name: str, tags: List[Tag] = [], description: Union[str, None] = None, region: Union[str, None] = None, primary_contact: Union[int, None] = None):
    airtable.add_project(name, tags = tags, description = description, region = region, primary_contact = primary_contact)
    return f"Project {name} has been created successfully"

@app.delete(f'/project/{id}', status_code = status.HTTP_204_NO_CONTENT, projects = ['projects'])
def remove_project(project: pr):
    id = pr.get_id(project)
    airtable.remove_project(id)
    return f"Project with id {id} has been deleted successfully"

@app.put(f'/project/{id}', status_code = status.HTTP_202_ACCEPTED, projects = ['projects'])
def update(id, changes: dict):
    project = get_project(id)
    if not project:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Project with the id {id} is not found")
    airtable.update_projects_put(id, pr.get_name(project), pr.get_description(project), pr.get_region(project), pr.get_primary_contact(project))
    return f"Project with id {id} has been updated successfully"

@app.get('/project', response_model = List[pr], projects = ['project'])
def get_projects_list() -> List[pr]:
    data = airtable.get_projects()["records"]
    projects: List[pr] = []
    for project in data:
        fields = project["fields"]
        # date created requires some scraping, as the airtable keeps more precise time than we need.
        year, month, day = [int(string) for string in re.split(r'-', project["createdTime"][0:10])]
        date = datetime(year, month, day)
        projects.append(pr(project["id"], fields.get("Name", None), fields.get("Tags", None), fields.get("Description", None), date, fields.get("Region", None), fields.get("Primary_Contact", None)))
    return projects

@app.get(f'/project/{id}', status_code = 200, response_model = pr, projects = ['projects'])
def get_project(id):
    project = airtable.get_project(id)
    if not project:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Project with the id {id} is not available")
    fields = project["fields"]
    year, month, day = [int(string) for string in re.split(r'-', project["createdTime"][0:10])]
    date = datetime(year, month, day)
    return pr(project["id"], fields.get("Name", None), fields.get("Tags", None), fields.get("Description", None), date, fields.get("Region", None), fields.get("Primary_Contact", None))