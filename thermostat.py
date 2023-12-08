from flask import Flask
#import thermostat_formulas
app = Flask(__name__)
@app.route("/")
def home():
    return "h"