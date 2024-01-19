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
    print(f"Material: {material}, Ambient: {ambient}, Temperature: {temperature}, regulator_gain: {regulator_gain}, regulator: {regulator}")


    time, TempWater, Density, e, HeatOut, HeatIn, HeatSum, ThermalCapacity = main.Calculate(data)

    timeHour = []
    for i in range(len(time)):
        timeHour.append(time[i]/3600)

    df = pd.DataFrame({'Time [h]':timeHour, 'Water temperature [C]':TempWater})
    df2 = pd.DataFrame({'Time [h]':timeHour, 'Water Density [kg/m^3]':Density})
    df3 = pd.DataFrame({'Time [h]':timeHour, 'e':e})
    df4 = pd.DataFrame({'Time [h]':timeHour, 'Heat Out [kg*m^2*s^-2]':HeatOut})
    df5 = pd.DataFrame({'Time [h]':timeHour, 'Heat in [kg*m^2*s^-2]':HeatIn})
    df6 = pd.DataFrame({'Time [h]':timeHour, 'Heat Sum [kg*m^2*s^-2]':HeatSum})
    df7 = pd.DataFrame({'Time [h]':timeHour, 'Thermal Capacity [J/C]':ThermalCapacity})

    if(not int(regulator)):
        fig =px.line(df, x='Time [h]', y='Water temperature [C]', title="Thermostat - PID regulator, water temperature")
        fig2 = px.line(df2, x = 'Time [h]', y='Water Density [kg/m^3]', title = "Thermostat - PID regulator, water density")
        fig3 = px.line(df3, x = 'Time [h]', y='e', title = "Thermostat - PID regulator, e")
        fig4 = px.line(df4, x = 'Time [h]', y='Heat Out [kg*m^2*s^-2]', title = "Thermostat - PID regulator, heat out")
        fig5 = px.line(df5, x = 'Time [h]', y = 'Heat in [kg*m^2*s^-2]', title = "Thermostat - PID regulator, heat created inside kettle")
        fig6 = px.line(df6, x = 'Time [h]', y = 'Heat Sum [kg*m^2*s^-2]', title = "Thermostat - PID regulator, heat created substracted by heat loss")
        fig7 = px.line(df7, x = 'Time [h]', y = 'Thermal Capacity [J/C]', title = "Thermostat - PID regulator - Thermal Capacity")
    else:
        fig =px.line(df, x='Time [h]', y='Water temperature [C]', title="Thermostat - PI regulator")
        fig2 = px.line(df2, x = 'Time [h]', y='Water Density [kg/m^3]', title = "Thermostat - PI regulator, water density")
        fig3 = px.line(df3, x = 'Time [h]', y='e', title = "Thermostat - PI regulator, e")
        fig4 = px.line(df4, x = 'Time [h]', y='Heat Out [kg*m^2*s^-2]', title = "Thermostat - PI regulator, heat out")
        fig5 = px.line(df5, x = 'Time [h]', y = 'Heat in [kg*m^2*s^-2]', title = "Thermostat - PI regulator, heat created inside kettle")
        fig6 = px.line(df6, x = 'Time [h]', y = 'Heat Sum [kg*m^2*s^-2]', title = "Thermostat - PI regulator, heat created substracted by heat loss")
        fig7 = px.line(df7, x = 'Time [h]', y = 'Thermal Capacity [J/C]', title = "Thermostat - PI regulator - Thermal Capacity")
    fig.add_hline(y=temperature)
    
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON3 = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON4 = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON5 = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON6 = json.dumps(fig6, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON7 = json.dumps(fig7, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("flaskApp.html", graphJSON=graphJSON, graphJSON2=graphJSON2, graphJSON3=graphJSON3, graphJSON4=graphJSON4, graphJSON5=graphJSON5, graphJSON6=graphJSON6, graphJSON7=graphJSON7)




if __name__ == '__main__':  
   app.run(debug=True)