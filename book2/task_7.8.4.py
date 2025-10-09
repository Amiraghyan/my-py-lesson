def calc(str1: str):
    str_list = str1.split()

    a = int(str_list[0])
    b = int(str_list[2])

    match str_list[1]:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
        case "**":
            return a ** b
        case "//":
            return a // b
        
print(calc("3 * 3"))

