from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route("/add", methods=["POST"])
def add_numbers():
    r = request.get_json()

    try:
        first_number = r["first_number"]
    except (KeyError, TypeError):
        return jsonify({"error": "first_number is a required field in the request body"}), 400

    try:
        second_number = r["second_number"]
    except (KeyError, TypeError):
        return jsonify({"error": "second_number is a required field in the request body"}), 400

    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        return jsonify({"error": "Both first_number and second_number need to be integer values"}), 400

    return jsonify({"result": result}), 200


@app.route("/test", methods=["GET"])
def test():

    return jsonify({"message": "success"}), 200
