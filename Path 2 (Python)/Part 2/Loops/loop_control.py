# break statement: exits the current loop

for i in range(10):
    if i == 5:
        break

    print(i)

print()

# continue: skips the current iteration of the loop

for i in range(10):
    if i == 5:
        continue

    print(i)


# pass: it is just a placeholder when devs haven't decided what to do there
# not usually used!