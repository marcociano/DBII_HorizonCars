from flask import Flask, render_template, request
import Queries as queries
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
    lista = queries.car_alphabetical_sorting()
    car_price = []
    for i in lista:
        car_price.append((CarPrice.CarPrice(i)))
    return car_price


@app.route("/index")
def homepage():
    return render_template("index.html")


@app.route("/")
def main():
    return render_template("inderx.html")


@app.route("/query_page")
def query_page():
    return render_template("query_page.html")

#Ricerca
