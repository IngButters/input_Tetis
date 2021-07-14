from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__) #We initialize the flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datos.db' #COnfigure the route of the database
db = SQLAlchemy(app)# To initialize the class







    




if __name__ == "__main__":
    app.run(debug=True) #This is to turn on debug mode
