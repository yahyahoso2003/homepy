from math import *
num1 = input('Enter the first number: ')

if num1.isdigit():
    operation = input('Enter the operation (1 for +, 2 for -, 3 for *, 4 for /, 5 for ^, 6 for %): ')

num2 = input('Enter the second number: ')
if num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
result=0
if operation == '1' or operation=='+':
  result = num1 + num2
elif operation == '2' or operation=='-':
  result = num1 - num2
elif operation == '3' or operation=='*':
  result = num1 * num2
elif operation == '4' or operation=='/':
  result = num1 / num2
elif operation == '5' or operation=='^':
  result = num1 ** num2
elif operation == '6' or operation=='%':
  result = num1 % num2

print('Result:', result)


print('1_ Normal rounding, up or down a number')
print('2_ Take the number without a decimal point')
print('3_ Exit')
options = input("Enter the option: ")

if options == "1":
  round_type = input('Enter Normal for a normal rounding, Up for a rounding to the highest number available, Down for a rounding to the lowest number available:')
  if round_type == 'Normal':
    result = round(result)
  elif round_type == 'Up':
    result= ceil(result)
  elif round_type == 'Down':
    result = floor(result)
  print('close output:', result)
elif options == '2':
  result = int(result)
  print('Output without a decimal point:', result)
elif options == '3':
  print('Thank you!')
  exit()
