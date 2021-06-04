#while loop
index = 1
while index <= 5:
    print(index)
    index = index + 1  # if you don't add this then while loop will run infinite
    # index += 1  # more compact way to write


# break, continue, pass statements to use within loops
num = [1,2,3,4,5]
for item in num:
    # will add later
    pass

# for item in num:
    if item == 4:
        continue
    print(item)

for item in num:
    if item == 3:
        break
    print(item)
