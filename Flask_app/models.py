""" This says to our application that this is a model that is going to be a table inside our database """
class Item(db.Model):
    #Rigth here we create our columns for the database
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True) #This is the way to create a column -> inside the parentesis is the type of column
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self): #This is to see the items in the database
        return f'Item {self.name}'