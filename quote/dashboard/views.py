# -*- coding: utf-8 -*-
"""Dashboard views"""
from flask import Blueprint, render_template, redirect, url_for
from flask.ext.security import login_required
from .models import Category, Product, Duration, Circulation, \
    ImageSize, ImageLocation
from .forms import AddCategoryForm
from quote.extensions import db

blueprint = Blueprint('dashboard', __name__, static_folder='../static')


def build_category_dropdown(categories, depth=0):
    '''Builds category data for parent select field'''
    items = []
    for category in categories:
        items.append((category.id, '-' * depth + ' ' + category.name))
        if category.children:
            items += build_category_dropdown(category.children, depth + 1)
    return items


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
def products():
    products = Product.query.all()
    return render_template('dashboard/products.html', products=products)


@blueprint.route('/dashboard/categories', methods=['GET', 'POST'])
@login_required
def categories():
    # form setup
    form = AddCategoryForm()
    query = Category.query.get(1).children
    categories = build_category_dropdown(query)
    form.parent.choices = categories

    # options queries
    duration = Duration.query.all()
    circulation = Circulation.query.all()
    image_size = ImageSize.query.all()
    image_location = ImageLocation.query.all()

    # form submit
    if form.validate_on_submit():
        description = form.description.data
        if form.description.data == '':
            description = None
        category = Category(
            name=form.name.data,
            parent_id=form.parent.data,
            description=description
        )
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('dashboard.categories'))

    return render_template(
        'dashboard/categories.html',
        categories=categories,
        duration=duration,
        circulation=circulation,
        image_size=image_size,
        image_location=image_location,
        form=form
    )
