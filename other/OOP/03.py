class Bot:
    # Սա CLASS ATTRIBUTE է։ Այն ընդհանուր է բոլոր բոտերի համար։
    species = "Robot"
    bot_count = 0 # Սկզբում 0 բոտ ունենք
    bot_version = "v1.0"
    active_bots = []

    def __init__(self, name, ip, damage_power):
        # Սրանք INSTANCE ATTRIBUTES են։
        self.name = name
        self.ip = ip
        self.damage_power = damage_power
        self.health = 100
        
        # Ամեն անգամ, երբ նոր բոտ է "ծնվում" (__init__-ը կանչվում է),
        # մենք մեծացնում ենք ընդհանուր հաշվիչը։
        Bot.bot_count += 1
        print(f"New bot created: {self.name}. Total bots: {Bot.bot_count}")
        Bot.active_bots.append(self)
        print(f"Bots: {Bot.active_bots}")
        print("--------------")

    def attack(self, target_bot):
        print(f"{self.name} ({self.health}) attacks {target_bot.name} ({target_bot.health}).")
        target_bot.health -= self.damage_power
        print(f"{target_bot.name}'s health is now {target_bot.health}.")

        if target_bot.health <= 0:
            target_bot.die()

    def display_status(self):
        print("--- STATUS ---")
        print(f"Name: {self.name}")
        print(f"IP: {self.ip}")
        print(f"Health: {self.health}")
        print(f"Damage Power: {self.damage_power}")
        print("--------------")

    def die(self):
        Bot.active_bots.remove(self)
        print(f"{self.name} has been destroyed.")
        



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

bot_charlie.display_status()

bot_charlie.attack(bot_alpha)
bot_alpha.display_status()

print("\n--- Showing status for all active bots ---")
for bot in Bot.active_bots:
    bot.display_status() # Սա կաշխատի, քանի որ bot-ը օբյեկտ է, ոչ թե string