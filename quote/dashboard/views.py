# -*- coding: utf-8 -*-
"""Dashboard views"""
from flask import Blueprint, render_template
from flask.ext.security import login_required

blueprint = Blueprint('dashboard', __name__, static_folder='../static')


@blueprint.route('/dashboard')
@login_required
def index():
    return render_template('dashboard/index.html')