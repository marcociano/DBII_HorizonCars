import numpy as np
from flask import Flask, render_template, request
from pymongo import MongoClient
import Queries as Query
import CarPrice

app = Flask(__name__, template_folder="front_end", static_folder="front_end/assets")

table = None


def get_result():
    return table


def change_result(value):
    global table
    table = value
    return get_result()


def full_table():
    lista = Query.car_alphabetical_sorting()
    list_car = []
    for i in lista:
        list_car.append((CarPrice.CarPrice(i)))
    return list_car


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/query_page')
def query_page():
    return render_template('query_page.html', carlist_price=change_result(full_table()))


# Ricerca veicolo
@app.route('/query_page/find_query', methods=['POST', 'GET'])
def find_query():
    if request.method == 'POST':
        car_name = request.form['find-car']
        fuel_type = request.form['find-car-fueltype']
        door_number = request.form['find-car-doornumber']
        car_body = request.form['find-car-body']
        hp_min = request.form['find-car-minhp']
        hp_max = request.form['find-car-maxhp']
        city_mpg_min = request.form['find-car-citympg-min']
        city_mpg_max = request.form['find-car-citympg-max']
        highway_mpg_min = request.form['find-car-highwaympg-min']
        highway_mpg_max = request.form['find-car-highwaympg-max']
        car_price_min = request.form['find-car-price-min']
        car_price_max = request.form['find-car-price-max']

        # Se la marca ed il modello della macchina rappresentano una stringa vuota, viene assegnato un dizionario {"$ne": None}

        if car_name == "":
            car_name = {"$ne": None}
        if fuel_type == "":
            fuel_type = {"$ne": None}
        if door_number == "":
            door_number = {"$ne": None}
        if car_body == "":
            car_body = {"$ne": None}

        # Qui di seguito gestisco i casi per i range di valori riguardanti i cavalli (hp_min e hp_max), il consumo in
        # città e autostrada (city_mpg_min, city_mpg_max e highway_mpg_min, highway_mpg_max) ed infine il prezzo (
        # car_price_min e car_price_max). A seconda di questi valori mi viene restituito il valore totale all'interno
        # della tabella.

        # Esempio per i cavalli (HP)
        if hp_min and hp_max:  # Entrambi i valori sono forniti
            horse_power = {"$gt": int(hp_min), "$lt": int(hp_max)}
        elif hp_min:  # Solo il minimo è fornito
            horse_power = {"$gt": int(hp_min)}
        elif hp_max:  # Solo il massimo è fornito
            horse_power = {"$lt": int(hp_max)}
        else:  # Nessun valore fornito
            horse_power = {"$ne": None}

        if city_mpg_min and city_mpg_max:  # Entrambi i valori sono forniti
            city_mpg = {"$gt": int(city_mpg_min), "$lt": int(city_mpg_max)}
        elif city_mpg_min:  # Solo il minimo è fornito
            city_mpg = {"$gt": int(city_mpg_min)}
        elif city_mpg_max:  # Solo il massimo è fornito
            city_mpg = {"$lt": int(city_mpg_max)}
        else:  # Nessun valore fornito
            city_mpg = {"$ne": None}

        if highway_mpg_min and highway_mpg_max:  # Entrambi i valori sono forniti
            highway_mpg = {"$gt": int(highway_mpg_min), "$lt": int(highway_mpg_max)}
        elif highway_mpg_min:  # Solo il minimo è fornito
            highway_mpg = {"$gt": int(highway_mpg_min)}
        elif highway_mpg_max:  # Solo il massimo è fornito
            highway_mpg = {"$lt": int(highway_mpg_max)}
        else:  # Nessun valore fornito
            highway_mpg = {"$ne": None}

        if car_price_min and car_price_max:  # Entrambi i valori sono forniti
            price_of_car = {"$gt": int(car_price_min), "$lt": int(car_price_max)}
        elif car_price_min:  # Solo il minimo è fornito
            price_of_car = {"$gt": int(car_price_min)}
        elif car_price_max:  # Solo il massimo è fornito
            price_of_car = {"$lt": int(car_price_max)}
        else:  # Nessun valore fornito
            price_of_car = {"$ne": None}

        print(car_name, fuel_type, door_number, car_body, horse_power, city_mpg, highway_mpg, price_of_car)
        try:
            listato = Query.search_car(car_name, fuel_type, door_number, car_body, horse_power, city_mpg, highway_mpg,
                                       price_of_car)
            list_car = []
            for i in listato:
                list_car.append(CarPrice.CarPrice(i))
            if len(list_car) != 0:
                return render_template("query_page.html", carlist_price=change_result(list_car))
                print("Effettuato")
            else:
                return render_template("query_page.html", respose="Non esistono veicoli con queste caratteristiche.")
                print("Ricerca fallita")
        except:
            print("Non trovato")
            return render_template('query_page.html', response="Nessun veicolo trovato.", carlist_price=get_result())
    return render_template("query_page.html", response="Errore rilevato", carlist_price=get_result())


