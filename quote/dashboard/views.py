# -*- coding: utf-8 -*-
"""Dashboard views"""
from flask import Blueprint, render_template
from flask.ext.security import login_required
from .models import Category

blueprint = Blueprint('dashboard', __name__, static_folder='../static')


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
    categories = Category.query.all()
    return render_template('dashboard/categories.html', categories=categories)
