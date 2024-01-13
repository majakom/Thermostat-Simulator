from flask import Flask, render_template, request, jsonify
import json
import pandas as pd
import plotly
import plotly.express as px
import thermostat_formulas as main

app = Flask(__name__, template_folder='html_files')
@app.route("/")
@app.route("/flaskApp")
def flaskApp():
    return render_template('flaskApp.html')

@app.route("/GetParameters", methods=['POST', 'GET'])
def GetParameters():
    regulator = request.form.get("typeRegulator")
    material = request.form.get("typeMaterial")
    ambient = request.form.get("AmbientTemperature")
    temperature = request.form.get("Temperature")
    regulator_gain = request.form.get("regulatorGain")
    Ti = request.form.get("Ti")
    Td = request.form.get("Td")
    TInterval = request.form.get("TInterval")
    data = [int(material), int(ambient), int(temperature), float(regulator_gain), float(Ti), float(Td), float(TInterval), int(regulator)]
    main.LoadJson()
    print(f"Material: {material}, Ambient: {ambient}, Temperature: {temperature}, regulator_gain: {regulator_gain}, ")

    time, TempWater, Denisty, e, HeatOut, HeatIn, HeatSum, ThermalCapacity = main.Calculate(data)
    df = pd.DataFrame({'Time [s]':time, 'Water temperature [C]':TempWater})
    if(regulator == 0):
        fig =px.line(df, x='Time [s]', y='Water temperature [C]', title="Thermostat - PID regulator")
    else:
        fig =px.line(df, x='Time [s]', y='Water temperature [C]', title="Thermostat - PI regulator")
    
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("flaskApp.html", graphJSON=graphJSON)




if __name__ == '__main__':  
   app.run(debug=True)