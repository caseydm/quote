# -*- coding: utf-8 -*-
"""Public section, including homepage."""
from flask import Blueprint, render_template

blueprint = Blueprint('public', __name__, static_folder='../static')


@blueprint.route('/')
def home():
    return render_template('public/index.html')