def get_next_id():
    client = MongoClient('mongodb://localhost:27017')
    db = client.CarPrice
    collection = db.CarPrice
    # Cerca l'ultimo record basandosi sull'ID più alto
    last_record = collection.find_one(sort=[("car_ID", -1)])  # Assicurati che "car_ID" sia il campo giusto

    if last_record is not None:
        # Incrementa l'ID più alto di 1
        return last_record['car_ID'] + 1
    else:
        # Se non ci sono record, inizia da 1
        return 1


def convert_numpy_int_to_int(value):
    if isinstance(value, np.int64):
        return int(value)
    return value


# Fine filtri ricerca
@app.route('/query_page/insert_car', methods=['POST', 'GET'])
def insert_car():
    csv_path = 'CarPrice_formatted.csv'
    new_id = get_next_id(csv_path)

    car_name = request.form['insert-car']
    car_symboling = request.form['insert-car-symboling']
    fuel_type = request.form['insert-car-fueltype']
    car_aspiration = request.form['insert-car-aspiration']
    car_doornumber = request.form['insert-car-doornumber']
    car_body = request.form['insert-car-body']
    drive_wheel = request.form['insert-car-drivewheel']
    engine_location = request.form['insert-car-enginelocation']
    wheel_base = request.form['insert-car-wheelbase']
    car_length = request.form['insert-car-length']
    car_height = request.form['insert-car-height']
    car_width = request.form['insert-car-width']
    car_weight = request.form['insert-car-weight']
    engine_type = request.form['insert-car-enginetype']
    cylinder_number = request.form['insert-car-cylindernumber']
    engine_size = request.form['insert-car-enginesize']
    fuel_system = request.form['insert-car-fuelsystem']
    bore_ratio = request.form['insert-car-boreratio']
    car_stroke = request.form['insert-car-stroke']
    compression_ratio = request.form['insert-car-compressionratio']
    car_hp = request.form['insert-car-hp']
    peak_rpm = request.form['insert-car-peakrpm']
    city_mpg = request.form['insert-car-citympg']
    highway_mpg = request.form['insert-car-highwaympg']
    price_of_car = request.form['insert-car-price']

    car = {
        "car_ID": convert_numpy_int_to_int(new_id),
        "CarName": car_name,
        "symboling": car_symboling,
        "fueltype": fuel_type,
        "aspiration": car_aspiration,
        "doornumber": car_doornumber,
        "carbody": car_body,
        "drivewheel": drive_wheel,
        "enginelocation": engine_location,
        "wheelbase": wheel_base,
        "carlength": car_length,
        "carwidth": car_width,
        "carheight": car_height,
        "curbweight": car_weight,
        "enginetype": engine_type,
        "cylindernumber": cylinder_number,
        "enginesize": engine_size,
        "fuelsystem": fuel_system,
        "boreratio": bore_ratio,
        "stroke": car_stroke,
        "compressionratio": compression_ratio,
        "horsepower": car_hp,
        "peakrpm": peak_rpm,
        "citympg": city_mpg,
        "highwaympg": highway_mpg,
        "price": price_of_car
    }
    car_price = CarPrice.CarPrice(car)
    if CarPrice.checkformat(car_price):
        Query.insert_new_car(car_price)
        return render_template('query_page.html', response='Veicolo inserito correttamente', carlist_price=full_table())
    else:
        return render_template('query_page.html', response='Valori mancanti', carlist_price=get_result())


if __name__ == "__main__":
    app.run(debug=True)
