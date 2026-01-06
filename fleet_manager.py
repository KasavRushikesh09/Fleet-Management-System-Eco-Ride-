from ElectricScooter import ElectricScooter
from ElectricCar import ElectricCar

class Fleetmanager:

    def __init__(self):
        self.hubs = {}

    def add_hub(self):
        hub = input("Enter hub name: ")
        if hub in self.hubs:
            print("Hub already exists")
        else:
            self.hubs[hub] = []
            print(f"{hub} added successfully")

    def add_vehicle_to_hub(self):
        hub = input("Enter hub name: ")
        if hub not in self.hubs:
            print("Hub not found")
            return

        option = input("1. Scooter\n2. Car\nChoose: ")

        vehicle_id = input("Vehicle ID: ")
        model = input("Model: ")
        battery = int(input("Battery %: "))

        if option == '1':
            speed = int(input("Max speed: "))
            vehicle = ElectricScooter(vehicle_id, model, battery, speed)

        elif option == '2':
            seats = int(input("Seating capacity: "))
            vehicle = ElectricCar(vehicle_id, model, battery, seats)

        else:
            print("Invalid option")
            return

        for v in self.hubs[hub]:
            if v == vehicle:
                print("Vehicle already exists")
                return

        self.hubs[hub].append(vehicle)
        print("Vehicle added successfully")
    #UC 8
    def search_by_hub(self,hub_name):
        if hub_name not in self.hubs:
            print("Hub not found")
            return []
        return self.hubs[hub_name]

    def search_high_battery_vehicles(self):
        all_vehicles = []
        for vehicles in self.hubs.values():
            all_vehicles.extend(vehicles)

        return list(filter(lambda v:v.get_battery_percentage()>80,all_vehicles))

    # UC 9
    def categorized_view(self):
        categorized = {
            "Car":[],
            "Scooter":[]
        }
        #collect vehicles from all hubs
        for vehicles in self.hubs.values():
            for v in vehicles:
                if isinstance(v,ElectricCar):
                    categorized["Car"].append(v)
                elif isinstance(v,ElectricScooter):
                    categorized["Scooter"].append(v)

        return categorized

    
