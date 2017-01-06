# -*- coding: utf-8 -*-
"""Estimate views"""
from flask import Blueprint, render_template
from flask_security import login_required
import arrow

blueprint = Blueprint('estimate', __name__, static_folder='../static')


@blueprint.route('/dashboard/estimates/new')
@login_required
def new_estimate():
    today = arrow.now().format('MMMM DD, YYYY')
    return render_template('dashboard/estimate/new_estimate.html', today=today)
