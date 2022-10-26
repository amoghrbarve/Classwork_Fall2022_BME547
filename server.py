# from flask import Flask, request, jsonify
# app = Flask(__name__)  # Generally put it in global section of the code

# @app.route("/", methods=["GET"])
# def server_status():
#     return "server is on"

# @app.route("/info", methods=["GET"])
# def information():
#     return "besa me culo machin"

# @app.route("/hdl_check", methods=["POST"])
# def hdl_check_from_internet():
#     """

#     incoming json = {"name":<name_str>,
#                      "hdl_value": <hdl_value_int>"}
#     """

#     from blood_calc import check_HDL
#     in_data = request.get_json()
#     hdl_value = in_data["hdl_value"]
#     answer = check_HDL(hdl_value)
#     print(hdl_value)
#     return answer

# @app.route("/add_numbers", methods=["POST"])
# def add_numbers_from_internet():
#     """

#     incoming json = {}
#     """

#     in_data = request.get_json()
#     a = in_data["a"]
#     b = in_data["b"]
#     answer = a + b
#     print(answer)
#     return jsonify(answer)


# if __name__ == "__main__":
#     app.run()
from flask import Flask, jsonify, request
from datetime import datetime, time
app = Flask(__name__)

@app.route("/", methods = ["GET"])
def server_status():
    return "Server is on"


def get_time():
    time = datetime.now().time()
    return time


def get_date():
    date = datetime.now().date()
    return date


def get_age(in_data):
    if in_data["units"] == "years":
        format = "%m/%d/%y"
        birthdate = datetime.strptime(in_data["date"], format)
        date_now = datetime.now().date()
        age = date_now - birthdate
        age_years = age/365
        return age_years
    else:
        return 0


def time_until_next_meal(meal):
    time_now = datetime.now().time()
    breakfast_time = time(8, 0, 0)
    lunch_time = time(13, 0, 0)
    dinner_time = time(20, 0, 0)

    meal_time = meal+"_time"

    if time_now <= meal_time:
        until_next_meal = time_now - meal_time
    else:
        until_next_meal = 24 + time_now - meal_time

    return until_next_meal


@app.route("/time", methods = ["GET"])
def send_time():
    time = get_time()
    return time


@app.route("/date", methods = ["GET"])
def send_date():
    date = get_date()
    return date


@app.route("/age", methods = ["POST"])
def send_age():
    in_data = request.get_json()
    age_years = get_age(in_data)
    return age_years, 200


@app.route("/until_next_meal/<meal>", methods = ["GET"])
def send_meal():
    meal = request.get_json()
    until_next_meal = time_until_next_meal(meal)
    return until_next_meal, 200


if "__name__" == "__main__":
    app.run(port=4996)
