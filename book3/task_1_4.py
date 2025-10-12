class Light():
    def __init__(self) -> None:
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def status(self):
        return self.is_on
    
bulb = Light()

print(bulb.status())

bulb.turn_on()
print(bulb.status())

bulb.turn_off()
print(bulb.status())
