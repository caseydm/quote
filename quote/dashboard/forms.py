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


class AddClientForm(Form):
    """
    Add a client
    """
    fname = StringField('First name', validators=[InputRequired()])
    lname = StringField('Last name', validators=[InputRequired()])
    email = StringField('Email')
    phone = StringField('Phone')
    address1 = StringField('Address line 1')
    address2 = StringField('Address line 2')
    city = StringField('City')
    state = StringField('State')
    zip_code = StringField('Zip code')
