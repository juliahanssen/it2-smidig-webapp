from flask import Flask, render_template
import requests
from yr import hent_temp 
from yr import hent_vind, hent_vaer


app = Flask(__name__)

@app.route("/")
def index():
    temperatur = hent_temp(59.89, 10.52)
    vind = hent_vind(59.89, 10.52)
    vaer = hent_vaer(59.89, 10.52)
    print(f"Tempratur: {temperatur}")
    print(f"Vær: {vaer}")
    print(f"Vind: {vind}")
    sted = "sandvika"
    return render_template("index.html", sted=sted, temperatur=temperatur, vind=vind, vaer=vaer)


app.run(debug=True)
