# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 15)
# ]


# # def sort_item(item):
# #     return item[1]


# items.sort(key=lambda item: item[1])
# print(items)


try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("No exception were thrown")
print("execution continue")
