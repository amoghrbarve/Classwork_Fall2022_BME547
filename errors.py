def function_name():
    try: 
        answer = 1/0
    except ZeroDivisionError:
    answer = 0
    print("Division by zero is not possible")
    print(answer)
    return answer


def main():
    function_name()


if __name__ == "__main__":
    main()
