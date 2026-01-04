
from ElectricScooter import ElectricScooter
from ElectricCar import ElectricCar
from fleet_manager import Fleetmanager

class EcoRideMain:
    def greet(self):
       print("Welcome to Eco-Ride urban Mobility system")
    def main(self):
        EcoRideMain.greet()
        ather = ElectricScooter(123,"Ather",80,100)
        ola = ElectricScooter(125,"ola",80,100)
        car = ElectricCar(126,"car",85,4)
        fm = Fleetmanager()
        fm.add_hub()
        fm.add_vehicle_to_hub()
        fm.add_vehicle_to_hub()
        fm.add_vehicle_to_hub()
if __name__ == "__main__":
    EcoRideMain.main()



