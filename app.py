from flask import Flask, render_template
import requests
from yr import hent_temp

app = Flask(__name__)

@app.route("/")
def index():
    temperatur = hent_temp(59.89, 10.52)
    print(f"Tempratur: {temperatur}")
    sted = "sandvika"
    return render_template("index.html", sted=sted, temperatur=temperatur)

app.run(debug=True)