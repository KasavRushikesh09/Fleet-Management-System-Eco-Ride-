
from ElectricScooter import ElectricScooter
from ElectricCar import ElectricCar

class EcoRideMain:
    @staticmethod
    def start():
        print("Welcome to Eco-Ride Urban Mobility System")

if __name__ == "__main__":
    EcoRideMain.start()
    e = ElectricScooter(123,"Ather",60,90)
    print(e.max_speed_limit)
    e = ElectricCar(190, "mercedes", 60, 5)
    print(e.seating_capacity)


