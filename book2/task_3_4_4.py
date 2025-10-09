my_list = ([1,2],[1,2],[3,4,5])


new_tuple = tuple()

for elm in my_list:
    if new_tuple.count(elm) < 1:
        new_tuple += (elm,)


print(new_tuple)