def my_range(*arg):

    start = 0
    stop = int()
    step = 1


    if len(arg) == 1:
        stop = arg[0]
        while start < stop:
            yield start
            start += 1
    elif len(arg) == 2:
        start = arg[0]
        stop = arg[1]
        while start < stop:
            yield  start
            start += 1
    elif len(arg) == 3:
        start = arg[0]
        stop = arg[1]
        step = arg [2]
        if step > 0:
            while start < stop:
                yield start
                start += step 
        else:
            while start > stop:
                yield  start
                start += step 
    else: 
        raise SyntaxError
    

for el in my_range(10, 1, -1):
    print(el)

    


