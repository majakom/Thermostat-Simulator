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
    time, TempWater = main.Calculate(data)
    df = pd.DataFrame({'x_data':time, 'y_data':TempWater})

    fig =px.line(df, x='x_data', y='y_data', title="Testing")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    fig.write_html("ThermostatSimulator/html_files/graphApp.html")
    print(f"Material: {material}, Ambient: {ambient}, Temperature: {temperature}")
    
    return render_template('result.html')




if __name__ == '__main__':  
   app.run(debug=True)