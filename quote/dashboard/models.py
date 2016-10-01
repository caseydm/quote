# -*- coding: utf-8 -*-
"""Item Category models"""
from quote.extensions import db


class Category(db.Model):
    """Item Category model"""

    __tablename__ = 'categories'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    parent_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    description = db.Column(db.String(255))
    children = db.relationship(
        'Category',
        backref=db.backref('parent', remote_side=id)
    )


class Duration(db.Model):
    """License duration model"""

    id = db.Column(db.Integer(), primary_key=True)
    description = db.Column(db.String(255))

    # amount to multiple from base_price
    factor = db.Column(db.Integer())


class Circulation(db.Model):
    """Lisence circulation model"""

    id = db.Column(db.Integer(), primary_key=True)
    description = db.Column(db.String(255))

    # amount to multiply from base_price
    factor = db.Column(db.Integer())


class Product(db.Model):
    """Product model"""

    __tablename__ = 'products'

    id = db.Column(db.Integer(), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    size = db.Column(db.String(255))
    location = db.Column(db.String(255))
    base_price = db.Column(db.String(255))
