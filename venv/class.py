# Class examples (classes)

class UberEats:
    def request_uber(self):
        return "Uber Requested"

    def __init__(self):
        self.fare = 0
        self.distance = 0


    def star_trip(self):
        return "Trip started"


toyota = UberEats()
print(toyota.request_uber())
print(toyota.fare)
print(toyota.distance)

class MainUber(UberEats):
    def __init__(self):



mainuber = mainUber()
mainuber.request_uber()