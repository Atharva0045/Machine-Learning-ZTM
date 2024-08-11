username = input('Enter your Username: ')
password = input('Enter your Password: ')

hidden_password = '*' * len(password)

print(f'Hey {username}, your password \'{hidden_password}\' is {len(password)} letters long!')