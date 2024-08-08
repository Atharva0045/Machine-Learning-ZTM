# for loop: the for loop iterates over a range or an iterable.. 
# the for loop may use two common functions: range() and enumerate()

# range(start(optional, default=0), stop, stepover):
for i in range(10):
    print(i, end=" ")

print()

for j in range(-1, 20, 2):
    print(j, end=" ")

print()


# enumerate(iterable): gives index as well as value!

for index, value in enumerate('Atharva'):
    print(index, value)

print()


# enumerate() with a dict:

hash_table = {'Name': 'Atharva',
              'Age': 92,
              'Dept': 'AI'}

for index, (key, value) in enumerate(hash_table.items()):
    print(f"Index: {index}, Key: {key}, Value: {value}")


# while loop: while loop runs according to a condition

var = 1
while var <= 10:
    print(var)
    var += 1