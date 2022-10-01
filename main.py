num1 = int(input('Enter first number->'))
num2 = int(input('Enter second number->'))
number = num2

while num1 < number < num2:
    print(f'number = {number}')
    number -= 1
else:
    print(f'number = {number}. Робота циклу завершена')