str1 = "Jan = January; Feb = February; Mar = March"

list1 = str1.replace(" ","").split(";")

new_dict = {}

for elm in list1:
    index1 = elm.index("=")
    key = elm[:index1]
    value = elm[index1+1:]

    new_dict[key] = value


print(new_dict)