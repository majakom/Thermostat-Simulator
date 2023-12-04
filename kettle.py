

class Kettle:
    def __init__(self, material, thermalConductivity, thickness, area):
        self.material = material
        self.thermalConductivity = thermalConductivity
        self.thickness = thickness
        self.area = area
    def CalculateThermalResisatnce(self):
        return self.thickness/(self.thermalConductivity*self.area)
    def CalculateHeatLoss(self, TempWater, TempAmb, ThermalResistance):
        return (TempWater[-1] - TempAmb)/ThermalResistance
    def CalculateHeatProvided(self, voltage, current, time):
        return voltage[-1]*current*time
    def CalculateIsochoricSpecificHeat(self, TempWater):
        return 0.0001*(TempWater[-1]**3) - 0.035*(TempWater[-1]**2) - 2.4706*TempWater[-1] + 4219.1 # [J/(kg*K)]
    def CalculateWaterDensity(self, TempWater):
        return -0.0034*(TempWater[-1]**2) - 0.0929*TempWater[-1] + 1001.3 # [kg/m^3]
    def CalculateThermalCapacity(self, Density, TempWater):
        Volume = 1.7 #assumption that Volume is constant
        Mass = Density[-1]*Volume
        return Mass*self.CalculateIsochoricSpecificHeat(TempWater)
    def CalculateWaterTemperature(self, TempWater, HeatIn, TempAmb, ThermalResistance, ThermalCapacity):
        TempWater.append(TempWater[-1] + /ThermalCapacity)






        