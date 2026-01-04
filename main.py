
from ElectricScooter import ElectricScooter
from ElectricCar import ElectricCar

class EcoRideMain:
    def greet():
       print("Welcome to Eco-Ride urban Mobility system")

if __name__ == "__main__":
    EcoRideMain.greet()
    e = EcoRideMain(123,"ather",90,100)
    print(e.calculate_trip_cost(20))
    c = ElectricCar(1,"bmw",90,4)
    print(c.calculate_trip_cost(30))


