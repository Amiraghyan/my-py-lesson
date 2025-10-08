# 0-15 միջակայքի թիվը արտածել երկուական հաամակարգով

number = int(input("Գրիր ամբողջ դրական թիվ։ "))

binary_str = ""

if number == 0:
    binary_str = "0"
else: 
    while number:
        n = number % 2
        binary_str = str(n) + binary_str
        number //= 2

print(binary_str)