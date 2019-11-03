from flask_wtf import FlaskForm
from wtforms import SubmitField,IntegerField, StringField, BooleanField,  TextAreaField, SelectMultipleField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired

class ListForm(FlaskForm):
    # id = IntegerField('Id',validators=[DataRequired()])
    # date = DateField('Date', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    tag = SelectField('Status', choices = [('Uncomplete','Uncomplete'), ('Complete','Complete')],validators=[DataRequired()])
    submit = SubmitField('submit')