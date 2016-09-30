# -*- coding: utf-8 -*-
"""Dashboard views"""
from flask import Blueprint, render_template, redirect, url_for
from flask.ext.security import login_required
from .models import Category
from .forms import AddCategoryForm
from quote.extensions import db

blueprint = Blueprint('dashboard', __name__, static_folder='../static')


def build_category_list():
    '''Builds category data for parent select field'''
    categories = Category.query.get(1).children
    items = []

    def loop(categories, depth):
        for category in categories:
            items.append((category.id, '-' * depth + ' ' + category.name))
            if category.children:
                loop(category.children, depth + 1)
        return items

    return loop(categories, 0)


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


@blueprint.route('/dashboard/categories', methods=['GET', 'POST'])
@login_required
def edit_categories():
    form = AddCategoryForm()
    form.parent.choices = build_category_list()

    # form submit
    if form.validate_on_submit():
        category = Category(
            name=form.name.data,
            parent_id=form.parent.data,
            description=form.description.data
        )
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('dashboard.edit_categories'))

    categories = build_category_list()
    return render_template(
        'dashboard/categories.html',
        categories=categories,
        form=form
    )
