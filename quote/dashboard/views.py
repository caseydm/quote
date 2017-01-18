# -*- coding: utf-8 -*-
"""Dashboard views"""
from flask import Blueprint, render_template, redirect, url_for, flash, request, abort, jsonify
from flask_security import login_required, current_user
from .models import Category, Product, Duration, Circulation, \
    ImageSize, ImageLocation, Client
from .forms import AddCategoryForm, AddClientForm
from quote.estimate.models import Estimate
from quote.security.models import User
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
    estimates = Estimate.query.filter_by(user_id=current_user.id).all()
    user = User.query.get(current_user.id)
    initial_setup = user.initial_setup
    return render_template(
        'dashboard/index.html',
        initial_setup=initial_setup,
        estimates=estimates
    )


@blueprint.route('/dashboard/clients/new', methods=['GET', 'POST'])
@login_required
def new_client():
    form = AddClientForm()
    if form.validate_on_submit():
        data = form.data

        # set empty form strings to None
        data = {k: None if v == '' else v for k, v in data.items()}

        # add user id
        data['user_id'] = current_user.get_id()

        # save to database
        client = Client(**data)
        db.session.add(client)
        db.session.commit()

        flash('Client saved')
        return redirect(url_for('dashboard.new_client'))
    return render_template('dashboard/new_client.html', form=form)


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
    categories.insert(0, (1, ''))  # root option
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
        parent_id = form.parent.data
        category = Category(
            name=form.name.data,
            parent_id=parent_id,
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


@blueprint.route('/api/business_setup', methods=['POST'])
@login_required
def setup_business():
    # validate data
    if not request.json or request.json['fname'] == '':
        abort(400)

    user = User.query.get(current_user.id)

    # edit user object
    user.fname = request.json['fname']
    user.lname = request.json['lname']
    user.business_name = request.json['business_name']
    user.phone = request.json['phone']
    user.initial_setup = True

    # save to database
    db.session.commit()

    return jsonify({'success': 'business info updated'}), 201
