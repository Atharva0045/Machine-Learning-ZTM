cart = ['Notebooks', 'Sunglasses', 'Pen', 'Bottle', 'Gaming Mouse', 'Wallet', 'Charger', 'Laptop']

# len(): returns the length of the list
print(len(cart))

# .append(): adds item to the end of the list
cart.append('Cable')
print('After append:', cart)

# .insert(): insert a value at an index in the list
cart.insert(1, 'Shaker')
print('After insert:', cart)

# .extend(): extends the list with another iterable object -> like another list

# .pop(): removes the end item of the list, if provided an index, removes the item at that index!

# .remove(): removes all occurances of the provided value

# .clear(): clears the entire list

# .index(): gives index of provided value

# .count(): return how many occurances are there

# .sort(): sorts the list in place
# sorted(): creates new sorted instance of the object

# .reverse(): reverses the list in place