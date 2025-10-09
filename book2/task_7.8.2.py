
def my_bin(number):
    binary_str = ""

    if number == 0:
        binary_str = "0"
    else: 
        while number:
            n = number % 2
            binary_str = str(n) + binary_str
            number //= 2
    return int(binary_str)

num = my_bin(8)

print(num)