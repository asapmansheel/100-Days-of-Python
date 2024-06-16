import art
from replit import clear

# Calculator Functions
def plus(first_number,second_number):
  return first_number + second_number

def minus(first_number,second_number):
  return first_number - second_number

def multiply(first_number,second_number):
  return first_number * second_number

def divide(first_number,second_number):
  return first_number / second_number

# Operations Dictionary
operations = {'+' : plus, '-' : minus, '*' : multiply, '/' : divide}

should_continue = True

def calculator():
  print(art.logo)
  first_number = float(input("What's the first number?: "))
  for key in operations:
    print(key)


  while should_continue:
    operation = input('Pick an operation: ')
    second_number = float(input("What's the next number?: "))
    
    calculation_function = operations[operation]
    result = calculation_function(first_number,second_number)
    
    print(f'{first_number} {operation} {second_number} = {result}')
    
    continue_calculation = input('Type "y" to continue calculating with {result}, or type "n" to start a new calculation: ')
  
    if continue_calculation == 'y':
      first_number = result
    else:
      clear()
      calculator()
    

calculator()
