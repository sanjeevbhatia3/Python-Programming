# open the file
my_file = open('test.txt')

# error when file is not defined
my_file = open('colors.txt')

# read the file
content = my_file.read()
print(content)
# file is read in string
print(type(content))

# to get the cursor location
print(my_file.tell())

print("read file again")
my_file.seek(5)
read_again = my_file.read()
print(read_again)

# use readline method
my_file.seek(0)
line = my_file.readline()
print(line)

# use readlines method
my_file.seek(0)
list_line = my_file.readlines()
print(list_line)

# close the file
my_file.close()
# check if file is closed (True/False)
print(my_file.closed)

# use this method if dont want to worry about closing the file
with open('test.txt', 'r') as my_file:
    content = my_file.read()
    print(content)

# append some text
with open('test.txt', 'a') as my_file:
    my_file.write('Hey universe')

with open('test.txt', 'r') as my_file:
    updated_file = my_file.read()
    print(updated_file)

# create file and write some text
with open('xyz.txt', 'w') as f:
    f.write("Hi there!")