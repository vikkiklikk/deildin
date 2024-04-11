from flask import request, jsonify
from config import app, db
from models import Contact

@app.route("/contacts", methods=["GET"])
def get_contacts():
  contacts = Contact.query.all() #uses flask alchemy to get all the contacts
  json_contacts = list(map(lambda x: x.to_json(), contacts)) #converts the python model into json list
  return jsonify({"contacts": json_contacts})





# Spin up the database if it does not exist
if __name__ == "__main__":
  with app.app_context():
    db.create_all()


  app.run(debug=True)