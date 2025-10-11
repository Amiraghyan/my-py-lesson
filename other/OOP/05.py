class Bot:
    species = "Robot"
    bot_count = 0
    bot_version = "v1.0"
    active_bots = []

    def __init__(self, name, ip, damage_power):
        self.name = name
        self._ip = ip
        self._damage_power = damage_power
        self._health = 100

        Bot.bot_count += 1
        print(f"New bot created: {self.name}. Total bots: {Bot.bot_count}")
        Bot.active_bots.append(self)
        print(f"Bots: {Bot.active_bots}")
        print("--------------")

    def __str__(self):
        return f"<Bot: {self.name}, HP: {self._health}>"

    def __repr__(self):
        return f"Bot('{self.name}', '{self._ip}', {self._damage_power})"

    def attack(self, target_bot):
        print(f"{self.name} ({self.get_health()}) attacks {target_bot.name} ({target_bot.get_health()}).")
        target_bot.take_damage(self._damage_power)

    def take_damage(self, amount):
        if amount <= 0:
            raise ValueError
        else:
            self._health -= amount
        if self._health <= 0:
            self.die()

    def display_status(self):
        print("--- STATUS ---")
        print(f"Name: {self.name}")
        print(f"IP: {self._ip}")
        print(f"Health: {self._health}")
        print(f"Damage Power: {self._damage_power}")
        print("--------------")

    def die(self):
        Bot.active_bots.remove(self)
        print(f"{self.name} has been destroyed.")

    def get_health(self):
        return self._health

    def get_damage_power(self):
        return self._damage_power


bot_alpha = Bot("Alpha", "192.168.1.10", 10)
bot_bravo = Bot("Bravo", "192.168.1.11", 15)
bot_charlie = Bot("Charlie", "8.8.8.8", 20)

bot_alpha.attack(bot_bravo)
bot_bravo.display_status()

bot_bravo.attack(bot_charlie)
bot_bravo.attack(bot_charlie)
bot_bravo.attack(bot_charlie)
bot_bravo.attack(bot_charlie)
bot_bravo.attack(bot_charlie)
bot_bravo.attack(bot_charlie)
bot_bravo.attack(bot_charlie)


print("\n--- Showing status for all active bots ---")
for bot in Bot.active_bots:
    bot.display_status()

print(bot_alpha)
print(bot_charlie.get_health())

bot_alpha.take_damage(-50)