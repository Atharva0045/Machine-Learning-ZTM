# list comprehensions can be used to make lists faster
# it can be done with any iterable OR from scratch

my_list = [char for char in 'Hello']
print(my_list)
print()

numbers = [num for num in range(50)]
print(numbers)
print()

even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)