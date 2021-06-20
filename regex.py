import re

text = "You can reach me at 123-123-4567"
pattern = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
result = re.search(pattern, text)
print(result) # this will return match object with match
                # information and index location of match
print(result.span()) # get start and end index in tuple
print(result.start()) # get start index of match
print(result.group()) # get the pattern match


text = "Call me at 123-123-4567 or 333-333-3333"
pattern = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# it will give list of all matches
results = re.findall(pattern, text)
print(results)

# to get object with more details for all match
for result in re.finditer(pattern, text):
    print(result)  # print(result.span())

# Character identifier
# so far we have seen '\d' for digit
# '\w' is use for alphanumeric -> C_at-1 \w\w\w\w-\w
# '\s' for white space -> c a t c\sa\st
# '\D' for non digit -> ABS \D\D\D
# '\W' for non-alphanumeric -> *-+=0


# Quantifiers
# + (Occurs one or more time)
# {3} Occurs exactly 3 times
# * (Occurs zero or more times)
# ? (Once or more)

text = "You can reach me at 123-123-4567"
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
result = re.search(pattern, text)
print(result) # this will return match object with match
                # information and index location of match
print(result.group()) # get the pattern match

# check for individual group
pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
result = re.search(pattern, text)
print(result.group(1))
print(result.group(3))


# or (|) operator
text = "I have Tesla car"
pattern = re.compile(r'Tesla')
# pattern = re.compile(r'Infiniti')
# pattern = re.compile(r'Tesla | Infiniti')
model_match = re.search(pattern, text)
print(model_match)


# . (dot) operator
text = "It is best to take rest during fest"
pattern = re.compile(r'.est')
result = re.findall(pattern, text)
print(result)

# ^ (start with)
text = "1/1/2021"
# text = "date 1/1/2021"
result = re.findall("^\d", text)
print(result)

# $ (end with)
text = "Today's date 1/1/2021"
# text = "Today's date 1/1/2021 monday"
result = re.findall('\d$', text)
print(result)

# [] to exclude
# you want to remove all punctuation from text
text = "This is Sanjeev! the founder of interviewbox.tech?"
pattern = re.compile(r'[^!?]+')
result = re.findall(pattern, text)
print(result)
# print(''.join(result))