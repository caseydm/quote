from flask.ext.wtf import Form
from wtforms.fields import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired


class AddCategoryForm(Form):
    """
    Add a category
    """
    name = StringField('Name', validators=[InputRequired()])
    parent = SelectField('Parent', choices=[
        ('1', 'None'),
        ('2', 'Digital Media'),
        ('3', 'Advertising'),
        ('5', 'Email Marketin')
    ])
    description = TextAreaField('Description')
