# Variable assignment
num = 23
greet = 'welcome'
price = 4.56
is_raining = True  # False

# Check variable type
variable_type = type(is_raining)
print(variable_type)

name = "John Oliver"
print(name[0])  # get first letter
print(name[-1])  # get last letter

# Slicing: [start:stop:step]
first_name = name[:4:]
print(first_name)
last_name = name[5:]
print(last_name)

# .format
print("My best friend name is {f} {l}".format(f=first_name, l=last_name))

# Strings are immutable
# name[0] = 'R' not allowed
new_name = 'R' + name[1:]
print(new_name)

# Concatenation (str + int not allowed)
# need to typecast from int to str
age = 45
print(name + str(age))

# methods
print(name.capitalize())
print(len(name))

# split method (convert string into list)
fav_place_to_visit = "I like to go to canada and india"
fav_place_list = fav_place_to_visit.split()
print(fav_place_list)

# join method (merge list back into string)
print(" ".join(fav_place_list))
