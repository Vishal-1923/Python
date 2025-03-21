from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #its like saying we r going to create sql like db called data.db in same directory.
db = SQLAlchemy(app)

#class
class Drink(db.Model):#db.Model is SQLAlchemy thing, it will inherit from it. It has various built in functionalities.
    #defining columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(120))

    #overwriting another method named repr
    #will be called whenever we wanna print drink in a list
    def __repr__(self): #self means the object itself, we can grab object attributes by doing self.x or so.
        return f"{self.name} - {self.description}"

#this was how we create a model.


@app.route('/') #route is nothing but an endpoint.
def index(): #this is the method which is called when someone visits the above path.
    return "Ram Ram Ji !"

#get request
@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    # return {"drinks" : "drink data"}#its not like ki hm ise niche yaha likh d return main, we get this error: object of type Drink is not JSON serializable.
    # we have construct it in form of JSON
    output = []#an empty list
    # will iterate over drink
    for drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.description} #dictionary

        output.append(drink_data) #will add this dictionary to list

    return {"drinks" : output} #this will be serializable as we have a list of dictionaries 


#route for getting single drink via id
@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name": drink.name, "description": drink.description} #no need to do jsonify or convert to json as dictionaries are serializable. 
                        # but here the order is not guranteed as when flask convert dictionary to json it does not gurantee the same. 
                        # if u want it to be in order just use jsonify.

# post
@app.route('/drinks', methods=['POST'])
def add_drink():
# little bit tricky as we have to post the data given by user to our db.
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id} #id attribute is going to be added to this drink object.

@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"error": "not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"msg" : "yeah!!!!!"}