def interface():
    print("Blood Calculator: ")
    print("Options: ")
    print("1 - Answer: ")
    print("9 - Quit: ")
    keep_running = True
    choice = input("Enter choice: ")
    if choice == "9":
        return ()
    elif choice == "1":
        HDL_driver()


def input_HDL():
    HDL_input = input("Enter the HDL value: ")
    return int((HDL_input))


def check_HDL(HDL_input):
    if HDL_input > 60:
        return "Normal"
    elif HDL_input <= 60 and HDL_input > 40:
        return "Borderline"
    else:
        HDL_input < 40
        return "Low"


def HDL_driver():
    hdl_value = input_HDL()
    answer = check_HDL(hdl_value)
    output_HDL_result(hdl_value, answer)


def output_HDL_result(hdl_value, charac):
    print("The results for an HDL value of {} is {}".format(hdl_value.charac))


if __name__ == "__main__":
    interface()
    input_HDL()
