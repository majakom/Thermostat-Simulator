# Thermostat Simulator

Project made for Basics Of Control Engineering laboratories at Poznań University of Technology.

## General Information

Repo consists of: <br /><br />
   * [material.json](material.json) - json file with types of materials and their characteristics concerning thermodynamics therms.
   In order to add a new material to the simulator programm you should add its characteristics to this file.<br /> <br />
   * [Kettle.py](Kettle.py) - python file with a class containing physical and mathematical formulas necessary for visualizations in the form of graphs. <br /> <br />
   * [thermostat.py](thermostat.py) - python file - includes flask <br /> <br />
   * [thermostat_formulas.py](thermostat_formulas.py) - runs necessary calculations depending on types of data provided by user via website. <br /> <br />
   * [CSS file](static) - visual side of the website <br /> <br />
   * [HTML file](html_files) - allows user to enter needed data or choose settings for the simulation about to be run; displays graphs that depict the process of the simulation <br /> <br />

Site created using flask.

The command-line prototype involved using matplotlib library.

## Documentation

* [Here](documentation.pdf) You can find documentation which focuses mostly on formulas used for calculations in the simulator. 
