"""Do some things with dicts and list"""

my_dict = {
  0 : 0,
  1 : "vafler",
  "two" : 2,
  5 : 4
}

my_list = [0, 1, "boller", 4]

print("Dictionary Keys:")
for key in my_dict:
    print(key)


print("\nDictionary Values:")
for useless, value in my_dict.items():
    print(value)


print("\nDictionary keys/value:")
for key,value in my_dict.items():
    print(f"{key} {value}")


print("\nList values:")
for element in my_list:
    print(element)


print("\nList indices/value:")
for index,value in enumerate(my_list):
    print(f"{index} {value}")
