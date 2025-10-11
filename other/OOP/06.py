class Bot:
    species = "Robot"
    bot_count = 0
    bot_version = "v1.0"
    active_bots = []

    def __init__(self, name, ip):
        self.name = name
        self._ip = ip
        self._health = 100

        Bot.bot_count += 1
        print(f"New bot created: {self.name}. Total bots: {Bot.bot_count}")
        Bot.active_bots.append(self)
        print("--------------")

    def __str__(self):
        return f"<Bot: {self.name}, HP: {self._health}>"

    def __repr__(self):
        return f"Bot('{self.name}', '{self._ip}')"


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
        print("--------------")

    def die(self):
        Bot.active_bots.remove(self)
        print(f"{self.name} has been destroyed.")

    def get_health(self):
        return self._health
    
    def receive_healing(self, amount):
        if amount <= 0:
            raise ValueError
        
        self._health = min(100, self._health + amount)


class AttackerBot(Bot):
    def __init__(self, name, ip, damage_power):
        super().__init__(name, ip)
        self._damage_power = damage_power
    
    def __repr__(self):
        return f"AttackerBot('{self.name}', '{self._ip}', dmg={self._damage_power})"

    def attack(self, target_bot):
        print(f"{self.name} ({self.get_health()}) attacks {target_bot.name} ({target_bot.get_health()}).")
        target_bot.take_damage(self._damage_power)

    def display_status(self):
        print("--- STATUS ---")
        print(f"Name: {self.name}")
        print(f"IP: {self._ip}")
        print(f"Health: {self._health}")
        # Ավելացված մասը
        print(f"Damage Power: {self._damage_power}")
        print("--------------")


class MedicBot(Bot):
    def __init__(self, name, ip, healing_power):
        super().__init__(name, ip)
        self._healing_power = healing_power

    def __repr__(self):
        return f"MedicBot('{self.name}', '{self._ip}', heal={self._healing_power})"
    

    def heal(self, target_bot):
        print(f"{self.name} ({self.get_health()}) heal {target_bot.name} ({target_bot.get_health()}).")
        target_bot.receive_healing(self._healing_power)

    # MedicBot-ի մեջ
    def display_status(self):
        print("--- STATUS ---")
        print(f"Name: {self.name}")
        print(f"IP: {self._ip}")
        print(f"Health: {self._health}")
        # Ավելացված մասը
        print(f"Healing Power: {self._healing_power}")
        print("--------------")




bot_terminator = AttackerBot("Terminator", "192.168.1.10", 10)
bot_robocop = AttackerBot("RoboCop", "192.168.1.11", 15)
bot_baymax = MedicBot("Baymax", "8.8.8.8", 20)


bot_terminator.attack(bot_robocop)
bot_robocop.display_status()

bot_terminator.attack(bot_robocop)
bot_robocop.display_status()

bot_terminator.attack(bot_robocop)
bot_robocop.display_status()

bot_terminator.attack(bot_robocop)
bot_robocop.display_status()

bot_terminator.attack(bot_robocop)
bot_robocop.display_status()



bot_baymax.heal(bot_robocop)
bot_robocop.display_status()

bot_baymax.heal(bot_robocop)
bot_robocop.display_status()

bot_baymax.heal(bot_robocop)
bot_robocop.display_status()

bot_baymax.heal(bot_robocop)
bot_robocop.display_status()

bot_baymax.heal(bot_robocop)
bot_robocop.display_status()
