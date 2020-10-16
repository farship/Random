#calculator using variable and evaluate
def variables_Evaluate():
    x = input("first number: ")
    method = input("method: ")
    y = input("second number: ")
    method_dict = {
        'multiply' : '*',
        'divide' : '/',
        'add' : '+',
        'subtract' : '-'}
    z = eval(x + method_dict[method] + y)
    print (z)


def evaluatePure():
    methods = ['Add = +', 'Subtract = -', 'Multiply = *', 'Divide = /', 'Power = **']
    for line in methods:
        print (line)
    equation = input("What's the Equation? \n")
    print (str(eval(equation)))
    evaluatePure()
    
evaluatePure()
