num = int(input("Գրիր ամբողջ թիվ։ "))

reversed_number = 0

while num > 0:
    temp_num = num%10
    reversed_number = reversed_number*10 + temp_num
    num //= 10

print(reversed_number)