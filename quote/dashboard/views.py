# -*- coding: utf-8 -*-
"""Dashboard views"""
from collections import defaultdict
from flask import Blueprint, render_template
from flask.ext.security import login_required
from .models import Category
from quote.extensions import db

blueprint = Blueprint('dashboard', __name__, static_folder='../static')


def tree():
    return defaultdict(tree)


@blueprint.route('/dashboard')
@login_required
def index():
    return render_template('dashboard/index.html')


@blueprint.route('/dashboard/estimates/new')
@login_required
def new_estimate():
    return render_template('dashboard/new_estimate.html')


@blueprint.route('/dashboard/clients/new')
@login_required
def new_client():
    return render_template('dashboard/new_client.html')


@blueprint.route('/dashboard/products')
@login_required
def list_products():
    return render_template('dashboard/products.html')


@blueprint.route('/dashboard/categories')
@login_required
def edit_categories():
    parent = Category.query.get(3)
    newcat = Category(name='New One', parent=parent)
    db.session.add(newcat)
    db.session.commit()
    categories = Category.query.filter_by(parent_id=1)
    return render_template('dashboard/categories.html', categories=categories)
