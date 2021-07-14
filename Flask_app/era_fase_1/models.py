from era_fase_1 import db

class User(db.Model):
    #Rigth here we create our columns for the database
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    #for passwords it's different we have to store it encrypted
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    #to allow the users to own several items here we apply relationship field
    #backref let's us know which items does the user own
    #Item is so that the db relates to the exiting on
    #Always leave lazy=True so the db can get all the items in one call
    items = db.relationship('Item', backref='owned_user', lazy=True)


""" This says to our application that this is a model that is going to be a table inside our database """
class Item(db.Model):
    #Rigth here we create our columns for the database
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True) #This is the way to create a column -> inside the parentesis is the type of column
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    #This field is so we can create a foreign key
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))


    def __repr__(self): #This is to see the items in the database
        return f'Item {self.name}'