from sqlalchemy import (
    create_engine, Column,  Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Favorite Game" table
class FavoriteGame(base):
    __tablename__ = "FavoriteGame"
    id = Column(Integer, primary_key=True)
    release_year = Column(Integer)
    console_name = Column(String)
    company = Column(String)
    

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on our Favotite Game table
need_for_speed = FavoriteGame(
    release_year=2000,
    console_name="Sony",
    company="EA Game Production"
    
)

fifa = FavoriteGame(
    release_year=2015,
    console_name="Xbox",
    company="EA Game Production"
    
)


ufc = FavoriteGame(
    release_year=2020,
    console_name="Sony",
    company="EA Game Production"
    
)

wow = FavoriteGame(
    release_year=2020,
    console_name="PC",
    company="EA Game Production"
    
)
# add each instance of our programmers to our session
#session.add(need_for_speed)
session.add(fifa)
session.add(ufc)
session.add(wow)
# commit our session to the database
session.commit()


# query the database to find all Favorite Games
games = session.query(FavoriteGame)
for game in games:
    print(
        game.id,
        game.release_year,
        game.console_name,
        game.company,
        sep=" | "
    )