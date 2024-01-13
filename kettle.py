

class Kettle:
    def __init__(self, material, thermalConductivity, thickness, area):
        self.material = material
        self.thermalConductivity = thermalConductivity
        self.thickness = thickness
        self.area = area
    def CalculateThermalResistance(self):
        return self.thickness/(self.thermalConductivity*self.area)
    def CalculateHeatLoss(self, TempWater, TempAmb, ThermalResistance):
        return (TempWater[-1] - TempAmb)/ThermalResistance
    def CalculateHeatProvided(self, power, time):
        return power[-1]*time[-1]
    def CalculateIsochoricSpecificHeat(self, TempWater):
        return 0.0001*(TempWater[-1]**3) - 0.035*(TempWater[-1]**2) - 2.4706*TempWater[-1] + 4219.1 # [J/(kg*K)]
    def CalculateWaterDensity(self, TempWater):
        return -0.0034*(TempWater[-1]**2) - 0.0929*TempWater[-1] + 1001.3 # [kg/m^3]
    def CalculatePower(self, voltage, current):
        return voltage[-1]*current[-1]
    def CalculateThermalCapacity(self, Density, SpecificHeat):
        Volume = 0.17 #assumption that Volume is constant 
        Mass = Density[-1]*Volume
        return Mass*SpecificHeat[-1]
    def CalculateWaterTemperature(self, TempWater, HeatIn, HeatOut, timeInterval, ThermalCapacity):
        return TempWater[-1] + ((HeatIn[-1] - HeatOut[-1])*timeInterval / ThermalCapacity[-1])
        






        