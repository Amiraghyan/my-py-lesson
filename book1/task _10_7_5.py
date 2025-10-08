v = int(input("Գրեք ձեր օգտագործածի չափը: "))

if v <= 100:
    price = 0
elif v <= 200:
    price = 200 * (v - 100)
else:
    price = 220*(v - 200) + 200 * 100

print(price)