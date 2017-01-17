# -*- coding: utf-8 -*-
"""Estimate models"""
import datetime
from quote.extensions import db


class Estimate(db.Model):
    """Estimate model"""

    __tablename__ = 'estimates'

    id = db.Column(db.Integer, primary_key=True)
    estimate_number = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    line_items = db.relationship('LineItem', backref='estimate', lazy='dynamic')
    terms = db.Column(db.Text, nullable=True)
    note = db.Column(db.Text, nullable=True)
    tax_rate = db.Column(db.Float, nullable=False)
    date_of_issue = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class LineItem(db.Model):
    """Estimate model"""

    __tablename__ = 'line_items'

    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Integer, nullable=False)
    invoice_estimate_id = db.Column(db.Integer, db.ForeignKey('estimates.id'))
    description = db.Column(db.String(300), nullable=False)
    rate = db.Column(db.Numeric(8, 2), nullable=False)
    qty = db.Column(db.Float, nullable=False)
