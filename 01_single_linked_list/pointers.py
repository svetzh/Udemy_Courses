
num1 = 11
num2 = num1
print(
    id(num1),
    id(num2)
)

num2 = 22

print(
    id(num1),
    id(num2)
)


###################################

dict1 = {
    'value': 11,
}

dict2 = dict1
print("Before update: ")
print(dict1)
print(dict2)

print("dict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))


dict2["value"] = 22
print("\nAfter update: ")
print("dict1 : ", dict1)
print("dict2 : ", dict2)

print(id(dict1))
print(id(dict2))

# what is happening to dict2 = 22 it's been GARBAGE COLLECTED

dict3 = dict2
print(dict3)
print(id(dict3))
