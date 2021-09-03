def add_two_numbers(number1, number2):
    if type(number1) is not int or type(number2) is not int:
        raise TypeError("Type mismatch")

    result = number1 + number2
    return result


# print(add_two_numbers(2, "hi"))

def divide_two_numbers(number1, number2):
    if number2 == 0:
        raise ValueError("Divide by zero is not allowed!")
    result = number1 / number2
    return result