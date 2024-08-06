# string: str
# it is a sequence of characters, simply alpha-numeric along with any special characters

username = 'super_coder'
password = 'super_secret'

# short strings are defined either in ' ' or " "
# long strings are defined in ''' '''


# concatenate two strings:
first = 'Atharva'
last = 'Aher'

full_name = first + ' ' + last
print(full_name)


# Escape sequence:
# in order to print some special characters, we use the escape sequences

example = 'It\'s \"kind of" sunny'
print(example)
# by normal means we wouldn't have been able to print the inverted comma's, by using the escape sequence '\', it was made possible
# \t = tab
# \n = new line, enter


# formatted strings:
name = 'Atharva' 
print(f'My name is: {name}')