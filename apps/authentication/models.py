# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin

from sqlalchemy.orm import relationship
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin

from apps import db, login_manager

from apps.authentication.util import hash_pass

class Users(db.Model, UserMixin):
    

    __tablename__ = 'Users'

    id            = db.Column(db.Integer, primary_key=True)
    username      = db.Column(db.String(64), unique=True)
    email         = db.Column(db.String(64), unique=True)
    password      = db.Column(db.LargeBinary)
    phone_number = db.Column(db.Integer, nullable=True)

    first_name      = db.Column(db.String(64), nullable=True)
    last_name       = db.Column(db.String(64), nullable=True)

    address         = db.Column(db.String(64), nullable=True)
    city            = db.Column(db.String(64), nullable=True)
    state           = db.Column(db.String(64), nullable=True)
    country         = db.Column(db.String(64), nullable=True)
    zip_code        = db.Column(db.String(64), nullable=True)

    about_me        = db.Column(db.String(64), nullable=True)
    picture_filepath  = db.Column(db.String(64), nullable=True)

    oauth_github  = db.Column(db.String(100), nullable=True)

    '''If you add more fields, you need to migrate the database.
       1. In a terminal, run: flask db migrate -m "Initial migration."
       2. Then run: flask db upgrade
    '''

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)

    def update(self, update_dictionary: dict):
        for col_name in self.__table__.columns.keys():
            if col_name in update_dictionary:
                setattr(self, col_name, update_dictionary[col_name])

    def __repr__(self):
        big_string = ''
        for col_name in self.__table__.columns.keys():
            big_string += f'{col_name}: {getattr(self, col_name)} '
        return big_string



class Companys(db.Model):
    

    __tablename__ = 'Companys'

    id            = db.Column(db.Integer, primary_key=True)
    email         = db.Column(db.String(64), unique=True)
    phone_number = db.Column(db.Integer, nullable=True)

    company_name    = db.Column(db.String(64), nullable=False)

    address         = db.Column(db.String(64), nullable=True)
    city            = db.Column(db.String(64), nullable=True)
    state           = db.Column(db.String(64), nullable=True)
    country         = db.Column(db.String(64), nullable=True)
    zip_code        = db.Column(db.String(64), nullable=True)

    instruction_pay_rate = db.Column(db.Integer, nullable=True)

    '''If you add more fields, you need to migrate the database.
       1. In a terminal, run: flask db migrate -m "Initial migration."
       2. Then run: flask db upgrade
    '''

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)

    def update(self, update_dictionary: dict):
        for col_name in self.__table__.columns.keys():
            if col_name in update_dictionary:
                setattr(self, col_name, update_dictionary[col_name])

    def __repr__(self):
        big_string = ''
        for col_name in self.__table__.columns.keys():
            big_string += f'{col_name}: {getattr(self, col_name)} '
        return big_string


















@login_manager.user_loader
def user_loader(id):
    return Users.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = Users.query.filter_by(username=username).first()
    return user if user else None

class OAuth(OAuthConsumerMixin, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id", ondelete="cascade"), nullable=False)
    user = db.relationship(Users)
