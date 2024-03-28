import BD_Connection_Pool as Cp


def search_car(car_name, fuel_type, door_number, car_body,
               horse_power, city_mpg, highway_mpg,
               price_of_car):
    col = Cp.connection_pool()
    query = col.find({"$and": [
        {"CarName": car_name},
        {"fueltype": fuel_type},
        {"doornumber": door_number},
        {"carbody": car_body},
        {"horsepower": horse_power},
        {"citympg": city_mpg},
        {"highwaympg": highway_mpg},
        {"price": price_of_car}
    ]})
    return query


def insert_new_car(new_car):
    col = Cp.connection_pool()
    col.insert_one({
        "car_ID": new_car.car_id,
        "CarName": new_car.car_name,
        "symboling": new_car.car_symboling,
        "fueltype": new_car.fuel_type,
        "aspiration": new_car.car_aspiration,
        "doornumber": new_car.door_number,
        "carbody": new_car.car_body,
        "drivewheel": new_car.drive_wheel,
        "enginelocation": new_car.engine_location,
        "wheelbase": new_car.wheel_base,
        "carlength": new_car.car_length,
        "carwidth": new_car.car_width,
        "carheight": new_car.car_height,
        "curbweight": new_car.curb_weight,
        "enginetype": new_car.engine_type,
        "cylindernumber": new_car.cylinder_number,
        "enginesize": new_car.engine_size,
        "fuelsystem": new_car.fuel_system,
        "boreratio": new_car.bore_ratio,
        "stroke": new_car.car_stroke,
        "compressionratio": new_car.compression_ratio,
        "horsepower": new_car.horse_power,
        "peakrpm": new_car.peak_rpm,
        "citympg": new_car.city_mpg,
        "highwaympg": new_car.highway_mpg,
        "price": new_car.price_of_car
    })


def update_car(car, modified):
    col = Cp.connection_pool()
    query = {"CarName": car}
    new_values = {
        "$set": {
            "CarName": modified.car_name,
            "symboling": modified.car_symboling,
            "fueltype": modified.fuel_type,
            "aspiration": modified.car_aspiration,
            "doornumber": modified.door_number,
            "carbody": modified.car_body,
            "drivewheel": modified.drive_wheel,
            "enginelocation": modified.engine_location,
            "wheelbase": modified.wheel_base,
            "carlength": modified.car_length,
            "carwidth": modified.car_width,
            "carheight": modified.car_height,
            "curbweight": modified.curb_weight,
            "enginetype": modified.engine_type,
            "cylindernumber": modified.cylinder_number,
            "enginesize": modified.engine_size,
            "fuelsystem": modified.fuel_system,
            "boreratio": modified.bore_ratio,
            "stroke": modified.car_stroke,
            "compressionratio": modified.compression_ratio,
            "horsepower": modified.horse_power,
            "peakrpm": modified.peak_rpm,
            "citympg": modified.city_mpg,
            "highwaympg": modified.highway_mpg,
            "price": modified.price_of_car
        }
    }
    print(new_values)
    col.update_one(query, new_values)


def delete_car(car_id, car_name):
    col = Cp.connection_pool()
    col.delete_many({"car_ID": car_id, "CarName": car_name})


def car_alphabetical_sorting():
    col = Cp.connection_pool()
    query = col.find().sort("CarName", 1)
    return query


def find_by_name(car_name):
    col = Cp.connection_pool()
    query = col({"CarName": car_name})
    return query


def find_by_symboling(car_symboling):
    col = Cp.connection_pool()
    query = col({"symboling": car_symboling})
    return query


def find_by_fueltype(fuel_type):
    col = Cp.connection_pool()
    query = col({"fueltype": fuel_type})
    return query


def find_by_aspiration(car_aspiration):
    col = Cp.connection_pool()
    query = col({"aspiration": car_aspiration})
    return query


def find_by_doornumber(door_number):
    col = Cp.connection_pool()
    query = col({"doornumber": door_number})
    return query


def find_by_carbody(car_body):
    col = Cp.connection_pool()
    query = col({"carbody": car_body})
    return query


def find_by_drivewheel(drive_wheel):
    col = Cp.connection_pool()
    query = col({"drivewheel": drive_wheel})
    return query


def find_by_enginelocation(engine_location):
    col = Cp.connection_pool()
    query = col({"enginelocation": engine_location})
    return query


def find_by_carlength(length):
    col = Cp.connection_pool()
    query = col({"carlength": length})
    return query


def find_by_carwidth(width):
    col = Cp.connection_pool()
    query = col({"carlength": width})
    return query


def find_by_carheight(height):
    col = Cp.connection_pool()
    query = col({"carlength": height})
    return query


def find_by_curbweight(curb):
    col = Cp.connection_pool()
    query = col({"carlength": curb})
    return query


def find_by_enginetype(engine_type):
    col = Cp.connection_pool()
    query = col({"enginetype": engine_type})
    return query


def find_by_cylindernumber(cylinder_number):
    col = Cp.connection_pool()
    query = col({"cylindernumber": cylinder_number})
    return query


def find_by_enginesize(engine_size):
    col = Cp.connection_pool()
    query = col({"enginesize": engine_size})
    return query


def find_by_fuelsystem(fuel_system):
    col = Cp.connection_pool()
    query = col({"fuelsystem": fuel_system})
    return query


def find_by_bore_ratio(bore_ratio):
    col = Cp.connection_pool()
    query = col({"boreratio": bore_ratio})
    return query


def find_by_compressionratio(compression_ratio):
    col = Cp.connection_pool()
    query = col({"compressionratio": compression_ratio})
    return query


def find_by_horsepower(min_hp, max_hp):
    col = Cp.connection_pool()
    query = col({"horsepower": {"$gt": min_hp, "$lt": max_hp}})
    return query


def find_by_max_peakratio(max_peak_ratio):
    col = Cp.connection_pool()
    query = col({"peakratio": {"$lt": max_peak_ratio}})
    return query


def find_by_citympg(min_cmpg, max_cmpg):
    col = Cp.connection_pool()
    query = col({"citympg": {"$gt": min_cmpg, "$lt": max_cmpg}})
    return query


def find_by_highwaympg(min_hmpg, max_hmpg):
    col = Cp.connection_pool()
    query = col({"highwaympg": {"$gt": min_hmpg, "$lt": max_hmpg}})
    return query


def find_by_price(min_p, max_p):
    col = Cp.connection_pool()
    query = col({"price": {"$gt": min_p, "$lt": max_p}})
    return query
