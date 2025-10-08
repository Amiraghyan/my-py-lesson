# Ֆակտորիալ

num = int(input("Գրիր Ամբողջ թիվ։ "))

factoria_num = 1

while num >= 1:
    factoria_num *= num
    num -= 1
    
print(factoria_num)