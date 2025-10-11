bot_alpha = {
    "name": "Alpha",
    "ip": "192.168.1.10",
    "health": 100,
    "damage_power": 10
}

bot_bravo = {
    "name": "Bravo",
    "ip": "192.168.1.11",
    "health": 90,
    "damage_power": 15
}


bot_charlie = {
    "name": "Charlie",
    "ip": "8.8.8.8",
    "health": 76,
    "damage_power": 20
}

def attack(attacker_bot, target_bot):
    temp_health = target_bot["health"]
    target_bot["health"] -= attacker_bot["damage_power"]

    print(f"{attacker_bot["name"]} ({attacker_bot["health"]}) attacks {target_bot["name"]} ({temp_health}). {target_bot["name"]}'s health is now {target_bot["health"]}.")

def display_status(bot: dict):
    for key, val in bot.items():
        print(f"{key} - {val}")

attack(bot_bravo,bot_alpha)
attack(bot_alpha,bot_charlie)
attack(bot_charlie,bot_bravo)

display_status(bot_alpha)
display_status(bot_bravo)
display_status(bot_charlie)