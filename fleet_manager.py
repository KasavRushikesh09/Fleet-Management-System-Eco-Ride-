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
            from ElectricScooter import ElectricScooter
            speed = int(input("Max speed: "))
            vehicle = ElectricScooter(vehicle_id, model, battery, speed)

        elif option == '2':
            from ElectricCar import ElectricCar
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
