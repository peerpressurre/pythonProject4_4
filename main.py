num1 = int(input('Enter first number->'))
num2 = int(input('Enter second number->'))
if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp
number = num2

while number > num1:
    print(f'{number}')
    number -= 1
else:
    print(f'{number}')