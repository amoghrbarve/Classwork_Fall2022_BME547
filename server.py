from flask import Flask, request, jsonify
app = Flask(__name__)  # Generally put it in global section of the code

@app.route("/", methods=["GET"])
def server_status():
    return "server is on"

@app.route("/info", methods=["GET"])
def information():
    return "besa me culo machin"

@app.route("/hdl_check", methods=["POST"])
def hdl_check_from_internet():
    """

    incoming json = {"name":<name_str>,
                     "hdl_value": <hdl_value_int>"}
    """

    from blood_calc import check_HDL
    in_data = request.get_json()
    hdl_value = in_data["hdl_value"]
    answer = check_HDL(hdl_value)
    print(hdl_value)
    return answer

@app.route("/add_numbers", methods=["POST"])
def add_numbers_from_internet():
    """

    incoming json = {}
    """

    in_data = request.get_json()
    a = in_data["a"]
    b = in_data["b"]
    answer = a + b
    print(answer)
    return jsonify(answer)


if __name__ == "__main__":
    app.run()
