# conditional logic can be used to manupulate the flow of the program!

# we use conditional statements for this:
#   1) if: executes statements only if condition is true
#   2) if-else: executes statements only if condition is true, if not, executes the else statement
#   3) if-elif-else: holds multiple expressions and conditions, else is optional


is_old = True
is_licenced = False

if is_old:
    print('You are old enough')

if is_licenced:
    print('Good to go for driving, yayyyyyy!')
else:
    print('Not so good for driving though')


num = 10

if num == 1:
    print('Heyyy')
elif num == 10:
    print('Lol yes')

# use of and/or/not (user can nest them also)

if not is_old: #executes if and only if the negation of expression is True
    print('Not old')

if is_old and is_licenced: # executes if and only if both of the expressions are True
    print('Good for driving and also of age!')

if is_old or is_licenced: # executes if and only if one of the expressions is True
    print('One or Both condition met')

if is_old and not is_licenced:
    print('Only age is satisfied!')


# ternary operator: shortcut for if-else

number = 10
result = 'Number is 10' if number == 10 else 'Number is not 10'
print(result)