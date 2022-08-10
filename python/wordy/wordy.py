import re

operations = {
    '+': lambda a, b : a + b,
    '-': lambda a, b : a - b,
    '*': lambda a, b : a * b,
    '/': lambda a, b : a / b,
}

def answer(question):
    # convert question to equation
    equation = question_to_equation(question)

    # check for proper equation format
    validate_equation(equation)

    # convert equation string to list
    equation = equation.split(' ')

    # assign first equation value to result
    result = int(equation[0])

    # find each operation and perform calculation
    for index in range(len(equation)):
        if index % 2 != 0:
            operation = equation[index]
            operand = int(equation[index+1])
            result = operations.get(operation)(result, operand)

    return result

def question_to_equation(question):
    # Convert question sring to equation string
    equation = re.sub(r'^What is|\?', '', question)
    equation = re.sub(r'plus', '+', equation)
    equation = re.sub(r'minus', '-', equation)
    equation = re.sub(r'multiplied by', '*', equation)
    equation = re.sub(r'divided by', '/', equation)
    equation = equation.strip()

    return equation

def validate_equation(equation):
    # check for foreign values in equation string
    if re.search(r'[a-zA-Z]', equation):
        raise ValueError('unknown operation')

    # convert equation string to list
    equation = equation.split(' ')

    # check that equation has odd length
    if len(equation) % 2 == 0:
        raise ValueError('syntax error')
    
    # check for numbers at even indexes
    for index in range(0, len(equation), 2):
        try:
            int(equation[index])
        except:
            raise ValueError('syntax error')
    
    # check for operators at odd indexes
    for index in range(1, len(equation), 2):
        if equation[index] not in operations:
            raise ValueError('syntax error')