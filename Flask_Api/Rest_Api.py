# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 17:21:54 2020

@author: augus
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#import Tables
from content_base import Base, Album, Artist, Track, Tags

# Connect to Database and create database session
engine = create_engine('sqlite:///content.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

from flask import jsonify

#va permettre de faire la fonction export
def get_taggedcontent():
    albums = session.query(Album).join(Tags).filter(Album.tags!=None).all()
    artists = session.query(Artist).join(Tags).filter(Artist.tags!=None).all()
    tracks = session.query(Track).join(Tags).filter(Track.tags!=None).all()

    response=[]
    for a in albums:
        content = [{"type": "album", "id" : str(a.id)}]
        response+=content
    for b in artists:
        content = [{"type": "album", "id" : str(b.id)}]
        response+=content
    for t in tracks:
        content = [{"type": "album", "id" : str(t.id)}]
        response+=content
    return jsonify(response)

def updateContent(Table, table_id, tags):
    updatedContent = session.query(Table).filter_by(id=table_id).one()
    updatedContent.tags += tags
    session.add(updatedContent)
    session.commit()
    return 'Updated a Book with id %s' % id


def getcontent(Table,tags):
    L = []
    for row in session.query(Table).join(Tags).filter(Table.tags.contains(tags)).all():
        L += row.id
    return jsonify (L)

@app.route('/')
@app.route('/export', methods=['GET'])
def exportFunction():
    return get_taggedcontent()

@app.route('/<string:table>/<int:id>', methods=['POST'])
def contenttracks(table,id):
    tags = request.args.get('tags')
    if table == 'album':    
        return updateContent(Album,id, tags)
    elif table == 'artist':
        return updateContent(Artist,id, tags)
    elif table == 'track':
        return updateContent(Track,id, tags)

@app.route('/<string:table>', methods=['GET'])
def findContent(table):
    tags = request.args.get('tags')
    if table == 'album':    
        return getcontent(Album, tags)
    elif table == 'artist':
        return getcontent(Artiste, tags)
    elif table == 'track':
        return getcontent(Track, tags)

if __name__ == '__main__':
    app.run(debug=True)
