from typing import Type, Any


class CarPrice:
    # Inizializzo gli attributi dell'oggetto CarRetail recuperandoli dal database
    def __init__(self, car_price):
        self.car_id = car_price["Car_ID"]
        self.car_symboling = car_price["symboling"]
        self.car_name = car_price["CarName"]
        self.fuel_type = car_price["fueltype"]
        self.car_aspiration = car_price["aspiration"]
        self.door_number = car_price["doornumber"]
        self.car_body = car_price["carbody"]
        self.drive_wheel = car_price["drivewheel"]
        self.engine_location = car_price["enginelocation"]
        self.wheel_base = car_price["wheelbase"]
        self.car_length = car_price["carlength"]
        self.car_width = car_price["carwidth"]
        self.car_height = car_price["carheight"]
        self.curb_weight = car_price["curbweight"]
        self.engine_type = car_price["enginetype"]
        self.cylinder_number = car_price["cylindernumber"]
        self.engine_size = car_price["enginesize"]
        self.fuel_system = car_price["fuelsystem"]
        self.bore_ratio = car_price["boreratio"]
        self.car_stroke = car_price["stroke"]
        self.compression_ratio = car_price["compressionratio"]
        self.horse_power = car_price["horsepower"]
        self.peak_rpm = car_price["peakrpm"]
        self.city_mpg = car_price["citympg"]
        self.highway_mpg = car_price["highwaympg"]
        self.price_of_car = car_price["price"]

    # Restituisco l'oggetto come se fosse un dizionario
    def dump(self):
        return {
            "Car_ID": self.car_id,
            "symboling": self.car_symboling,
            "CarName": self.car_name,
            "fueltype": self.fuel_type,
            "aspiration": self.car_aspiration,
            "doornumber": self.door_number,
            "cabody": self.car_body,
            "drivewheel": self.drive_wheel,
            "enginelocation": self.engine_location,
            "wheelbase": self.wheel_base,
            "carlength": self.car_length,
            "carwidth": self.car_width,
            "carheight": self.car_height,
            "curbweight": self.curb_weight,
            "enginetype": self.engine_type,
            "cylindernumber": self.cylinder_number,
            "enginesize": self.engine_size,
            "fuelsystem": self.fuel_system,
            "boreratio": self.bore_ratio,
            "stroke": self.car_stroke,
            "compressionratio": self.compression_ratio,
            "horsepower": self.horse_power,
            "peakrpm": self.peak_rpm,
            "citympg": self.city_mpg,
            "highwaympg": self.highway_mpg,
            "price": self.price_of_car
        }


# Controllo se i parametri dell'oggetto sono vuoti
def checkformat(test):
    if (
            test.car_id == "" and
            test.car_symboling == "" and test.car_name == "" and
            test.fuel_type == "" and test.car_aspiration == "" and
            test.door_number == "" and test.car_body == "" and
            test.drive_wheel == "" and test.engine_location == "" and
            test.wheel_base == "" and test.car_length == "" and
            test.car_width == "" and test.car_height == "" and
            test.curb_weight == "" and test.engine_type == "" and
            test.cylinder_number == "" and test.engine_size == "" and
            test.engine_size == "" and test.fuel_system == "" and
            test.bore_ratio == "" and test.car_stroke == "" and
            test.compression_ratio == "" and test.horse_power == "" and
            test.peak_rpm == "" and test.city_mpg == "" and
            test.highway_mpg == "" and test.price_of_car == ""
    ):
        return False
    return True
