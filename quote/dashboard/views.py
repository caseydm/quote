# -*- coding: utf-8 -*-
"""Dashboard views"""
from flask import Blueprint, render_template, redirect, url_for
from flask.ext.security import login_required
from .models import Category
from .forms import AddCategoryForm
from quote.extensions import db

blueprint = Blueprint('dashboard', __name__, static_folder='../static')


def build_choice_tree():
    categories = Category.query.get(1).children
    items = [(1, 'None')]
    for root in categories:
        items.append((root.id, root.name))
        if root.children:
            for subcat1 in root.children:
                items.append((subcat1.id, '- ' + subcat1.name))
                if subcat1.children:
                    for subcat2 in subcat1.children:
                        items.append((subcat2.id, '--' + subcat2.name))
    return items


def build_choice_tree2(categories):
    items = []

    def loop(categories):
        for category in categories:
            items.append((category.id, category.name))
            if category.children:
                loop(category.children)
        return items
    result = loop(categories)
    return result


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
    categories = Category.query.get(1).children
    form = AddCategoryForm()
    form.parent.choices = build_choice_tree2(categories)

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

    categories = Category.query.filter_by(parent_id=1)
    return render_template(
        'dashboard/categories.html',
        categories=categories,
        form=form
    )
