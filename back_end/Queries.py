import BD_Connection_Pool as Cp
import CarPrice


def search_with_all_parameter(car_id, car_symboling, car_name, fuel_type, car_aspiration, door_number, car_body, drive_wheel,
                              engine_location, wheel_base, car_length,
                              car_width, car_height, curb_weight, engine_type, cylinder_number, engine_size,
                              fuel_system,
                              bore_ratio,
                              car_stroke, compression_ratio, horse_power, peak_rpm, city_mpg, highway_mpg,
                              car_of_price):
    col = Cp.connection_pool()
    query = col.find({"$and": [
        {"Car_ID": car_id},
        {"simboling": car_symboling},
        {"CarName": car_name},
        {"fueltype": fuel_type},
        {"aspiration": car_aspiration},
        {"doornumber": door_number},
        {"carbody": car_body},
        {"drivewheel": drive_wheel},
        {"enginelocation": engine_location},
        {"wheelbase": wheel_base},
        {"carlength": car_length},
        {"carwidth": car_width},
        {"carheight": car_height},
        {"curbweight": curb_weight},
        {"enginetype": engine_type},
        {"cylindernumber": cylinder_number},
        {"enginesize": engine_size},
        {"fuelsystem": fuel_system},
        {"boreratio": bore_ratio},
        {"carstroke": car_stroke},
        {"compressionratio", compression_ratio},
        {"horsepower": horse_power},
        {"peakrpm": peak_rpm},
        {"citympg": city_mpg},
        {"highwaympg": highway_mpg},
        {"price": car_of_price}
    ]})
    return query


def insert_car(new_car):
    col = Cp.connection_pool()
    col.insert_one({
        ""
    })


def car_alphabetical_sorting():
    col = Cp.connection_pool()
    query = col.find().sort("CarName", 1)
    return query
