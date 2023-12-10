from flask import Flask, render_template, request, jsonify
import thermostat_formulas as main

app = Flask(__name__, template_folder='html_files')
@app.route("/")
@app.route("/flaskApp")
def flaskApp():
    return render_template('flaskApp.html')

@app.route("/GetParameters", methods=["POST"])
def GetParameters():
    material = request.form.get("typeMaterial")
    ambient = request.form.get("AmbientTemperature")
    temperature = request.form.get("Temperature")
    data = [material, ambient, temperature]
    main.GetDataFromFlask(data)
    print(f"Material: {material}, Ambient: {ambient}, Temperature: {temperature}")
    
    return jsonify(data)

if __name__ == '__main__':  
   app.run(debug=True)