# Քայլ 1: Ստեղծում ենք օբյեկտ (instance)
my_number = 100
print(f"Օբյեկտ: {my_number}")
print(f"Օբյեկտի տիպը՝ {type(my_number)}")

print("-" * 20)

# Քայլ 2: Ուսումնասիրում ենք հենց կլասը
my_class = int
print(f"Կլաս: {my_class}")
print(f"Կլասի տիպը՝ {type(my_class)}")  # Ահա և մեր պատասխանը

print("-" * 20)


# Քայլ 3: Ստուգենք մեր սեփական կլասի հետ
class MyOwnClass:
    pass


print(f"Մեր սեփական կլասը՝ {MyOwnClass}")
print(f"Մեր կլասի տիպը՝ {type(MyOwnClass)}")  # Նույնպես <class 'type'>

print("-" * 20)

# Քայլ 4: Իսկ ի՞նչ է հենց type-ի տիպը (մտագրոհ)
print(f"Իսկ ի՞նչ է հենց type-ի տիպը: {type(type)}")  # type-ը իր սեփական տիպն է
