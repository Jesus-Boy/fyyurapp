# from flask import Flask, render_template, request, Response, flash, redirect, url_for
# from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
# import logging
# from logging import Formatter, FileHandler
# from flask_wtf import Form
# from sqlalchemy import ForeignKey
# from forms import *
# from flask_migrate import Migrate

# app = Flask(__name__)
# moment = Moment(app)
# app.config.from_object('config')
db = SQLAlchemy()

# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String(120)))
    need_talent = db.Column(db.Boolean, default= False)
    talent_description = db.Column(db.String())

    show = db.relationship('Show', backref='venue', lazy= True)
    

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String(120)))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    need_venue = db.Column(db.Boolean, default= False)
    venue_description = db.Column(db.String())

    show = db.relationship('Show', backref='artist', lazy= True)




    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

class Show(db.Model):
  __tablename__ = 'Show'

  id = db.Column(db.Integer, primary_key= True)
  artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
  venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable= False)
  date = db.Column(db.String(), nullable= False)