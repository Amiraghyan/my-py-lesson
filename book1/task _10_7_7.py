age_list = []

for i in range(4):
    age = int(input("Գրիր Տարիք։ "))
    age_list.append(age)

print(f"Ամենաերիտասարդի տարիքն է {min(age_list)}")