# number = [1,2,3,4,5]


# def num_square(num):
#     return num * num

# output = list(map(lambda num: num * num, number))
# print(output)
# print(list(map(num_square, number)))
# for item in map(num_square, number):
#     print(item)

# filter
num_list = [1,4,3,6,8,9]


# def odd_num(num):
#     return num % 2 != 0


print(list(filter(lambda num: num % 2 != 0, num_list)))

