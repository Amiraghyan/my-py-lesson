class Weapon():
    def __init__(self, name: str) -> None:
        self.name = name

    def attack(self):
        print(f"Attaced with {self.name}")

class Gun(Weapon):
    def __init__(self, name: str, bullets: int):
        super().__init__(name)
        self.bullets = bullets

    def attack(self):
        if self.bullets > 0:
            self.bullets -= 1
            print(f"Total bullets afther attack {self.bullets}")
        else:
            print(f"Out of bullets! Reload needed for {self.name}")

class Sword(Weapon):
    def __init__(self, name: str):
        super().__init__(name)

    def attack(self):
        print(f"Swinging the sword {self.name}")

class Soldier:
    def __init__(self, name, weapon) -> None:
        self.name = name
        self.weapon = weapon

    def use_weapon(self):
        self.weapon.attack()


gun = Gun("AK-47", 3)
sword = Sword("Katana")

soldier_with_gun = Soldier("John", gun)
soldier_with_sward = Soldier("Alice", sword)

soldier_with_gun.use_weapon()
soldier_with_gun.use_weapon()
soldier_with_gun.use_weapon()
soldier_with_gun.use_weapon()

soldier_with_sward.use_weapon()
