from abc import ABC, abstractmethod

class Vehicle(ABC):

     def __init__(self, vehicle_id, model, battery_percentage):
         self.vehicle_id = vehicle_id
         self.model = model
         self.__rental_price = 0
         self.__maintenance_status = "Good"
        #correct setter call
         self.battery_percentage = battery_percentage
         self.set_battery_percentage(battery_percentage)

     @abstractmethod
     def calculate_trip_cost(self,distance):
        pass
     #-----------Battery Percentage-------
     def get_battery_percentage(self):
         return self.__battery_percentage
     def set_battery_percentage(self, battery_percentage):
         if 0 <= battery_percentage <= 100:
             self.__battery_percentage = battery_percentage
         else:
              raise ValueError("battery must be between 0 and 100")
    # --------Rental Price --------
     def get_rental_price(self):
        return self.__rental_price

     def set_rental_price(self,price):
        if price > 0:
            self.__rental_price = price
        else:
            raise ValueError("rental price must be positive")

     def get_maintenance_status(self):
         return self.__maintenance_status

     def set_maintenance_status(self, status):
         self.__maintenance_status = status

     def __eq__(self,other):
         return isinstance(other,Vehicle) and self.vehicle_id == other.vehicle_id
