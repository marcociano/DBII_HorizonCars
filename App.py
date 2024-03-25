from flask import Flask, render_template, request
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

        temp1 = 0
        temp2 = 0

        #Se la marca ed il modello della macchina rappresentano una stringa vuota, viene assegnato un dizionario {"$ne": None}
        if car_name == "":
            car_name = {"$ne": None}
        if fuel_type == "":
            fuel_type = {"$ne": None}
        if door_number == "":
            door_number = {"$ne": None}
        if car_body == "":
            car_body = {"$ne": None}

        #Qui di seguito gestisco i casi per i range di valori riguardanti i cavalli (hp_min e hp_max),
        #il consumo in città e autostrada (city_mpg_min, city_mpg_max e highway_mpg_min, highway_mpg_max) ed infine il prezzo (car_price_min e car_price_max).
        #A seconda di questi valori mi viene restituito il valore totale all'interno della tabella.

        if hp_min == "":
            if hp_max == "":
                horse_power = {"$ne": None, "$ne": None}
            else:
                temp2 = int(hp_max)
                horse_power = {"$ne": None, "$lt": temp2}
        else:
            temp1 = int(hp_min)
            if hp_max == "":
                horse_power = {"$gt": temp1, "$ne": None}
            else:
                temp2 = int(hp_min)
                horse_power = {"$gt": temp1, "$lt": temp2}

        if city_mpg_min == "":
            if city_mpg_max == "":
                city_mpg = {"$ne": None, "$ne": None}
            else:
                temp2 = int(city_mpg_max)
                city_mpg = {"$ne": None, "$lt": temp2}
        else:
            temp1 = int(city_mpg_min)
            if city_mpg_max == "":
                city_mpg = {"$gt": temp1, "$ne": None}
            else:
                temp2 = int(city_mpg_min)
                city_mpg = {"$gt": temp1, "$lt": temp2}

        if highway_mpg_min == "":
            if highway_mpg_max == "":
                highway_mpg = {"$ne": None, "$ne": None}
            else:
                temp2 = int(highway_mpg_max)
                highway_mpg = {"$ne": None, "$lt": temp2}
        else:
            temp1 = int(highway_mpg_min)
            if highway_mpg_max == "":
                highway_mpg = {"$gt": temp1, "$ne": None}
            else:
                temp2 = int(highway_mpg_min)
                highway_mpg = {"$gt": temp1, "$lt": temp2}

        if car_price_min == "":
            if car_price_max == "":
                price_of_car = {"$ne": None, "$ne": None}
            else:
                temp2 = float(car_price_max)
                price_of_car = {"$ne": None, "$lt": temp2}
        else:
            temp1 = float(car_price_min)
            if car_price_max == "":
                price_of_car = {"$gt": temp1, "$ne": None}
            else:
                temp2 = float(car_price_min)
                price_of_car = {"$gt": temp1, "$lt": temp2}

        print(car_name, fuel_type, door_number, car_body, horse_power, city_mpg, highway_mpg, price_of_car)

        try:
            listato= Query.search_car(car_name, fuel_type, door_number, car_body, horse_power, city_mpg, highway_mpg, price_of_car)
            list_car = []
            for i in listato:
                list_car.append(CarPrice.CarPrice(i))
            if len(list_car) != 0:
                return render_template("query_page.html", carlist_price= change_result(list_car))
                print("Effettuato")
            else:
                return render_template("query_page.html", respose= "Non esistono veicoli con queste caratteristiche.")
                print("Ricerca fallita")
        except:
            print("Non trovato")
            return render_template("query_page.html", response= "Nessun veicolo trovato.", carlist_price=get_result())
        return render_template("query_page.html", response= "Errore rilevato", carlist_price=get_result())

if __name__ == "__main__":
    app.run(debug=True)
