from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlachemy import orm
from sqlalchemy.orm import relationship

from database import Base 

user_game_rel = Table(
    "association",
    Base.metadata,
    Column("users_id", ForeignKey("users.id")),
    Column("games_id", ForeignKey("games.id")),
)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)

    games = relationship(
        'Game', secondary=user_game_rel, backref="followers"
    )
    
    @orm.validates('age')
    def validate_age(self, key, value):
        if not 0 < value < 100:
            raise ValueError(f'Invalid age {value}')
    
class Game(Base):
    __tablename__ = 'games'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)

