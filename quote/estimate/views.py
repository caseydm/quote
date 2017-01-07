# -*- coding: utf-8 -*-
"""Estimate views"""
from flask import Blueprint, render_template, abort, request, jsonify
from flask_security import login_required, current_user
import arrow
from quote.dashboard.models import Client
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
    if not request.json:
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
