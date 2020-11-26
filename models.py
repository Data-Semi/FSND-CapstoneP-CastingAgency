from flask_sqlalchemy import SQLAlchemy
from flask import (Flask, render_template, request,
                   Response, redirect, url_for, jsonify, abort)
from flask_migrate import Migrate

database_name = "casting_agency"
# database_path = "postgres://{}/{}".format('localhost:5432', database_name)
database_path = ("postgres://uwqovqkwvpffuf:9e9d3fd95e3a" +
                 "68c7f1c938764ffaf28fe886c33f0f663a36ed12" +
                 "a7df49c1daf5@ec2-54-235-116-235.compute-1." +
                 "amazonaws.com:5432/d8dahk3smdf985")
db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    # migrate = Migrate(app, db) , if use this line,
    # delete line db.create_all() avobe.


class db_updating_methods(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


class Movies(db_updating_methods):
    __tablename__ = 'movies'

    title = db.Column(db.String)
    release_date = db.Column(db.Date)


class Actors(db_updating_methods):
    __tablename__ = 'actors'

    name = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
