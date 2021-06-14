# divide two numbers without error handling
def divide_num(a, b):
    output = a / b
    print(f'Division output of {a} divided by {b} is {output}')


# divide two numbers with error handling
def divide_num(a, b):
    try:
        output = a / b
    except ZeroDivisionError:
        print("Don't divide by zero")
    else:
        print(f'Division output of {a} divided by {b} is {output}')
    finally:
        print(f'divide_num function is executed!')


# divide two numbers with different type error handling
def divide_num(a, b):
    try:
        output = a / b
    except ZeroDivisionError:
        print("Don't divide by zero")
    except TypeError:
        print("Given numbers should be int or float")
    else:
        print(f'Division output of {a} divided by {b} is {output}')
    finally:
        print(f'divide_num function is executed!')


# combine different error handling
def divide_num(a, b):
    try:
        output = a / b
    except (ZeroDivisionError, TypeError) as er:
        print("Some error occurs")
        print(er)
    else:
        print(f'Division output of {a} divided by {b} is {output}')
    finally:
        print(f'divide_num function is executed!')


# execute method
divide_num(3, 0)