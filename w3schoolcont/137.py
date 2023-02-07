car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items() # тк указатель все в пайтоне указывает на итемы в дикт

print(x) #before the change

car["color"] = "red"

print(x) #after the change