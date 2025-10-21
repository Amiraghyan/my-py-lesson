class Weapon:
    """A base class for all weapon types."""

    def __init__(self, name: str) -> None:
        """Initializes the weapon with a name."""
        self.name = name

    def attack(self):
        """A generic attack action. Subclasses should override this."""
        print(f"Attacked with {self.name}.")


class Gun(Weapon):
    """A type of Weapon that uses bullets."""

    def __init__(self, name: str, bullets: int):
        """Initializes the gun with a name and a number of bullets."""
        super().__init__(name)
        self.bullets = bullets

    def attack(self):
        """
        Fires the gun if there are bullets, otherwise shows an empty message.
        """
        if self.bullets > 0:
            print(f"Firing {self.name}...")
            self.bullets -= 1
            print(f"Bullets remaining: {self.bullets}")
        else:
            print(f"Out of bullets! Reload needed for {self.name}.")


class Sword(Weapon):
    """A type of Weapon that is used for swinging."""

    def __init__(self, name: str):
        """Initializes the sword with a name."""
        super().__init__(name)

    def attack(self):
        """Performs a swinging attack with the sword."""
        print(f"Swinging the sword {self.name}!")


class Soldier:
    """Represents a soldier who has a weapon."""

    def __init__(self, name: str, weapon: Weapon) -> None:
        """Initializes the soldier with a name and a weapon object."""
        self.name = name
        self.weapon = weapon

    def use_weapon(self):
        """Makes the soldier use their currently equipped weapon."""
        self.weapon.attack()


# 1. Create the weapons
gun = Gun("AK-47", 3)
sword = Sword("Katana")

# 2. Create the soldiers and give them their weapons
soldier_with_gun = Soldier("John", gun)
soldier_with_sword = Soldier("Alice", sword)

# 3. Demonstrate the soldiers using their weapons
print("--- John's turn (with a gun) ---")
soldier_with_gun.use_weapon()
soldier_with_gun.use_weapon()
soldier_with_gun.use_weapon()
soldier_with_gun.use_weapon()

print("\n--- Alice's turn (with a sword) ---")
soldier_with_sword.use_weapon()
