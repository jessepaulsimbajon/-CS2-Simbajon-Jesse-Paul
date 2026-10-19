# Travel Fare Calculator
FARE_RATE = 14

name = input("Enter passenger name: ")
distance = float(input("Enter distance (km): "))
passengers = int(input("Enter number of passengers: "))

total_fare = distance * FARE_RATE * passengers

# Validating Passenger name
if name.strip() == "":
    print("Name must not be empty please try again")
    
else:
    print("\nPassenger:", name)    
    print("Total Fare: PHP", round(total_fare, 2))
    
# Validating Distance
if distance == 0:
    print("Distance must not be 0 try again")
    
else:
    print("")    
     
    
# Validating Passengers 
if passengers <=0:
    print("Passengers must not be less than or equal to 0")
    
else:
    print("")    
       
