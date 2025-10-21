class Light:
    """Represents a light bulb that has an on/off state."""

    def __init__(self) -> None:
        """Initializes a new Light object, which is off by default."""
        self.is_on = False

    def turn_on(self) -> None:
        """Turns the light on."""
        self.is_on = True
        print("The light is now ON.")

    def turn_off(self) -> None:
        """Turns the light off."""
        self.is_on = False
        print("The light is now OFF.")

    def get_status(self) -> bool:
        """Returns the current state of the light (True if on, False if off)."""
        return self.is_on


# Create an instance (object) of the Light class.
light_bulb = Light()

# Check the initial status of the light bulb.
initial_status = light_bulb.get_status()
print(f"Initial status: {initial_status}")

# Turn the light on and check its status again.
light_bulb.turn_on()
current_status = light_bulb.get_status()
print(f"Current status: {current_status}")

# Turn the light off and check the final status.
light_bulb.turn_off()
final_status = light_bulb.get_status()
print(f"Final status: {final_status}")
