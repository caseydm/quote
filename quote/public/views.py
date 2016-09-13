# -*- coding: utf-8 -*-
"""Public section, including homepage."""
from flask import Blueprint, render_template
from flask.ext.security import login_required

blueprint = Blueprint('public', __name__, static_folder='../static')


@blueprint.route('/')
@login_required
def home():
    return render_template('public/index.html')
