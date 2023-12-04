import json
import kettle

global materials
materials = []

def LoadJson():
    with open("material.json", "r") as dataFile:
        data = json.load(dataFile)
    for material in data["materials"]:
        materials.append(kettle.Kettle(material["name"], material["ThermalConductivity"], material["thickness"], 0.126))


def GetAllData(TempAmbMin, TempAmbMax, TempMax, TempMin):
    print("Enter the value of ambient temperature in Celcius (assuming it is a constant):")
    TempAmb = float(input())
    while(TempAmbMin>=TempAmb and TempAmb>=TempAmbMax){
        if(TempAmbMin>=TempAmb){
            print("Chosen temperature is too low. Min value = 7 C. Try again:")
        } elif (TempAmb>=TempAmbMax) {
            print("Chosen temperature is too high. Max value = 40 C. Try again:")
        }
        TempAmb = float(input())
    }

    print("Enter the value of wanted temperature of water in Celcius:")
    TempWanted = float(input())  
    while(TempMin>=TempWanted and TempWanted>=TempMax){
        if(TempMin>=TempWanted){
            print("Chosen temperature is too low. Min value = 7 C. Try again:")
        } elif (TempWanted>=TempMax) {
            print("Chosen temperature is too high. Max value = 40 C. Try again:")
        }
        TempWanted = float(input())
    }

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
    timeSimulation = 4000 #entire time for simulation
    time = [0.0] # time lapse vector
    timeI = 0.1 # time interval
    N = int(timeSimulation/timeI) + 1

    TempMin = 50 #min temperature to achieve via kettle
    TempMax = 90 #max temperature to achieve via kettle
    TempAmbMin = 10 #min temperature in outside enivironment
    TempAmbMax = 40 #max temperature in outside environment
    
    
    Kp = 0.02 #regulator gain
    HeatIn = [0.0] #heat created inside kettle
    HeatOut = [0.0] #heat loss to the outside environment

    newKettle, TempWanted, TempAmb = GetAllData(TempAmbMin, TempAmbMax, TempMax, TempMin)

    TempWater = [TempAmb] # assumption that water temperature is equal to ambient temperature at the start

    for _ in range(N):
        time.append(t[-1] + timeI)
        



LoadJson()







