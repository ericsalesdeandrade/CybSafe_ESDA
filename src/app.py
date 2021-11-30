from flask import Flask, jsonify, request
from src.get_pokemon import Pokemon
from src.helpers.postgres_access import DBAccess

app = Flask(__name__)  # create an app instance


@app.route("/")
def hello():
    """
    Endpoint to check if the API is working
    :return:
    """
    return jsonify({"Result": "Hello! Pokemon API is up and running"})


@app.route("/create_table", methods=['GET'])
def create_database():
    """
    Endpoint to create table
    :return:
    """
    try:
        if request.method == 'GET':
            db_obj = DBAccess()
            db_obj.create_table()
            return jsonify({"Result": "Succeeded"})
    except Exception as error:
        print(error)
        return jsonify({"Result": "Failed"})


@app.route("/store_pokemon", methods=['GET'])
def store_pokemon():
    """
    Endpoint to store required number of pokemon in table,
    takes 'quantity' (int) as GET Argument
    :return:
    """
    try:
        if request.method == 'GET':
            poke = Pokemon()
            poke.get_data_pokemon_api(qty=request.args.get("quantity"))
            poke.store_pokemon()
            return jsonify({"Result": "Succeeded"})
    except Exception as error:
        print(error)
        return jsonify({"Result": "Failed"})


@app.route("/get_pokemon", methods=['GET'])
def get_pokemon():
    """
    Endpoint to get all pokemon from table
    """
    try:
        if request.method == 'GET':
            poke = Pokemon()
            records = poke.get_pokemon()
            return jsonify({"Result": "Succeeded", "records": records})
    except Exception as error:
        print(error)
        return jsonify({"Result": "Failed"})


if __name__ == "__main__":  # on running python app.py
    app.run()  # run the flask app
