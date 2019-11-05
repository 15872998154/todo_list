from flask_wtf import FlaskForm
from wtforms import SubmitField,IntegerField, StringField, BooleanField,  TextAreaField, SelectMultipleField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired

class ListForm(FlaskForm):
    
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    tag = SelectField('Status', choices = [('Uncomplete','Uncomplete'), ('Complete','Complete')],validators=[DataRequired()])
    deadline = DateField('Deadline', format='%Y-%m-%d')
    submit = SubmitField('submit', render_kw={'class': 'btn btn-success'})

class DeadlineForm(FlaskForm):
    deadline = DateField('Deadline', format='%Y-%m-%d')
    submit = SubmitField('query by deadline', render_kw={'class': 'btn btn-success'})