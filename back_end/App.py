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
    car_price = []
    for i in lista:
        car_price.append((CarPrice.CarPrice(i)))
    return car_price


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/query_page')
def query_page():
    return render_template("query_page.html", list_air=change_result(full_table()))


if __name__ == "__main__":
    app.run(debug=True)
