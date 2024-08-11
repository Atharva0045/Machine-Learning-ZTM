dictionary = {'AI': 'Atharva', 'Comp': 'Aakanksha'}

# .get(): if a key doesn't exist and is tried to access, it creates a new key in dict
# if provided a optional parameter {default}, assigns it as default value instead of None

print(dictionary.get('IT'))
print(dictionary.get('EnTC', 'Sahil'))

# .keys(): returns the keys of the dict
print(dictionary.keys())

# .values(): returns the values of the dict
print(dictionary.values())

# .items(): returns the items of the dict as tuple
print(dictionary.items())

# .pop(): pops the item of the dict and returns it's value!
print(dictionary.pop('IT'))