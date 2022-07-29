import Test_Data
import re
from typing import List, Union
from Project_Class import Project as pr

# This is a basic script to filter data based on search filters. I plan to include a better matching algorithm for the title matching
    # and allow for less advanced searches, but this is a starting point.

search_filters = {"title_includes":[], "tags_include":[], "title_exclude":[], "tags_exclude":[]}

_data = Test_Data.get_projects()

def filter_search(title_include: Union[str, None], tags_include: Union[str, None] = None, title_exclude: Union[str, None] = None, tags_exclude: Union[str, None] = None):
    """Filters searches based on strings to include in the title, tags to include, strings to exclude from the title, and tags to exclude.
    Only direct matches with the title will cause inclusion or exclusion."""
    display = []
    for project in _data:
        if contains_tags(project, tags_exclude) == None and contains_tags(project, tags_include) != None \
            and title_contains(project, title_include) and not title_contains(project, title_exclude):
            display += project
    
def contains_tags(project: pr, tags: List[str]) -> Union[List[str], None]:
    """Returns True if a project has any tags from a given list and false if it has no tags.""" 
    matching_tags = []
    for tag in tags:
        if tag in pr.get_tags(project):
            matching_tags.append(tag)
    return matching_tags if len(matching_tags) > 0 else None

def title_contains(project: pr, titles: List[str]) -> bool:
    for title in titles:
        #if title is in the project Title
        return True
    return False
