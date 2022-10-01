num1 = int(input('Enter first number->'))
num2 = int(input('Enter second number->'))
temp = ''

if num1 > num2:
    num1 = temp
    num2 = num1
    temp = num2
number = num1

if number % 2 == 0:
    number += 1

while number < num2:
    print(f'{number}')
    number += 2

print('Робота програми завершена')
