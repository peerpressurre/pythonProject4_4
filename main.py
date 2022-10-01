num1 = int(input('Enter first number->'))
num2 = int(input('Enter second number->'))
number = num1
if number % 2 == 0:
    number += 1
else:
 while number < num2:
     print(f'{number}')
     number += 2
 else:
     print(f'{number}. Робота циклу завершена')
print('Робота програми завершена')