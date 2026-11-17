Project Name    - Drive Eco

Description     - Ready for E-motion? This project is formulated around the European continent and is to euducate the end user about the emissions of greenhouse gases by the mode of transportation. Here, we have analysed various aspects pertaining to the emission and the possible solution to it, solution being use of EV's in the present & future until there is a superior technologcial advancement in place. 

Project By      - Team Rio - Matthieu Momdain - Project Manager, Bharat Singh - Consultant, Paakwesi Yankson - Consultant.

Project requirements    -  Following are required platform and libraries used for the projetc and are essential for running the project:- 
(a) IDE (Integrated Development Environment) - VS Code, jupiter notebook, google colab.                                                                                   (b) Libraries required : base libraries to run code:- pandas- import pandas as pd, numpy - import numpy as np, sys - import sys;                                     Libraries for visualisation:- seaborn - import seaborn as sns, plotly - import plotly.express as px, matplotlib - import matplotlib.pyplot as plt;                        For web scraping: requests - import requests, Beautifulsoup (fetch data) - from bs4 import BeautifulSoup, widgets - pip install ipywidgets, from ipywidgets import interact, Dropdown;                                                                                                                                                                    Presentation:- streamlit - import sys, !{sys.executable} -m pip install streamlit, !{sys.executable} -m streamlit --version, pip install --upgrade streamlit, create a streamlit.ipynb file in the project folder where all of your work data on the project are located;                                                                         To run presentation:- create an app.py file in the: project folder/streamlit_app folder and in the streamlit.ipynb file terminal run code - streamlit run app.py  

Data Source     - EV sales data - iea.org/data-and-statistics/data-tools/global-ev-data-explorer; Emission comparission; Website: eea.europa.eu / theicct.org; EV registration data in europe Source : European Environment Agency data - https://www.eea.europa.eu/en/analysis/indicators/new-registrations-of-electric-vehicles/new-registration-of-electric-cars ; cost comparision b/w ev and petrol charge rates Source : •	Website: theaa.ie/chargingcost.eu	Application: Supplies baseline retail pump prices for petrol (€1.75/L) and diesel (€1.65/L) as well as household and blended public electricity tariffs (€0.30 to €0.38/kWh) used to calculate operating costs per 100 km.; Transport emission: DATA_SOURCE_NAME = "European Environment Agency (EEA) & Eurostat" DATA_SOURCE_URL = "https://www.eea.europa.eu/en/analysis/indicators/greenhouse-gas-emissions-from-transport"; Data Source for percentage share of various sectors in Europe: https://www.eea.europa.eu/en/analysis/publications/key-trends-and-drivers-in-ghg-emissions-in-the-eu/trends-ghg-emissions-sector; Average Fuel Price by Country in 1H2026 https://energy.ec.europa.eu/document/download/906e60ca-8b6a-44e7-8589-652854d2fd3f_en?filename=Weekly_Oil_Bulletin_Prices_History_maticni_4web.xlsx; CO2e emissions at the exhaust pipe per litre of fuel (webscrapping) https://www.vmaths.fr/apps/convertisseur-carburant-co2.html; energy mix of electricity production, and CO2e production for the year 2025 https://files.ember-energy.org/public-downloads/generation/outputs/release_generation_yearly_lower.csv; Price of electricity per kWh per country for a household: https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/nrg_pc_204$defaultview/1.0?compress=false&format=tsv; Number of charging stations per country
https://ec.europa.eu/eurostat/databrowser/view/road_if_rchev__custom_23884693/default/table; Number of inhabitants and area of countries
https://ec.europa.eu/eurostat/databrowser/view/reg_area3__custom_23884225/default/table - area of countries; Average Charging Price 2026 AU KWH: Eleport's Handcrafted Series https://eleport.com/price-report/


Project Application - Educating them about the emissions rates by various categories of vehicles and Motivate the end user towards investing in EV's for a better environment, the project also provides the user to filter through the EV's from the data base based on the filter options of price, battery capacity, range of distance in one charge, Car Brand and model of car. With this search the user gets a fine idea of which vehicle he/ she can buy.

Hypothesis:
We are interested in the impact of greenhouse gases emission on climate change with a focus on Europe. We know that transport accounts for 26 % of emissions on this continent. Of these emissions, 44% are emitted by private vehicles.
As a consultant in electric mobility and in view of the effort to be made to massively equip countries with electric vehicles, we want to involve governments and private public authorities to facilitate an educated choice towards access to the electric car fleet, reduce the dependence of our countries on fuel imports, starting with quick wins.
Problem/Topic:
The answer we could make, in short, is to massively propose to switch to electric mobility, yes, but from one country to another, the fact of no longer choosing a combustion vehicle implies impacts that must be measured.
From one country to another:
- the energy mix differs, implying a more or less carbon-intensive production of energy, at a more or less important price.
-The price of energy too.
-the practicality of finding a charging station must be known.
In addition: the type of vehicle must be taken into account according to the needs and means of the household.
The question to be solved is to determine which fuel type of transport we should rely on to promote electric mobility and achieve a ripple effect?

Change Log  -   It is encouraged that, whoever is using the project for their interest can make or update changes in the database for a robust search availability and accessebility. Furthermore, take pleasure in exploring the graphical presentation as per your taste.

Conclusion  - Depending upon the current circumstances and present infrastructures, end users are encouraged to analyse the situation of running cost, energetical mix pertaining to cost of energy, duties applicable on import of fuels, 


Note:   All the data which are in placce in the project are from EU government agencies. There are no consideration of maintenance or consumables, considered equal in the same type of segment. The reserach outcome is formulated in such a way that the analysis done is at a universal level and not specific to a particcular model, size of engine, weight of vehicle, etc...




