#This is how we put multiple routes to one page
@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')# this redirects to my html file

@app.route('/formato_tetis')
def formato_tetis_page():
    items = Item.query.all() #This returns all the items stored in our database
    return render_template('formato_tetis.html', items=items)