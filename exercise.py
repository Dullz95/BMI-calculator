# bus

class Bus_descr:

    def __init__(self, seats, color, driver):
        self.seats = 56
        self.color = "The bus is red"
        self.driver = "The bus driver is Abdullah"

    def change_color(self, color):
        self.color = color



bus = Bus_descr()

print(bus.seats)
print(bus.color)
print(bus.driver)
