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
    material = request.form.get("typeMaterial")
    ambient = request.form.get("AmbientTemperature")
    temperature = request.form.get("Temperature")
    data = [int(material), int(ambient), int(temperature)]
    main.LoadJson()
    print(f"Material: {material}, Ambient: {ambient}, Temperature: {temperature}")

    time, TempWater = main.Calculate(data)
    df = pd.DataFrame({'Time [s]':time, 'Water temperature [C]':TempWater})
    fig =px.line(df, x='Time [s]', y='Water temperature [C]', title="Thermostat - PID regulator")
    
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("flaskApp.html", graphJSON=graphJSON)




if __name__ == '__main__':  
   app.run(debug=True)