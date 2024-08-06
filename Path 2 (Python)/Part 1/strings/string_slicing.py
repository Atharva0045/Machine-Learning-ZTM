# string indices start with 0 and go till (string_length-1)
string = 'Atharva'
print(string[0])

# to get the length of string, we can use the len() function!
print(len(string))


# string slicing using Index of the string:
# it allows us to grab a specific part of the string

# slicing: [start : stop : stepover]

print(string[0:2]) # (Prints At): starts with the first index provided and goes till (second_index-1)
print(string[0:len(string)]) # prints full string
print(string[3:]) # starts at given index and grabs every index after
print(string[:5]) # starts at 0 and goes till (provided-1)

# step over in slicing: add a third slice parameter to jump over positions while slicing
print(string[0:len(string):2]) # (Prints Ahra)



# Negative indexing and Slicing
# last position holds -1 index as well.. therefore, we can do tricks with this!
print(string[-1:2:-1]) # rules apply same but since the step over is -1, it goes backwards!

# trick to reverse a string:
reverse = string[::-1]
print(f'Reverse String: {reverse}')