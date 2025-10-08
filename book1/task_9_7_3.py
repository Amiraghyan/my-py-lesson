# Գրել եռանիշ թիվ և ստուգել արդյոք Պոլինդրում է ։
# Արտածել True եթե այո , False եթե ոչ

number = int(input("Գրիր եռանիշ ամբողջ թիվ։ "))

first = number//100
last = number%10

if first == last:
    print(True)
else:
    print(False)
