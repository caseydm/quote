# -*- coding: utf-8 -*-
"""Item Category models"""
from quote.extensions import db


class Category(db.Model):
    """Item Category model"""

    __tablename__ = 'categories'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    description = db.Column(db.String(255))
    children = db.relationship(
        'Category',
        backref=db.backref('parent', remote_side=id)
    )


class Duration(db.Model):
    """License duration model"""

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))


class Circulation(db.Model):
    """License circulation model"""

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))


class ImageSize(db.Model):
    """License image size"""

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))


class ImageLocation(db.Model):
    """License image location"""

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))


class Product(db.Model):
    """Product model"""

    __tablename__ = 'products'

    id = db.Column(db.Integer(), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship('Category')
    circulation_id = db.Column(db.Integer, db.ForeignKey('circulation.id'))
    circulation = db.relationship('Circulation')
    duration_id = db.Column(db.Integer, db.ForeignKey('duration.id'))
    duration = db.relationship('Duration')
    image_size_id = db.Column(db.Integer, db.ForeignKey('image_size.id'))
    image_size = db.relationship('ImageSize')
    image_location_id = db.Column(db.Integer, db.ForeignKey('image_location.id'))
    image_location = db.relationship('ImageLocation')
    price = db.Column(db.Numeric(6, 2), nullable=False)
