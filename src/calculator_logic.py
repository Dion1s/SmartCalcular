import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def calculate_factorial(calc_operator):
    return str(factorial(int(calc_operator)))

def calculate_sin(calc_operator):
    return str(math.sin(math.radians(int(calc_operator))))

def calculate_cos(calc_operator):
    return str(math.cos(math.radians(int(calc_operator))))

def calculate_tan(calc_operator):
    return str(math.tan(math.radians(int(calc_operator))))

def calculate_cot(calc_operator):
    return str(1 / math.tan(math.radians(int(calc_operator))))

def calculate_square_root(calc_operator):
    if int(calc_operator) >= 0:
        return str(eval(calc_operator + '**(1/2)'))
    else:
        return "ERROR"

def calculate_third_root(calc_operator):
    if int(calc_operator) >= 0:
        return str(eval(calc_operator + '**(1/3)'))
    else:
        return "ERROR"

def change_sign(calc_operator):
    if calc_operator[0] == '-':
        return calc_operator[1:]
    else:
        return '-' + calc_operator

def calculate_percent(calc_operator):
    return str(eval(calc_operator + '/100'))

def calculate_expression(calc_operator):
    return str(eval(calc_operator)) 