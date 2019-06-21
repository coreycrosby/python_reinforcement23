class Location:
    
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

class Trip:

    def __init__(self):
        self.destinations = []

    def add_location(self, location):
        self.destinations.append(location)

    def add_all(self, *locations):
        for location in locations:
                self.add_location(location)

    def itinerary(self):
        print("Begin trip.")
        for num in range(0, len(self.destinations)-1):
            print(f"Travelled from {self.destinations[num]} to {self.destinations[num+1]}")
        print("Ended trip.")

tor = Location("Toronto")
ott = Location("Ottawa")
mon = Location("Montreal")
qc = Location("Quebec City")
hal = Location("Halifax")
sj = Location("St. John's")


canada_trip = Trip()
canada_trip.add_all(tor, ott, mon, qc, hal,sj)
canada_trip.itinerary()
