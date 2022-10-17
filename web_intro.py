#%%

import requests
r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/machoman")
print(r)
print(type(r))
print(r.text)


# if r.status_code == 200:
#     answer = r.json()
#     print(answer)
#     for branch in answer:
#         print(branch["name"])

# output_info = {"Name": "Amogh Barve",
#                 "net_id": "arb155",
#                 "e-mail": "amogh.barve@duke.edu"}
output_info = {"user":"ab", "message":"You prayer answered"}
r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
                   json=output_info)

