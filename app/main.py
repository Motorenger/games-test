from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal

from models import User, Game

Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()


@app.get("/games")
def games_list(db: Session = Depends(get_db)):
    games = db.query(Game).all()
    for game in games:
        game.followers
    return games

@app.get("/me/{user_id}")
def read_item(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if user:
        user.games
        return user
    return {"Not found"}

@app.get("/me/{user_id}/connect/{game_id}")
def connect_game(user_id: int, game_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    game = db.query(Game).filter(Game.id == game_id).first()
    user.games.append(game)
    db.add(user)
    db.commit()
    return user
