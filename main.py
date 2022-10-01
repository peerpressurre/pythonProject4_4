num1 = int(input('Enter first number->'))
num2 = int(input('Enter second number->'))

if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp

while num1>num2:
    print(f'num1 = {number}')
    num1-=1
 print(f'number = {number}. Робота циклу завершена')