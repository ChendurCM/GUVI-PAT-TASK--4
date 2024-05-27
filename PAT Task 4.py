import math

class Circle:
    def __init__(self, radii):
        if not all(isinstance(radius, (int, float)) for radius in radii):
            raise ValueError("All elements in the list must be numbers.")
        self.radii = radii

    def area(self, radius):
        return math.pi * radius * radius

    def circumference(self, radius):
        return 2 * math.pi * radius

    def display_properties(self):
        for radius in self.radii:
            print(f"Radius: {radius}")
            print(f"Area: {self.area(radius):.2f}")
            print(f"Circumference: {self.circumference(radius):.2f}")
            print("-" * 30)

# Usage example:
radii_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radii_list)
circle.display_properties()


class Circle:
    # Class private variable for pi
    __pi = 3.141

    def __init__(self, radii):
        # Instance variable to store the list of radii
        self.radii = radii
        # Validate that all elements in the list are numbers
        if not all(isinstance(radius, (int, float)) for radius in self.radii):
            raise ValueError("All elements in the list must be numbers.")

    def area(self, radius):
        # Use the class private variable __pi to calculate the area
        return Circle.__pi * radius * radius

    def circumference(self, radius):
        # Use the class private variable __pi to calculate the circumference
        return 2 * Circle.__pi * radius

    def display_properties(self):
        for radius in self.radii:
            print(f"Radius: {radius}")
            print(f"Area: {self.area(radius):.2f}")
            print(f"Circumference: {self.circumference(radius):.2f}")
            print("-" * 30)

# Usage example:
radii_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radii_list)
circle.display_properties()


class Circle:
    # Class private variable for pi
    __pi = 3.141

    def __init__(self, radii):
        # Instance variable to store the list of radii
        self.radii = radii
        # Validate that all elements in the list are numbers
        if not all(isinstance(radius, (int, float)) for radius in self.radii):
            raise ValueError("All elements in the list must be numbers.")

    @classmethod
    def area(cls, radius):
        # Use the class private variable __pi to calculate the area
        return cls.__pi * radius * radius

    @classmethod
    def perimeter(cls, radius):
        # Use the class private variable __pi to calculate the perimeter (circumference)
        return 2 * cls.__pi * radius

    def display_properties(self):
        for radius in self.radii:
            print(f"Radius: {radius}")
            print(f"Area: {self.area(radius):.2f}")
            print(f"Perimeter: {self.perimeter(radius):.2f}")
            print("-" * 30)

# Usage example:
radii_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radii_list)
circle.display_properties()


class TV:
    def __init__(self, brand, price, inches):
        self.brand = brand
        self.price = price
        self.inches = inches
        self.is_on = False  # TV is off by default
        self.reset()  # Initialize the TV to default settings

    def power(self):
        self.is_on = not self.is_on
        status = "on" if self.is_on else "off"
        print(f"The TV is now {status}.")

    def set_channel(self, channel):
        if self.is_on:
            if 1 <= channel <= 50:
                self.channel = channel
                print(f"Channel set to {self.channel}.")
            else:
                print("Invalid channel. Please select a channel between 1 and 50.")
        else:
            print("TV is off. Please turn it on first.")

    def set_volume(self, volume):
        if self.is_on:
            if 0 <= volume <= 100:
                self.volume = volume
                print(f"Volume set to {self.volume}.")
            else:
                print("Volume must be between 0 and 100.")
        else:
            print("TV is off. Please turn it on first.")

    def increase_volume(self):
        if self.is_on:
            if self.volume < 100:
                self.volume += 1
                print(f"Volume increased to {self.volume}.")
            else:
                print("Volume is already at maximum (100).")
        else:
            print("TV is off. Please turn it on first.")

    def decrease_volume(self):
        if self.is_on:
            if self.volume > 0:
                self.volume -= 1
                print(f"Volume decreased to {self.volume}.")
            else:
                print("Volume is already at minimum (0).")
        else:
            print("TV is off. Please turn it on first.")

    def reset(self):
        """Reset TV to default channel and volume."""
        self.channel = 1
        self.volume = 50
        print("TV has been reset to channel 1 and volume 50.")

    def display_status(self):
        """Return a string with the current status of the TV."""
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"

