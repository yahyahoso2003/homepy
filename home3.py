numbers = []

numbers.append(int(input('enter first number: ')))
numbers.append(int(input('enter second number: ')))
numbers.append(int(input('enter third number: ')))
numbers.append(int(input('enter fourth number: ')))
numbers.append(int(input('enter fifth number: ')))

max = numbers[0]
if max < numbers[1]:
    max = numbers[1]
if max < numbers[2]:
    max = numbers[2]
if max < numbers[3]:
    max = numbers[3]
if max < numbers[4]:
    max = numbers[4]

min = numbers[0]
if min > numbers[1]:
    min = numbers[1]
if min > numbers[2]:
    min = numbers[2]
if min > numbers[3]:
    min = numbers[3]
if min > numbers[4]:
    min = numbers[4]


print('Max =',max)
print('Min =',min)