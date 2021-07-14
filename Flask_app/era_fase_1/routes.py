from era_fase_1 import app
from flask import render_template
from era_fase_1.models import Item
from era_fase_1.forms import RegisterForm
#This is how we put multiple routes to one page
@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')# this redirects to my html file

@app.route('/formato_tetis')
def formato_tetis_page():
    items = Item.query.all() #This returns all the items stored in our database
    return render_template('formato_tetis.html', items=items)

@app.route('/register')
def register_page():
    form = RegisterForm()
    #To display the field in the HTML page
    return render_template('register.html', form=form)