# Usage example:
tv = TV("Samsung", 500, 55)
print(tv.display_status())   # Display initial status
tv.power()                   # Turn the TV on
tv.set_channel(5)            # Change channel to a valid channel
tv.set_channel(60)           # Attempt to change to an invalid channel
tv.set_volume(30)            # Change volume
tv.increase_volume()         # Increase volume
tv.decrease_volume()         # Decrease volume
tv.reset()                   # Reset TV to default settings
print(tv.display_status())   # Display updated status


class TV:
    def __init__(self, Panasonic, price, inches):
        self.brand = Panasonic
        self.price = price
        self.inches = inches
        self.is_on = False  # TV is off by default
        self.reset()  # Initialize the TV to default settings

    def power(self):
        self.is_on = not self.is_on
        status = "on" if self.is_on else "off"
        print(f"The TV is now {status}.")

    def set_channel(self, channel):
        if self.is_on:
            if 1 <= channel <= 50:
                self.channel = channel
                print(f"Channel set to {self.channel}.")
            else:
                print("Invalid channel. Please select a channel between 1 and 50.")
        else:
            print("TV is off. Please turn it on first.")

    def set_volume(self, volume):
        if self.is_on:
            if 0 <= volume <= 100:
                self.volume = volume
                print(f"Volume set to {self.volume}.")
            else:
                print("Volume must be between 0 and 100.")
        else:
            print("TV is off. Please turn it on first.")

    def increase_volume(self):
        if self.is_on:
            if self.volume < 100:
                self.volume += 1
                print(f"Volume increased to {self.volume}.")
            else:
                print("Volume is already at maximum (100).")
        else:
            print("TV is off. Please turn it on first.")

    def decrease_volume(self):
        if self.is_on:
            if self.volume > 0:
                self.volume -= 1
                print(f"Volume decreased to {self.volume}.")
            else:
                print("Volume is already at minimum (0).")
        else:
            print("TV is off. Please turn it on first.")

    def reset(self):
        """Reset TV to default channel and volume."""
        self.channel = 1
        self.volume = 50
        print("TV has been reset to channel 8 and volume 75.")

    def display_status(self):
        """Return a string with the current status of the TV."""
        return f"{self.panasonic} at channel {self.channel}, volume {self.volume}"


class LED(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def viewing_angle(self):
        return "Wide viewing angle"

    def backlight(self):
        return "LED backlight"

    def display_details(self):
        details = (f"Brand: {self.brand}\n"
                   f"Size: {self.inches} inches\n"
                   f"Price: ${self.price}\n"
                   f"Screen Thickness: {self.screen_thickness} mm\n"
                   f"Energy Usage: {self.energy_usage} watts\n"
                   f"Lifespan: {self.lifespan} hours\n"
                   f"Refresh Rate: {self.refresh_rate} Hz\n"
                   f"Viewing Angle: {self.viewing_angle()}\n"
                   f"Backlight: {self.backlight()}\n"
                   f"Channel: {self.channel}\n"
                   f"Volume: {self.volume}")
        print(details)
        return details


class Plasma(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def viewing_angle(self):
        return "Excellent viewing angle"

    def backlight(self):
        return "No backlight (self-illuminating)"

    def display_details(self):
        details = (f"Brand: {self.brand}\n"
                   f"Size: {self.inches} inches\n"
                   f"Price: ${self.price}\n"
                   f"Screen Thickness: {self.screen_thickness} mm\n"
                   f"Energy Usage: {self.energy_usage} watts\n"
                   f"Lifespan: {self.lifespan} hours\n"
                   f"Refresh Rate: {self.refresh_rate} Hz\n"
                   f"Viewing Angle: {self.viewing_angle()}\n"
                   f"Backlight: {self.backlight()}\n"
                   f"Channel: {self.channel}\n"
                   f"Volume: {self.volume}")
        print(details)
        return details

# Usage example:
led_tv = LED("Samsung", 800, 55, 25, 120, 50000, 60)
plasma_tv = Plasma("Panasonic", 600, 50, 30, 200, 100000, 600)

# Display details for each TV
print("LED TV Details:")
led_tv.display_details()

print("\nPlasma TV Details:")
plasma_tv.display_details()
