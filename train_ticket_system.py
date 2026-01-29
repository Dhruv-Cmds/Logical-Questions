# Author: Dhruv

# Create a class Train with:
# Attributes
# name
# seats
# fare
# Methods
# book_ticket(num_seats)
# '''get_status()
# get_fare()'''
# Rules
# If requested seats > available → print "Not enough seats"
# Otherwise:
# Reduce seats
# Print "Booking successful"
# Test with multiple bookings.

class Train :
    def __init__(self , name , seats , fare):
        self.name = name 
        self.seats = seats
        self.fare = fare

    def book_ticket(self , num_seats):

        if (self.seats < num_seats):
            print ("Not enough seats")

        elif (self.seats >= num_seats):
            self.seats = self.seats - num_seats
            print(f"Booking successful for {num_seats} seats")

    def get_status(self):
        print(f"Seats available: {self.seats}")

    def get_fare(self):
        print(f"Your Ticket Price is :{self.fare}")

t1 = Train("Rajdhani Express", 5, 1500)

t1.get_fare()
t1.get_status()

num_seats = int(input("Enter seats to book: "))
t1.book_ticket(num_seats)

t1.get_status()