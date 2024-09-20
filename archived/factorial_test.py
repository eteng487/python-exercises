def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


usrInput = input('Please enter a number or \'exit\' to end: ')
print('Factorial of {} is: {}'.format(int(usrInput),factorial(int(usrInput))))
