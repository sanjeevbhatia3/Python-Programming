# def multiple_of_ten():
#     my_list = [1, 2, 3, 4, 5]
#     output = []
#     for num in my_list:
#         output.append(num * 10)
#     return output
#
#
# products = multiple_of_ten()
# print(products)


def multiple_of_ten():
    my_list = [1, 2, 3, 4, 5]
    for item in my_list:
        yield item*10


# print(list(multiple_of_ten()))
print(multiple_of_ten())
iterator = multiple_of_ten()
print(next(iterator))
print(next(iterator))
print(next(iterator))

# for item in iterator:
#     print(item)
