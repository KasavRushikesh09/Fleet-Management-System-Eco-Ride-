
from ElectricScooter import ElectricScooter
from ElectricCar import ElectricCar

class EcoRideMain:
    def greet(self):
       print("Welcome to Eco-Ride urban Mobility system")
    def main(self):
        EcoRideMain.greet()
    ather = ElectricScooter(123,"Ather",80,100)
    ola = ElectricScooter(125,"ola",80,100)
    car = ElectricCar(126,"car",85,4)
    lst = [ather,car,ola]

    for i in lst:
        print(i.calculate_trip_cost(50))
if __name__ == "__main__":
    EcoRideMain.main()



