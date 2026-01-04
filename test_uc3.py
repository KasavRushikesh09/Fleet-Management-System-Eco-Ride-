from ElectricCar import ElectricCar
from ElectricScooter import ElectricScooter

car = ElectricCar("C101","Tesla Model 3",90,5)
scooter = ElectricScooter("S201","Ola s1",80,90)

print("Car:",car.vehicle_id,car.model,car.battery_percentage,car.seating_capacity)
print("Scooter:",scooter.vehicle_id,scooter.model,scooter.battery_percentage,scooter.max_speed_limit)
