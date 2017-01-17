# -*- coding: utf-8 -*-
"""Estimate views"""
from flask import Blueprint, render_template, abort, request, jsonify
from flask_security import login_required, current_user
import arrow
from quote.dashboard.models import Client
from quote.estimate.models import Estimate, LineItem
from quote.extensions import db

blueprint = Blueprint('estimate', __name__, static_folder='../static')


@blueprint.route('/dashboard/estimates/new')
@login_required
def new_estimate():
    today = arrow.now().format('MMMM DD, YYYY')
    return render_template('dashboard/estimate/new_estimate.html', today=today)


@blueprint.route('/api/client', methods=['POST'])
@login_required
def create_client():
    # validate data
    if not request.json or request.json['fname'] == '':
        abort(400)

    # create Client object
    client = Client(
        user_id=current_user.id,
        fname=request.json['fname'],
        lname=request.json['lname'],
        email=request.json['email'],
        phone=request.json['phone'],
    )

    # save to database
    db.session.add(client)
    db.session.commit()

    return jsonify(client.as_dict()), 201


@blueprint.route('/api/estimate', methods=['POST'])
@login_required
def save_estimate():
    # validate data
    if not request.json:
        abort(400)

    estimate = Estimate(
        estimate_number=request.json['estimate_number'],
        user_id=request.json['user_id'],
        client_id=request.json['client_id'],
        terms=request.json['terms'],
        note=request.json['note'],
        tax_rate=request.json['tax_rate']
    )

    # process line items
    line_items = request.json['items']

    for line in line_items:
        for order, line in line.items():
            estimate.line_items.append(
                LineItem(
                    order=order,
                    description=line['description'],
                    rate=line['rate'],
                    qty=line['qty']
                )
            )

    db.session.add(estimate)
    db.session.commit()

    return jsonify(estimate.as_dict()), 201
