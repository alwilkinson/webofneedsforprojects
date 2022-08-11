from project_main import get_projects_list
import re
from typing import List, Union, Dict
from Project_Class import Project as pr
from datetime import datetime
from models import Tag

# This is a basic script to filter data based on search filters. I plan to include a better matching algorithm for the name matching
    # and allow for less advanced searches, but this is a starting point.

data = get_projects_list()

def filter_search(data: List[pr], name_include: Union[str, None] = None, tags_include: Union[List[Tag], None] = None, name_exclude: Union[List[str], None] = None, tags_exclude: Union[Tag, None] = None, before_date: Union[datetime.date, None] = None, after_date: Union[datetime.date, None] = None, description_include: Union[List[str], None] = None, description_exclude: Union[List[str], None] = None) -> Union[List[pr], Dict[pr, List[str]]]:
    """Filters searches based on strings to include in the name, tags to include, strings to exclude from the name, tags to exclude, and whether it was created before or after a given date.
    Only direct matches with the name will cause inclusion or exclusion."""
    display: Union[List[pr], Dict[pr, List[str]]] = data
    if tags_include or tags_exclude:
        display = filter_tags(display, tags_include, tags_exclude)
    if name_include or name_exclude:
        display = filter_name(display, name_include, name_exclude)
    if before_date or after_date:
        display = filter_date_created(display, before_date, after_date)
    if description_include or description_exclude:
        display = filter_description(display, description_include, description_exclude)
    return display
    
    
def filter_tags(data: List[pr], tags_include: Union[List[Tag], None] = None, tags_exclude: Union[List[Tag], None] = None) -> Dict[pr: List[Tag]]:
    """Returns a dictionary whose keys are the projects that include at least one tag from tags_include and have no tags from tags_exclude,
    and whose values are the corresponding list of matching tags to include."""
    filtered: dict = {}
    for project in data:
        if contains_tags(project, tags_exclude) == None:
            tags = contains_tags(project, tags_include)
            if tags_include != None and tags != None:
                filtered += {project: tags}
    return filtered
    
def contains_tags(project: pr, tags: Union[List[Tag], None]) -> Union[List[Tag], None]:
    """Returns a list of matching tags if a project has any tags from a given list and None if it has no tags or the tags parameter was given None.""" 
    if tags == None:
        return None
    matching_tags = []
    for tag in tags:
        if tag in pr.get_tags(project):
            matching_tags.append(tag)
    return matching_tags if len(matching_tags) > 0 else None

def filter_name(data: Union[List[pr], Dict[pr, List[str]]], name_include: Union[List[str], None] = None, name_exclude: Union[List[str], None] = None) -> Union[List[pr], Dict[pr, List[str]]]:
    """Returns a list of projects whose name contains at least one string out of name_include and no strings out of name_exclude. If given a dictionary,
    it will instead return a dictionary filtered by the same criteria."""
    out: List[pr] = []
    if type(data) == list:
        projects_list: list = data
    else:
        projects_list: list = data.keys
    for project in projects_list:
        if name_contains(project, name_include) and not name_contains(project, name_exclude):
            out.append(project)
    return out if type(data) == list else {project:data[project] for project in out}

def name_contains(project: pr, patterns: List[str]) -> bool:
    if patterns == None:
        return True
    for pattern in patterns:
        match = re.search(pattern, pr.get_name(project))
        if match != None:
            return True
    return False

def filter_date_created(data: Union[List[pr], Dict[pr, List[str]]], before_date: Union[datetime.date, None] = None, after_date: Union[datetime.date, None] = None) -> Union[List[pr], Dict[pr, List[str]]]:
    out: List[pr] = []
    if type(data) == list:
        projects_list: list = data
    else:
        projects_list: list = data.keys
    for project in projects_list:
        if created_before(project, before_date) and created_after(project, after_date):
            out.append(project)
    return out if type(data) == list else {project:data[project] for project in out}

def created_before(project: pr, date: Union[datetime.date, None] = None) -> bool:
    return True if date == None or pr.get_date_created < date else False

def created_after(project: pr, date: Union[datetime.date, None] = None) -> bool:
    return True if date == None or pr.get_date_created > date else False

def filter_description(data: Union[List[pr], Dict[pr, List[str]]], description_include: Union[List[str], None] = None, description_exclude: Union[List[str], None] = None) -> Union[List[pr], Dict[pr, List[str]]]:
    """Returns a list of projects whose description contains at least one string out of description_include and no strings out of description_exclude. If given a dictionary,
    it will instead return a dictionary filtered by the same criteria."""
    out: List[pr] = []
    if type(data) == list:
        projects_list: list = data
    else:
        projects_list: list = data.keys
    for project in projects_list:
        if description_contains(project, description_include) and not description_contains(project, description_exclude):
            out.append(project)
    return out if type(data) == list else {project:data[project] for project in out}

def description_contains(project: pr, patterns: List[str]) -> bool:
    if patterns == None:
        return True
    for pattern in patterns:
        match = re.search(pattern, pr.get_description(project))
        if match != None:
            return True
    return False

#fiter by region

#filter by event vs not

#filter by event time


if __name__ == "__main__":
    print('Including Creative Writing:', end = '')
    filter_search(data, "Creative Writing")
    print('Including JS and excluding C', end = '')
    filter_search(data, "JS", None, "C")