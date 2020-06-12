import hashlib
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///db.sqlite3")
Base = declarative_base()


class Artist(Base):
    __tablename__ = "artist"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    music_s = relationship("Music", backref="artist")


class Album(Base):
    __tablename__ = "album"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    music_s = relationship("Music", backref="album")


class Music(Base):
    __tablename__ = "music"
    md5 = Column(String, primary_key=True)
    title = Column(String)
    artist_id = Column(Integer, ForeignKey("artist.id"))
    album_id = Column(Integer, ForeignKey("album.id"))


Base.metadata.create_all(engine)
Session = sessionmaker(engine)
