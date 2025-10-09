def revers_int(number: int):

    reversed_number = int()

    while number > 0:
        temp_num = number%10
        reversed_number = reversed_number*10 + temp_num
        number //= 10

    return reversed_number

print(revers_int(15478965))