my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# .discard(): discards an element from set if it exists!

# SET THOERY:
# difference of set:
print(my_set.difference(your_set))

# intersection of set:
print(my_set.intersection(your_set))

# union of set:
print(my_set.union(your_set))

# .isdisjoint(): checks if two sets have nothing in common
print(my_set.isdisjoint(your_set))

# .issubset(): checks if one set is subset of the other
print(my_set.issubset(your_set))

# .issuperset(): checks if one set is superset of the other
print(my_set.issuperset(your_set))