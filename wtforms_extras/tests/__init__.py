from wtforms import (
    TextField, validators, Form, TextAreaField, BooleanField, DateField,
    DateTimeField
)
from wtforms_extras import Renderer


class TestForm(Form):
    text = TextField(u'Name', [validators.data_required()])
    textarea = TextAreaField(u'Text Area')
    boolean = BooleanField('Boolean')
    date = DateField('Date')
    datetime = DateTimeField('DateTime')

form = TestForm()
renderer = Renderer(form)
