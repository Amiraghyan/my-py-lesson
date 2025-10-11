class Bot:
    def __init__(self, name, ip, damage_power):
        self.name = name
        self.ip = ip
        self.damage_power = damage_power
        self.health = 100

    def attack(self, target_bot):
        print(f"{self.name} ({self.health}) attacks {target_bot.name} ({target_bot.health}).")
        target_bot.health -= self.damage_power
        print(f"{target_bot.name}'s health is now {target_bot.health}.")

    def display_status(self):
        print("--- STATUS ---")
        print(f"Name: {self.name}")
        print(f"IP: {self.ip}")
        print(f"Health: {self.health}")
        print(f"Damage Power: {self.damage_power}")
        print("--------------")


bot_alpha = Bot("Alpha", "192.168.1.10", 10)
bot_bravo = Bot("Bravo", "192.168.1.11", 15)
bot_charlie = Bot("Charlie", "8.8.8.8", 20)

bot_alpha.attack(bot_bravo)
bot_bravo.display_status()

bot_bravo.attack(bot_charlie)
bot_charlie.display_status()

bot_charlie.attack(bot_alpha)
bot_alpha.display_status()