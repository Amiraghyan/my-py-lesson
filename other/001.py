def divide_from_file(filename):
    print(f"Փորձում ենք բացել {filename} ֆայլը...")
    file = None  # Սկզբնական արժեք՝ finally-ում հասանելի լինելու համար
    try:
        with open(filename, "r", encoding="utf-8") as file:
            number_str = file.readline()
            number = int(number_str)

    except FileNotFoundError:
        print("Սխալ։ Ֆայլը չի գտնվել։")
        return None
    except ValueError:
        print("Սխալ։ Ֆայլի պարունակությունը թիվ չէ։")
        return None

    else:  # Կատարվում է, եթե try-ը հաջողվեց (ոչ մի բացառություն)
        try:
            # Սա նոր, ներդրված try-except է՝ բաժանման համար
            result = 100 / number
            print("Բաժանումը հաջողվեց։")
            return result
        except ZeroDivisionError:
            print("Սխալ։ Ֆայլում գրված է զրո։")
            return None


# Օրինակի կանչ
divide_from_file("my_data.txt")
