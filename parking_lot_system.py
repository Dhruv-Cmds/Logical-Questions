# Author: Dhruv

# total_capacity = 10
# Instance attributes
# lot_name
# available_slots
# Methods
# 1. park_car(cars)
# If cars > available_slots → print "Parking Full"
# Else:
# reduce available_slots
# reduce class variable total_capacity
# print "Car parked successfully"
# 2. leave_car(cars)
# Increase available_slots
# Increase class variable total_capacity
# Do NOT exceed original capacity (10)
# 3. get_status()
# Print:
# lot name
# available slots
# total capacity left (class variable)
# 4. Static method
# def welcome():
#     print("Welcome to Smart Parking System")

class ParkingLot:

    total_capacity = 10   # class variable (global)

    def __init__(self, lot_name, slots):
        self.lot_name = lot_name
        self.available_slots = slots

    @staticmethod
    def welcome():
        print("Welcome to Smart Parking System")

    def park_car(self, cars):
        if cars > self.available_slots:
            print("Parking Full in lot", self.lot_name)
        else:
            self.available_slots -= cars
            ParkingLot.total_capacity -= cars
            print(f"{cars} car(s) parked in lot {self.lot_name}")

    def leave_car(self, cars):
        self.available_slots += cars
        ParkingLot.total_capacity += cars

        # limit total capacity
        if ParkingLot.total_capacity > 10:
            ParkingLot.total_capacity = 10

        print(f"{cars} car(s) left from lot {self.lot_name}")

    def get_status(self):
        print("Lot:", self.lot_name)
        print("Available slots:", self.available_slots)
        print("Total system capacity:", ParkingLot.total_capacity)
        print("---------------------------")

p1 = ParkingLot("A", 5)
p2 = ParkingLot("B", 5)

ParkingLot.welcome()

p1.park_car(3)
p2.park_car(4)

p1.get_status()
p2.get_status()

p1.leave_car(2)
p1.get_status()


#  not done by me
