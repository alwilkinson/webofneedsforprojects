from datetime import datetime
from typing import Union, List
from tag_api.models import Tag

class Project:
    """Simple object to represent a project"""
    __slots__ = '_id', '_name', '_tags', '_description', '_date_created', '_region', '_creator_id', '_is_event', '_event_time'

    def __init__(self, id: str, name: str, tags: List[Tag] = [], description: Union[str, None] = None, region: Union[str, None] = None, creator_id: Union[int, None] = None, is_event: bool = False, event_time: Union[datetime, None] = None):
        self._id = id
        self._name = name
        self._tags = tags
        self._description = description
        self._date_created = datetime.today()
        self._region = region
        self._creator_id = creator_id
        self._is_event = is_event
        self._event_time = event_time

    #-------------------------- public accessors --------------------------

    def get_id(self) -> str:
        return self._id
    
    def get_tags(self) -> List[Tag]:
        return self._tags

    def get_name(self) -> str:
        return self._name

    def get_description(self) -> Union[str, None]:
        return self._description

    def get_date_created(self) -> datetime.date:
        return self._date_created
    
    def get_region(self) -> Union[str, None]:
        return self._region

    def get_creator_id(self) -> Union[int, None]:
        return self._creator_id
    
    def get_event_time(self) -> Union[datetime, None]:
        return self._event_time
    #-------------------------- nonpublic mutators --------------------------

    def add_tags(self, tags = Union[Tag, List[Tag]]):
        if type(tags) == Tag:
            self._tags.append(tags)
        else:
            self._tags += tags
    
    def remove_tags(self, tags = Union[Tag, List[Tag]]):
        if type(tags) == Tag:
            if tags in self._tags:
                self._tags.remove(tags)
        else:
            for tag in tags:
                if tag in self._tags:
                    self._tags.remove(tag)
