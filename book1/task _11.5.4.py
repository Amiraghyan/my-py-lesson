num = int(input("Գրիր ամբողջ թիվ։ "))

i = 0
sum_num = 0

while i <= num:

    if i%2 != 0:
        sum_num += i
    i += 1

print(f"0-ից {num} կենտ թվերիգումարը կլինի {sum_num}")