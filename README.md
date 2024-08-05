# Thermostat Simulator

Project made for Basics Of Control Engineering laboratories at Poznań University of Technology. <br />
Web app was made for simulating thermostat behaviour considering different settings.

The simulated thermostat uses a heater to make water gain the desired by the user temperature,
and then maintain it. The simulator assumes that the volume of water to be heated is constant and equal to
0,17 [m3]. The simulator takes into account the possibility of adjusting the desired final temperature of the
water, the ambient temperature, which is also initially equal to the water temperature in the
thermostat and one of the three materials (included in a json file) from which the thermostat can be constructed. Such
simulator is designed to regulate the power supplied to the thermostat so that the water reaches the temperature 
set previously by the user.

## Settings
Simulation settings include: <br />

   * ambient temperature <br />
   * desired temperature of water inside the thermostat <br />
   * fabric of which such thermostat is made of <br />
   * type of regulator (although project mostly focuses on PID regulator) <br />
   * regulator gain
   * Time interval of making calculations
   * Ti
   * Td


## General Information

Repo consists of: <br /><br />
   * [material.json](material.json) - json file with types of materials and their characteristics concerning thermodynamics therms.
   In order to add a new material to the simulator programm you should add its characteristics to this file.<br /> <br />
   * [Kettle.py](Kettle.py) - python file with a class containing physical and mathematical formulas necessary for visualizations in the form of graphs. <br /> <br />
   * [thermostat.py](thermostat.py) - python file - includes flask <br /> <br />
   * [thermostat_formulas.py](thermostat_formulas.py) - runs necessary calculations depending on types of data provided by user via website. <br /> <br />
   * [CSS file](static) - visual side of the website <br /> <br />
   * [HTML file](html_files) - allows user to enter needed data or choose settings for the simulation about to be run; displays graphs that depict the process of the simulation <br /> <br />

Web app created using flask.

The command-line prototype involved using matplotlib library.

## Documentation

* [Here](documentation.pdf) You can find documentation which focuses mostly on formulas used for calculations in the simulator. 
