TempAmb #ambient temperature const
Tw = [] #water temperature
P #power const
t = [] #list to keep track of time
tempMax = 90 #maks temperature to get from thermostat
tempMin = 50 #min temperature to get from thermostat
tempAmbMin = 7 #min temperature to use thermostat in
tempAmbMax = 40 #maks temperature to use thermostat in
timeMax = 3600 #maks time in which you can heat water
timeMin = 120 #min time in which you can heat water
timeWanted #time needed to heat water
TempMax #temperature you want to achieve
Ti = 0.1 #min time difference
qt = [] #heat provided by the heater
q0 = [] #heat lost to the environment
h #fabric thickness
lambd #thermal conductivity depending on the fabric
m #mass of the fabric
Rt = h/lambd #thermal conductivity
U #voltage
I #current const



def GetAllData(TempMax, tmax, Ta):
    print("Time in which you want to heat water?\n")
    while(timeMax<= timeWanted and timeWanted <= timeMin){
        timeWanted = input()
    }
    while(tempMin>=TempMax and TempMax>=TempMax){
        print("Temperature you want: ")
        TempMax = input()
    }
    while(tempAmbMin>=Ta and Ta>=tempAmbMax){
        print("Temperature in your enivronment: ")
        TempAmb = input()
    }


    







