def calculate():
  
  operation = input('''
  Please type in the math operation you wold like to complete:
  + for additon
  - for subtraction
  * for multiplication
  / for division
  ** for power
  % for modulo
  ''')

  number_1 = int(input('Enter your first number: '))
  number_2 = int(input('Enter your second number: '))

  if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

  elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

  elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

  elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

  elif operation == '**':
    print('{} ** {} = '.format(number_1, number_2))
    print(number_1 ** number_2)

  elif operation == '%':
    print('{} % {} = '.format(number_1, number_2))
    print(number_1 % number_2)

  else:
    print('You have not typed a valid operator, please run the program again.')

  again()

def again():

  calc_again = input('''
  Do you want to calculate again?
  Please type Y for YES or N for No.
  ''')

  if calc_again.upper() == 'Y':
    calculate()

  elif calc_again.upper() == 'N':
    print('See you later.')

  else:
    again()

calculate()