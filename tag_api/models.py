from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    group_id = Column(Integer, ForeignKey('tag_groups.id'))
    group = relationship('TagGroup', back_populates = 'tags')

class TagGroup(Base):
    __tablename__ = 'tag_groups'
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    tags = relationship('Tag', back_populates = 'group')