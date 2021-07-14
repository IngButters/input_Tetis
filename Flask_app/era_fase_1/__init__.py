from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__) #We initialize the flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datos.db' #COnfigure the route of the database
app.config['SECRET_KEY'] = '2b81318a88e8c289cf329a01'
db = SQLAlchemy(app)# To initialize the class
from era_fase_1 import routes