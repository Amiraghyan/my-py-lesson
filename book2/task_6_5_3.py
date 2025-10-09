dict1 = {
    "a": 1,
    "b": 2,
    "c": 3
            }
dict2 = {
    "d": 4,
    "e": 5,
            }

new_dict = {}

for key,val in dict1.items():
    new_dict[key] = val

for key,val in dict2.items():
    new_dict[key] = val

print(new_dict)