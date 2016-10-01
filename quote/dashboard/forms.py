from flask.ext.wtf import Form
from wtforms.fields import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired


class AddCategoryForm(Form):
    """
    Add a category
    """
    name = StringField('Name', validators=[InputRequired()])
    parent = SelectField('Parent', coerce=int)
    description = TextAreaField('Description')
