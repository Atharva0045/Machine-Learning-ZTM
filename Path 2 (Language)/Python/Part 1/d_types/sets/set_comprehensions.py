my_set = {char for char in 'Hello'}
print(my_set)
print()

numbers = {num for num in range(50)}
print(numbers)
print()

even_numbers = {num for num in numbers if num % 2 == 0}
print(even_numbers)