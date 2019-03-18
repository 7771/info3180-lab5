from flask import Flask
#from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(12)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://lrjbyvmjvfbgiv:060d61f325fce981a143f955e01b4a38ef64368f3b31be135a163a38500d17e4@ec2-75-101-133-29.compute-1.amazonaws.com:5432/d3psed55guvtgj'"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
