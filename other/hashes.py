# Հեշավորվող տիպերը թույլատրվում են
my_set_valid = {1, "hello", (10, 20), True, None}  # tuple-ը անփոփոխ է, ուստի հեշավորվող
print(f"Վավեր set: {my_set_valid}")

# Ոչ հեշավորվող տիպերը կարգելվեն
try:
    my_set_invalid = {1, "hello", [10, 20]}  # list-ը փոփոխվող է, ուստի ոչ հեշավորվող
except TypeError as e:
    print(f"\nՍխալի առաջացում set-ի դեպքում։")
    print(e)
