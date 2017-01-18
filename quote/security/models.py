# -*- coding: utf-8 -*-
"""User models"""
from flask_security import UserMixin, RoleMixin
from quote.extensions import db


roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    """User roles"""

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    """A user for the app"""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    business_name = db.Column(db.String(255), nullable=True)
    fname = db.Column(db.String(255), nullable=True)
    lname = db.Column(db.String(255), nullable=True)
    phone = db.Column(db.String(30), nullable=True)
    initial_setup = db.Column(db.Boolean)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
