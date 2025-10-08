# ստանալ շաբաթվա թիվը արտածել օրը

num = int(input("Գրիր շաբաթվա օրը թվով։ "))

match num:
    case 1:
        print("Երկուշաբթի")
    case 2:
        print("Երեքշաբթի")
    case 3:
        print("Չորեքշաբթի")
    case 4:
        print("Հինգշաբթի")
    case 5:
        print("Ուրբաթ")
    case 6:
        print("Շաբաթ")
    case 7:
        print("Կիրակի")
    case _:
        print("Նման օր գոյություն չունի")
    