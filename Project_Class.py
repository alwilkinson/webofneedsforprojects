from datetime import datetime
from typing import Union, List

class Project:
    """Simple object to represent a project"""
    __slots__ = '_id', '_title', '_tags', '_description', '_date_created', '_region', '_phone', '_email', '_is_event', '_event_time'

    def __init__(self, id: int, title: str, tags: List[str] = [], description: Union[str, None] = None, region: Union[str, None] = None, phone: Union[int, None] = None, email: Union[str, None] = None, is_event: bool = False, event_time: Union[datetime, None] = None):
        self._id = id
        self._title = title
        self._tags = tags
        self._description = description
        self._date_created = datetime.today()
        self._region = region
        self._phone = phone
        self._email = email
        self._is_event = is_event
        self._event_time = event_time

    #-------------------------- public accessors --------------------------

    def get_id(self) -> int:
        return self._id
    
    def get_tags(self) -> List[str]:
        return self._tags

    def get_title(self) -> str:
        return self._title

    def get_description(self) -> Union[str, None]:
        return self._description

    def get_date_created(self) -> datetime.date:
        return self._date_created
    
    def get_region(self) -> Union[str, None]:
        return self._region

    def get_phone(self) -> Union[int, None]:
        return self._phone

    def get_email(self) -> Union[str, None]:
        return self._email
    
    def get_event_time(self) -> Union[datetime, None]:
        return self._event_time
    #-------------------------- nonpublic mutators --------------------------

    def add_tags(self, tags = Union[str, List[str]]):
        if type(tags) == str:
            self._tags.append(tags)
        else:
            self._tags += tags
    
    def remove_tags(self, tags = Union[str, List[str]]):
        if type(tags) == str:
            if tags in self._tags:
                self._tags.remove(tags)
        else:
            for tag in tags:
                if tag in self._tags:
                    self._tags.remove(tag)
