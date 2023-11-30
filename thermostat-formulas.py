import json
Power = [] #power const
PowerMin #min power
PowerMax #max power

time = [] #list to keep track of time
timeSimulation = 4000 #s - time of the simulation
Ti = 0.1 #min time difference
N = int(timeSimulation/Ti) + 1 #the amount of the tests

TempMax = 90 #max temperature to get from thermostat
TempMin = 50 #min temperature to get from thermostat
TempAmbMin = 7 #min temperature to use thermostat in
TempAmbMax = 40 #max temperature to use thermostat in
TempAmb #ambient temperature - const
TempWanted #temperature you want to achieve
TempWater = [] #water temperature

Kp = 0.02 #regulator gain


U_min # min voltage
U_max #max voltage


qt = [] #heat provided by the heater
q0 = [] #heat loss to the environment
h #fabric thickness
lambd #thermal conductivity depending on the fabric
m #mass of the fabric
Rt = h/lambd #thermal conductivity
U #voltage
I #current const



def GetAllData(TempAmbMin, TempAmbMax):
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
    print("(1) Ceramic")
    print("(2) Glass")
    print("(3) Copper")
    print("(4) Aluminium")
    choice = int(input())
    match choice:
        case 0:
            


    







