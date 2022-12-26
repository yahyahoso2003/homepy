print('Welcome to Python ')

name = input('Enter a name :')
age = input('Enter a age:')
address = input('Enter a address:')

if name.isalpha() and age.isdigit():
    print('Hello Mr/Ms','name:','{',name,'}', 'age:' ,'{',age,'}' ,'locatel in:', '{',address,'}.',
          '\n thanks for beening one of our community.')
else:
    print('Invalid input, please try again.')
