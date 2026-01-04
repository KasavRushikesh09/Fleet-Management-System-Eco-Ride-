from abc import ABC, abstractmethod
class Vehicle(ABC):
     @abstractmethod
     def calculate_trip_cost(self,distance):
        pass
     def __init__(self, vehicle_id, model, battery_percentage):
         self.vehicle_id = vehicle_id
         self.model = model
         self.battery_percentage = None
        #correct setter call
         self.set_battery_percentage(battery_percentage)

     #-----------Battery Percentage-------
     def get_battery_percentage(self):
         return self.__battery_percentage
     def set_battery_percentage(self, battery_percentage):
         if 0 <= battery_percentage <= 100:
             self.__battery_percentage = battery_percentage
         else:
             print("Battery percentage must be between 0 and 100")
     # ---------Maintenance Status ----------
     def get_maintenance_status(self):
         return self.__maintenance_status
     def set_maintenance_status(self, maintenance_status):
         self.__maintenance_status = maintenance_status

    # --------Rental Price --------
     def get_rental_price(self):
        return self.__rental_price

     def set_rental_price(self,price):
        if price > 0:
            self.__rental_price = price
        else:
            print("Rental price must be greater than 0")
