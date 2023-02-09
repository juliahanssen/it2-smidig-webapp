from flask import Flask, render_template
from api import hent_filmliste

app = Flask(__name__)

filmliste = hent_filmliste()

@app.route("/")
def index():
    return render_template("index.html", filmliste=filmliste)

app.run(debug=True)