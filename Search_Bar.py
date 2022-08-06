import Test_Data
import re
from typing import List, Union, Dict
from Project_Class import Project as pr
from datetime import datetime

# This is a basic script to filter data based on search filters. I plan to include a better matching algorithm for the title matching
    # and allow for less advanced searches, but this is a starting point.

search_filters = {"title_includes": [], "tags_include": [], "title_exclude": [], "tags_exclude": [], "before_date": None, "after_date": None}

_data = Test_Data.get_projects()

def filter_search(data: List[pr], title_include: Union[str, None] = None, tags_include: Union[List[str], None] = None, title_exclude: Union[List[str], None] = None, tags_exclude: Union[str, None] = None, before_date: Union[datetime.date, None] = None, after_date: Union[datetime.date, None] = None) -> Union[List[pr], Dict[pr, List[str]]]:
    """Filters searches based on strings to include in the title, tags to include, strings to exclude from the title, tags to exclude, and whether it was created before or after a given date.
    Only direct matches with the title will cause inclusion or exclusion."""
    display: Union[List[pr], Dict[pr, List[str]]] = data
    if tags_include or tags_exclude:
        display = filter_tags(display, tags_include, tags_exclude)
    if title_include or title_exclude:
        display = filter_title(display, tags_include, tags_exclude)
    if before_date or after_date:
        display = filter_date_created(display, before_date, after_date)
    return display
    
    
def filter_tags(data: List[pr], tags_include: Union[List[str], None] = None, tags_exclude: Union[List[str], None] = None):
    """Returns a dictionary whose keys are the projects that include at least one tag from tags_include and have no tags from tags_exclude,
    and whose values are the corresponding list of matching tags to include."""
    filtered: dict = {}
    for project in data:
        if contains_tags(project, tags_exclude) == None:
            tags = contains_tags(project, tags_include)
            if tags_include != None and tags != None:
                filtered += {project: tags}
    return filtered
    
def contains_tags(project: pr, tags: Union[List[str], None]) -> Union[List[str], None]:
    """Returns a list of matching tags if a project has any tags from a given list and None if it has no tags or the tags parameter was given None.""" 
    if tags == None:
        return None
    matching_tags = []
    for tag in tags:
        if tag in pr.get_tags(project):
            matching_tags.append(tag)
    return matching_tags if len(matching_tags) > 0 else None

def filter_title(data: Union[List[pr], Dict[pr, List[str]]], title_include: Union[List[str], None] = None, title_exclude: Union[List[str], None] = None) -> Union[List[pr], Dict[pr, List[str]]]:
    """Returns a list of projects whose title contains at least one string out of title_include and no strings out of title_exclude. If given a dictionary,
    it will instead return a dictionary filtered by the same criteria."""
    out: List[pr] = []
    if type(data) == list:
        projects_list: list = data
    else:
        projects_list: list = data.keys
    for project in projects_list:
        if title_contains(project, title_include) and not title_contains(project, title_exclude):
            out.append(project)
    return out if type(data) == list else {project:data[project] for project in out}

def title_contains(project: pr, patterns: List[str]) -> bool:
    if patterns == None:
        return True
    for pattern in patterns:
        match = re.search(pattern, pr.get_title(project))
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

#filter by description

#fiter by region

#filter by event vs not

#filter by event time


if __name__ == "__main__":
    print('Including Creative Writing:', end = '')
    filter_search(None, "Creative Writing")
    print('Including JS and excluding C', end = '')
    filter_search(None, "JS", None, "C")