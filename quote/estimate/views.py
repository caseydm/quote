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

    # get highest estimate number from db
    query = db.session.query(
        db.func.max(Estimate.estimate_number)
    ).filter(Estimate.user_id == current_user.id).scalar()

    if query:
        next_estimate = query + 1
    else:
        next_estimate = 1

    # format next_estimate with leading zeros
    next_estimate = '{0:04d}'.format(next_estimate)

    return render_template(
        'dashboard/estimate/new_estimate.html',
        today=today,
        next_estimate=next_estimate
    )


@blueprint.route('/dashboard/estimate/<id>')
@login_required
def view_estimate(id):
    estimate = Estimate.query.filter_by(
        user_id=current_user.id,
        id=id
    ).first_or_404()

    return render_template(
        'dashboard/estimate/view_estimate.html',
        estimate=estimate)


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

    required_fields = ['estimate_number', 'user_id', 'client_id', 'tax_rate', 'total', 'tax_total', 'sub_total']
    for field in required_fields:
        if field is None:
            abort(400)

    estimate = Estimate(
        estimate_number=request.json['estimate_number'],
        user_id=request.json['user_id'],
        client_id=request.json['client_id'],
        terms=request.json['terms'],
        note=request.json['note'],
        tax_rate=request.json['tax_rate'],
        sub_total=request.json['sub_total'],
        tax_total=request.json['tax_total'],
        total=request.json['total']
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

    return jsonify({'success': 'estimate saved'}), 201
