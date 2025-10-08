# Արդյոք թիվի վերջին նիշը բաժանվում է 3-ի

number = int(input("Գրիր ամբեղջ թիվ։ "))

n = number % 10

if number < 10:
    n = number
else:
    n = number % 10

if n%3 == 0:
    print(f"{number}-ի վերջին նիշը բաժանվում է 3-ի")
else: 
    print(f"{number}-ի վերջին նիշը ՉԻ բաժանվում է 3-ի")

