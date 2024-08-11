# functions are the block of code that does certain task
# they can be 'called' number of times

def say_hello():
    print("Helloooooooo")

say_hello() # calling a function


# function with parameters:

def print_number(a):
    print(a)

number = 10
print_number(number)

# function with return:

def sum(num1, num2):
    return num1 + num2


print(f'Sum: {sum(14, 34)}')
print(f'Sum: {sum(10, 34.5)}')

total = sum(23, 4)
print(f'Sum: {total}')