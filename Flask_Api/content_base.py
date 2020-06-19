
import sys

# for creating the mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

# for creating foreign key relationship between the tables
from sqlalchemy.orm import relationship

# for configuration
from sqlalchemy import create_engine

# create declarative_base instance
Base = declarative_base()


 #classes
class Album(Base):
    __tablename__ = 'album'
    id = Column(Integer, primary_key=True)

    @property
    def serialize(self):
        return {
            'id': self.id,
        }

class Artist(Base):
    __tablename__ = 'artist'
    id = Column(Integer, primary_key=True)

    @property
    def serialize(self):
        return {
            'id': self.id,
        }
    
class Track(Base):
    __tablename__ = 'track'
    id = Column(Integer, primary_key=True)

    @property
    def serialize(self):
        return {
            'id': self.id,
        }


from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

#Tags is related to the other classes
class Tags(Base):
    __tablename__ = "tags"
    
    id = Column(Integer, primary_key=True)
    tag = Column(String, nullable = False)
    
    album_id = Column(Integer, ForeignKey('album.id'))  #allows us to join the tables
    album = relationship("Album", back_populates="tags")
    
    artist_id = Column(Integer, ForeignKey('artist.id')) #allows us to join the tables
    artist = relationship("Artist", back_populates="tags")
    
    Track_id = Column(Integer, ForeignKey('track.id')) #allows us to join the tables
    track = relationship("Track", back_populates="tags")
    
    @property
    def serialize(self):
        return {
            'tag': self.tag,
        }

#Creates the relationships
Album.tags = relationship("Tags", order_by=Tags.id, back_populates="album")
Artist.tags = relationship("Tags", order_by=Tags.id, back_populates="artist")
Track.tags = relationship("Tags", order_by=Tags.id, back_populates="track")

# creates a create_engine instance at the bottom of the file
engine = create_engine('sqlite:///content.db')
Base.metadata.create_all(engine)