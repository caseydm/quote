# -*- coding: utf-8 -*-
"""Item Category models"""
from quote.extensions import db


class Category(db.Model):
    """Item Category model"""

    __tablename__ = 'categories'

    id = db.Column(db.Integer(), primary_key=True)
    parent_id = db.Column(db.Integer)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))


class Option(db.Model):
    """Item options model"""

    __tablename__ = 'options'

    id = db.Column(db.Integer(), primary_key=True)
    description = db.Column(db.String(255))


class Product(db.Model):
    """Product model"""

    __tablename__ = 'products'

    id = db.Column(db.Integer(), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    options = db.Column(db.PickleType)
    price = db.Column(db.String(255))
