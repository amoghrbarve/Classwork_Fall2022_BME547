def create_patient_entry(first_name, last_name, patient_id, patient_age):
    new_patient = {"First Name":first_name, "Last Name":last_name, "Id":patient_id, "Age":patient_id, "Tests":[]}
    return new_patient
    print("new_patient")

def main():
    db = []
    db.append(create_patient_entry("Ann", "Ables", 1, 30))
    db.append(create_patient_entry("Bob", "Boyles", 2, 34))
    db.append(create_patient_entry("Chris", "Chou", 3, 25))
    print(db)

def db_seperate(db):
    for i in db:
        print("name: {},id: {}, age: {}".format(i["First Name"], i["Last Name"],i["Id"], i["Age"]))

def get_full_name(patient):
    for i in db:
        full_name = "{} {}".format(i["First Name"], i["Last Name"])
        return full_name

def match_id(db,input_value):
    for i in db:
        if i["First"] == input_value:
            print(i["First"])
            return i
    return False

def test_info(patient, test_tuple): #Adding a tuple
    patient.append(test_tuple)
    print(patient)
    return patient    

def adult_or_minor(patient):
    if patient_age >= 18:
        return("adult")
    else:
        return("minor")

# room_list = ["Room1", "Room2", "Room3"]


# #or i, patient in zip(db, room_list) 

if __name__ == "__main__":
    main()
    db = main()
    db_seperate(db)
    input_value = int(input("enter id :"))
    patient = match_id(db, input_value)
    # test_name = input("add test name ")
    # test_value = input ("add test value ")
    # test_tuple = (test_name, test_value)
    # test_info(patient, test_tuple)
