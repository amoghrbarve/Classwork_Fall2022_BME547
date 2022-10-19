import requests
# r = requests.get("http://127.0.0.1:5000/info")
# print(r.status_code)
# print(r.text)

# out_data = {"name":"Amogh",
#             "hdl_value": 5}
# r = requests.post("http://127.0.0.1:5000/hdl_check", json = out_data)
# print(r.status_code)
# print(r.text)


out_data = {"a":50, "b": 5}
r = requests.post("http://127.0.0.1:5000/add_numbers", json = out_data)
print(r.status_code)
print(r.text)
