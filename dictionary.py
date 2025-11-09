person = {"name": "Alice", "age": 25}

# keys()
# print(person.keys())     # dict_keys(['name', 'age'])

objKeys = person.keys()
print(objKeys)




# values()
print(person.values())   # dict_values(['Alice', 25])

# items()
print(person.items())    # dict_items([('name', 'Alice'), ('age', 25)])

# get()
print(person.get('age', 0))     # 25
print(person.get('city', 'NA')) # 'NA' (avoids KeyError)

# update()
person.update({"city": "NY"})
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'NY'}