# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 16:07:13 2020

@author: augus
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Import Tables
from content_base import Base, Album, Artist, Track, Tags

# bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
engine = create_engine('sqlite:///content.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object.
session = DBSession()

# Create a database

for k in range(50):
    session.add(Album())
    session.add(Artist())
    session.add(Track())

album1 = Album()
album2 = Album()
album1.tags = [Tags(tag='tag_a'), Tags(tag='tab_b')]
album1.tags = [Tags(tag='tag_c')]


artist1 = Artist()
artist2 = Artist()
artist1.tags = [Tags(tag='tag_a'), Tags(tag='tab_b')]
artist1.tags = [Tags(tag='tag_c')]

track1 = Track()
track2 = Track()
track1.tags = [Tags(tag='tag_a'), Tags(tag='tab_b')]
track1.tags = [Tags(tag='tag_c')]

session.add_all([album1,album2,artist1,artist2,track1,track2])

#commits changes
session.commit()  

