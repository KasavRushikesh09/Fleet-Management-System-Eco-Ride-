from ElectricCar import ElectricCar
from ElectricScooter import ElectricScooter

car = ElectricCar("C101", "Tesla Model 3", 90, 5)
scooter = ElectricScooter("S201", "Ola S1", 80, 90)

print("Car Trip Cost:", car.calculate_trip_cost(10))
print("Scooter Trip Cost:", scooter.calculate_trip_cost(10))
