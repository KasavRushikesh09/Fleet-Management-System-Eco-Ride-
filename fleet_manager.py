from ElectricScooter import ElectricScooter
from ElectricCar import ElectricCar

class Fleetmanager:
    def __init__(self):
        self.hubs={}
    def add_hub(self):
        hub_name = input("Please Enter the hub name: ")
        if hub_name in self.hubs:
            print("Hub Already Exists")
        else:
            self.hubs[hub_name] = []
            print(f"{hub_name} added Successfully")
    def add_vehicle_to_hub(self):
        hub_name = input("Enter the hub name to add vehicle to Hub:\n")
        option = input("Select the vehicle you want to add :\nEnter 1 for Electric Scooter \nEnter 2 for ELectric Car\n")
        print("Enter 1 for Electric Scooter \n  Enter 2 for Electric Car")
        vehicle = None
        if hub_name not in self.hubs:
            print(f"Hub {hub_name} does not exist")
        else:
            if option == '1':
                id = input("Enter the id of the vehicle:\n")
                model = input("Enter the model of the vehicle:\n")
                battery_percentage = int(input("Enter the battery percenatge of the vehicle:\n"))
                max_speed = int(input("Enter the maximum speed of the vehicle:\n"))
                vehicle = ElectricScooter(id,model,battery_percentage,max_speed)
            elif option == '2':
                id = input("Enter the id of the vehicle:\n")
                model = input("Enter the model of the vehicle:\n")
                battery_percentage = int(input("Enter the battery percentage of the vehicle:\n"))
                max_capacity = int(input("Enter the max speed of the vehicle:\n"))
                vehicle = ElectricCar(id,model,battery_percentage,max_capacity)

            self.hubs[hub_name].append(vehicle)
            print("vehicle added successfully")
            print(self.hubs)
    def add_multiple_vehicle_to_hub(self):
        hub_name = input("Enter the Hub name to Add vehicle to hub:\n")
        vehicle = None
        if hub_name not in self.hubs:
            print(f"Hub {hub_name} does not exist")
        else:
            for i in range(int(input("Enter the id  of the Vehicle:\n"))):
                option = input("Select the vehicle you want to add :\n enter 1 for Electric Scooter\n enter 2 for ELectric Car\n")
                if option == '1':
                    id = input("Enter the id of the Vehicle:\n")
                    model = input("Enter the model of the Vehicle:\n")
                    battery_percentage = int(input("Enter the battery percentage of the Vehicle:\n"))
                    max_speed = int(input("Enter the maximum speed of the Vehicle:\n"))
                    vehicle = ElectricScooter(id, model, battery_percentage, max_speed)
                elif option == '2':
                    id = input("Enter the id of the vehicle:\n")
                    model = input("Enter the model of the vehicle:\n")
                    battery_percentage = int(input("Enter the battery percentage of the vehicle:\n"))
                    max_capacity = int(input("Enter the max speed of the vehicle:\n"))
                    vehicle = ElectricCar(id,model,battery_percentage,max_capacity)
                self.hubs[hub_name].append(vehicle)
                print("vehicle added successfully")
                print(self.hubs)
