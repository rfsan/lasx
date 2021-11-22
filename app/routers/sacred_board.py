# Python standard library
from typing import List, Optional
# Core
from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy import func
from sqlalchemy.orm import Session
# Project
from .. import database, models, schemas, oauth2


router = APIRouter(
    prefix="/sacred_board",
    tags=['Sacred Board']
)


# @router.get('/', response_model=List[schemas.PostOut])
# def get_posts(
#         db: Session = Depends(get_db), 
#         current_user: int = Depends(oauth2.get_current_user),
#         limit: int = 10,
#         skip: int = 0,
#         search: Optional[str] = ""
#     ):
#     """"""
#     posts = db.query(
#         models.Post, func.count(models.Vote.post_id).label('votes')
#         ).join(
#             models.Vote, 
#             models.Vote.post_id == models.Post.id, 
#             isouter=True
#         ).group_by(models.Post.id
#         ).filter(models.Post.title.contains(search)
#         ).limit(limit
#         ).offset(skip).all()
#     return posts


@router.post(
    '/', 
    status_code=status.HTTP_201_CREATED, 
    response_model=schemas.SacredBoardResponse)
def create_post(
        sacred_board: schemas.SacredBoardCreate, 
        db: Session = Depends(database.get_db), 
        current_user: int = Depends(oauth2.get_current_user)
    ):
    """"""
    new_sacred_board = models.SacredBoard(
        owner_id=current_user.id, **sacred_board.dict())
    db.add(new_sacred_board)
    db.commit()
    db.refresh(new_sacred_board)

    return new_sacred_board


@router.get('/{id}', response_model=schemas.SacredBoardResponse) 
def get_post(
        id: int, 
        db: Session = Depends(database.get_db), 
        current_user: int = Depends(oauth2.get_current_user)
    ):
    """"""
    print(type(current_user))
    sacred_board = db.query(
        models.SacredBoard).filter(models.SacredBoard.id == id).first()
    if sacred_board is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Sacred Board with id {id} not found.')

    return sacred_board


# @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(
#         id: int, 
#         db: Session = Depends(get_db), 
#         current_user: int = Depends(oauth2.get_current_user)
#     ):
#     """"""
#     post_query = db.query(models.Post).filter(models.Post.id == id)
#     post = post_query.first()

#     if post is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, 
#             detail=f'post with id {id} not found.'
#         )
#     if post.owner_id != current_user.id:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN, 
#             detail='Not authorized to perform requested action'
#         )

#     post_query.delete(synchronize_session=False)
#     db.commit()

#     return Response(status_code=status.HTTP_204_NO_CONTENT)


# @router.put('/{id}', response_model=schemas.PostResponse)
# def update_post(
#         id: int, 
#         post: schemas.PostCreate, 
#         db: Session = Depends(get_db), 
#         current_user: int = Depends(oauth2.get_current_user)
#     ):
#     """"""
#     post_query = db.query(models.Post).filter(models.Post.id == id)
#     old_post = post_query.first()
#     if old_post is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, 
#             detail=f'post with id {id} not found.'
#         )
#     if old_post.owner_id != current_user.id:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN, 
#             detail='Not authorized to perform requested action'
#         )
    
#     post_query.update(post.dict(), synchronize_session=False)
#     db.commit()

#     return post_query.first()