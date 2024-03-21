from typing import Type, Any


class CarRetail:
    # Inizializzo gli attributi dell'oggetto CarRetail recuperandoli dal database
    def __init__(self, car_retail):
        self.make = car_retail["Make"]
        self.model = car_retail["Model"]
        self.year = car_retail["Year"]
        self.engine_fuel_type = car_retail["Engine Fuel Type"]
        self.engine_hp = car_retail["Engine HP"]
        self.engine_cylinders = car_retail["Engine Cylinders"]
        self.transmission_type = car_retail["Transmission Type"]
        self.driven_wheels = car_retail["Driven_Wheels"]
        self.numbers_of_doors = car_retail["Numbers of Doors"]
        self.market_category = car_retail["Market Category"]
        self.vehicle_size = car_retail["Vehicle Size"]
        self.vehicle_style = car_retail["Vehicle Style"]
        self.highway_mpg = car_retail["Highway MPG"]
        self.city_mpg = car_retail["city mpg"]
        self.msrp = car_retail["MSRP"]

    # Restituisco l'oggetto come se fosse un dizionario
    def dump(self):
        return {
            "Make": self.make,
            "Model": self.model,
            "Year": self.year,
            "Engine Fuel Type": self.engine_fuel_type,
            "Engine HP": self.engine_hp,
            "Engine Cylinders": self.engine_cylinders,
            "Transmission Type": self.transmission_type,
            "Driven_Wheels": self.driven_wheels,
            "Numbers of Doors": self.numbers_of_doors,
            "Market Category": self.market_category,
            "Vehicle Size": self.vehicle_size,
            "Highway MPG": self.highway_mpg,
            "city mpg": self.city_mpg,
            "MSRP": self.msrp
        }


# Controllo se i parametri dell'oggetto sono vuoti
def checkformat(test):
    if (
            test.make == "" and test.model == "" and
            test.year == "" and test.engine_fuel_type == "" and
            test.engine_hp == "" and test.engine_cylinders == "" and
            test.transmission_type == "" and test.driven_wheels == "" and
            test.numbers_of_doors == "" and test.market_category == "" and
            test.vehicle_size == "" and test.highway_mpg == "" and
            test.city_mpg == "" and test.msrp == ""
    ):
        return False
    return True
