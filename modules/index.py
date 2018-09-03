from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import json
from bson import json_util
import datetime
import config

app = Flask(__name__)

app.config["MONGO_DBNAME"] = config.mongodb_name
app.config["MONGO_URI"] = config.mongo_uri 

mongo = PyMongo(app)

@app.route("/", methods=["GET"])
def home():
    return "sup fam"

@app.route("/users", methods=["GET"])
def get_all_users():
    users = mongo.db["_User"]

    output = []

    for user in users.find():
        user["_id"] = str(user["_id"])
        output.append(user)
    return_json = jsonify({"results": output})
    return return_json

@app.route("/user/<user_id>", methods=["GET"])
def find_user_by_id(user_id):
    users = mongo.db["_User"]
    user_found = users.find_one({"_id": user_id})

    if user_found:
        json_output = jsonify({"results": user_found})
    else:
        json_output = jsonify({"results": "No users found."})
    return json_output

@app.route("/new_user", methods=["POST"])
def create_new_user():
    # connect to database
    users = mongo.db["_User"]

    # create new user from information given on the request
    firstName = request.json["firstName"]
    username = request.json["username"]
    password = request.json["password"]
    email = request.json["email"]
    fakeName = request.json["fakeName"]
    age = request.json["age"]
    dob = request.json["dob"]
    gender = request.json["gender"]
    interestedIn = request.json["interestedIn"]
    minAge = request.json["minAge"]
    maxAge = request.json["maxAge"]
    occupation = request.json["occupation"]
    lastLocation = request.json["lastLocation"]
    education = request.json["education"]
    bio = request.json["bio"]

    new_user_json = {
        "firstName": firstName,
        "username": username,
        "password": password,
        "email": email,
        "fakeName": fakeName,
        "age": age,
        "dob": dob,
        "gender": gender,
        "interestedIn": interestedIn,
        "minAge": minAge,
        "maxAge": maxAge,
        "occupation": occupation,
        "lastLocation": lastLocation,
        "education": education,
        "bio": bio 
    }

    new_user_id = users.insert(new_user_json)

    print(new_user_id)

    # new_user = users.find_one({"_id": new_user_id})

    return jsonify({"User succesfully created": new_user_json})

@app.route("/conversations", methods=["GET"])
def get_all_conversations():
    conversations = mongo.db.Conversation
    all_convos = []
    for conv in conversations.find():
        all_convos.append(conv)
    return_json = jsonify({"results": all_convos})
    return return_json

@app.route("/conversation/<conv_id>", methods=["GET"])
def find_conversation_by_id(conv_id):
    conversations = mongo.db.Conversation
    conversation_found = conversations.find_one({"_id":conv_id})
    if conversation_found:
        json_output = jsonify({"results": conversation_found})
    else:
        json_output = jsonify({"results": "No conversations found."})
    return json_output

# @app.route("/new_conversation", methods=["POST"])
# def create_new_conversation():
#     conversations = mongo.db.Conversation

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
