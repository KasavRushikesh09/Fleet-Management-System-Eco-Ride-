class Vehicle:
     def __init__(self, vehicle_id, model, battery_percentage):
         self.vehicle_id = vehicle_id
         self.model = model
         self.battery_percentage = battery_percentage

if __name__ == "__main__":
         vehicle = Vehicle("v101","Tesla Model 3",85)

         print("Vehicle ID:",vehicle.vehicle_id)
         print("Model:",vehicle.model)
         print("Battery Percentage:",vehicle.battery_percentage)