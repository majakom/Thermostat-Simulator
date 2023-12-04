import json
import kettle
import matplotlib.pyplot as plt

global materials
materials = []

def LoadJson():
    with open("material.json", "r") as dataFile:
        data = json.load(dataFile)
    for material in data["materials"]:
        materials.append(kettle.Kettle(material["name"], material["ThermalConductivity"], material["thickness"], 0.126))
LoadJson()
print(type(materials[0].material))

def GetAllData(TempAmbMin, TempAmbMax, TempMax, TempMin):
    print("Enter the value of ambient temperature in Celcius (assuming it is a constant):")
    TempAmb = float(input())
    while(TempAmbMin>=TempAmb and TempAmb>=TempAmbMax):
        if(TempAmbMin>=TempAmb):
            print("Chosen temperature is too low. Min value = 7 C. Try again:")
        elif (TempAmb>=TempAmbMax):
            print("Chosen temperature is too high. Max value = 40 C. Try again:")
        TempAmb = float(input())

    print("Enter the value of wanted temperature of water in Celcius:")
    TempWanted = float(input())  
    while(TempMin>=TempWanted and TempWanted>=TempMax):
        if(TempMin>=TempWanted):
            print("Chosen temperature is too low. Min value = 7 C. Try again:")
        elif (TempWanted>=TempMax):
            print("Chosen temperature is too high. Max value = 40 C. Try again:")
        TempWanted = float(input())

    print("Choose the material of the thermostat:")
    print("(0) Stainless steel")
    print("(1) Glass")
    print("(2) Copper")
    print("(3) Aluminium")
    choice = int(input())
    match choice:
        case 0:
            newKettle = materials[0]
        case 1:
            newKettle = materials[1]
        case 2:
            newKettle = materials[2]
        case 3:
            newKettle = materials[3]

    return newKettle, TempWanted, TempAmb

def Calculate():
    voltagePID = [0.0] # voltage in PID regulator
    voltage  = [0.0] # voltage now
    voltageMin = 0.0 #min voltage possible
    voltageMax = 240.0 # max voltage possible to use

    currentMin = 0 #current relays on the value of the voltage
    currentMax = 13
    current = [0.0]

    power = [0.0]

    timeSimulation = 4000 #entire time for simulation
    time = [0.0] # time lapse vector
    timeInterval = 0.1 # time interval
    timeI = 2.5
    timeD = 0.0
    N = int(timeSimulation/timeInterval) + 1

    TempMin = 50 #min temperature to achieve via kettle
    TempMax = 90 #max temperature to achieve via kettle
    TempAmbMin = 10 #min temperature in outside enivironment
    TempAmbMax = 40 #max temperature in outside environment
    
    Density = [] # density of water

    HeatIn = [0.0] #heat created inside kettle
    HeatOut = [0.0] #heat loss to the outside environment

    
    Kp = 0.02 #regulator gain
    
    newKettle, TempWanted, TempAmb = GetAllData(TempAmbMin, TempAmbMax, TempMax, TempMin)

    TempWater = [TempAmb] # assumption that water temperature is equal to ambient temperature at the start
    e = [(TempWanted - TempWater[0])] # tilt in the beginning
    sumE = [e[0]] #sum of tilts

    ThermalCapacity = [0.0]
    SpecificHeat = [0.0]
    ThermalResistance = newKettle.CalculateThermalResistance() #calculate thermal resistance

    for _ in range(N):
        time.append((time[-1] + timeInterval))
        e.append((TempWanted - TempWater[-1]))
        sumE.append((sumE[-1] + e[-1]))
        voltagePID.append(Kp*(e[-1] + (timeInterval/timeI)*sumE[-1] + (timeD/timeInterval)*(e[-1]-e[-2])))
        voltage.append(max(voltageMin, min(voltageMax, voltagePID[-1])))
        current.append((currentMax - currentMin)/(voltageMax - voltageMin) * (voltage[-1] - voltageMin) + currentMin)
        power.append(newKettle.CalculatePower(voltage, current))

        Density.append((newKettle.CalculateWaterDensity(TempWater)))
        SpecificHeat.append(newKettle.CalculateIsochoricSpecificHeat(TempWater))
        ThermalCapacity.append(newKettle.CalculateThermalCapacity(Density, SpecificHeat))
        HeatOut.append(newKettle.CalculateHeatLoss(TempWater, TempAmb, ThermalResistance))
        HeatIn.append(newKettle.CalculateHeatProvided(power, time))
        TempWater.append(newKettle.CalculateWaterTemperature(TempWater, HeatIn, HeatOut, timeInterval, ThermalCapacity))





LoadJson()
Calculate()







