from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException
import schemas, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/tag', status_code = status.HTTP_201_CREATED, tags = ['tags'])
def create(request: schemas.Tag, db: Session = Depends(get_db)):
    new_tag = models.Tag(name = request.name, group_id = 12) # need to change
    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    return new_tag

@app.delete('/tag/{id}', status_code = status.HTTP_204_NO_CONTENT, tags = ['tags'])
def destroy(id, db: Session = Depends(get_db)):
    tag = db.query(models.Tag).filter(models.Tag.id == id)
    if not tag.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Tag with the id {id} is not found")
    tag.delete(synchronize_session = False)
    db.commit()
    return 'Tag with the id ' + id + ' is deleted successfully'

@app.put('/tag/{id}', status_code = status.HTTP_202_ACCEPTED, tags = ['tags'])
def update(id, request: schemas.Tag, db: Session = Depends(get_db)):
    tag = db.query(models.Tag).filter(models.Tag.id == id)
    if not tag.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Tag with the id {id} is not found")
    tag.update({'name': request.name})
    db.commit()
    return 'Tag with the id ' + id + ' is updated successfully'

@app.get('/tag', response_model = List[schemas.ShowTag], tags = ['tags'])
def all(db: Session = Depends(get_db)):
    tags = db.query(models.Tag).all()
    return tags

@app.get('/tag/{id}', status_code = 200, response_model = schemas.ShowTag, tags = ['tags'])
def show(id, response: Response, db: Session = Depends(get_db)):
    tag = db.query(models.Tag).filter(models.Tag.id == id).first()
    if not tag:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Tag with the id {id} is not available")
    return tag



@app.post('/tag_group', status_code = status.HTTP_201_CREATED, tags = ['tag_groups'])
def create(request: schemas.TagGroup, db: Session = Depends(get_db)):
    new_tag_group = models.TagGroup(name = request.name)
    db.add(new_tag_group)
    db.commit()
    db.refresh(new_tag_group)
    return new_tag_group

@app.delete('/tag_group/{id}', status_code = status.HTTP_204_NO_CONTENT, tags = ['tag_groups'])
def destroy(id, db: Session = Depends(get_db)):
    tag_group = db.query(models.TagGroup).filter(models.TagGroup.id == id)
    if not tag_group.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"TagGroup with the id {id} is not found")
    tag_group.delete(synchronize_session = False)
    db.commit()
    return 'TagGroup with the id ' + id + ' is deleted successfully'

@app.put('/tag_group/{id}', status_code = status.HTTP_202_ACCEPTED, tags = ['tag_groups'])
def update(id, request: schemas.TagGroup, db: Session = Depends(get_db)):
    tag_group = db.query(models.TagGroup).filter(models.TagGroup.id == id)
    if not tag_group.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"TagGroup with the id {id} is not found")
    tag_group.update({'name': request.name})
    db.commit()
    return 'TagGroup with the id ' + id + ' is updated successfully'

@app.get('/tag_group', response_model = List[schemas.ShowTagGroup], tags = ['tag_groups'])
def all(db: Session = Depends(get_db)):
    tag_groups = db.query(models.TagGroup).all()
    return tag_groups

@app.get('/tag_group/{id}', status_code = 200, response_model = schemas.ShowTagGroup, tags = ['tag_groups'])
def show(id, response: Response, db: Session = Depends(get_db)):
    tag_group = db.query(models.TagGroup).filter(models.TagGroup.id == id).first()
    if not tag_group:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"TagGroup with the id {id} is not available")
    return tag_group