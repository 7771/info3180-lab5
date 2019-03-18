from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, DateField
from flask_wtf.file import FileField, FileRequired, FileAllowed, DataRequired
from wtforms.validators import InputRequired
from flask_sqlalchemy import SQLAlchemy

class Profile(FlaskForm):
    #username = StringField('Username', validators=[DataRequired()])
    #password = PasswordField('Password', validators=[DataRequired()])
    firstname = StringField('Firstname', validators=[DataRequired()])
    lastname = StringField('Lastname', validators=[DataRequired()])
    email = StringField('Email')#, validators=[Required()])
    location = StringField('Location')#, validators=[InputRequired()])
    gender = SelectField(option=[('male'),('female')])
    biography = StringField('Biography')
    created_on = DateField('Created_On')
    
class Photo(FlaskForm):
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])
    description = StringField('Description', validators=[DataRequired()])
    
