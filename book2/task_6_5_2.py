my_dict = {
    "The": [0,1],
    "best":[2,3,4]
            }


new_list = []

for key,val in my_dict.items():
    temp_list = []
    
    temp_list.append(key)
    temp_list.extend(val)
    
    new_list.append(temp_list)

print(new_list)