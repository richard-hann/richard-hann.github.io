# -*- coding: utf-8 -*-
"""Datasets, people, funding and research projects (source: richahan.folk.ntnu.no).
Each entry: (text, link url, linked text). Rebuild with: python3 markdown_generator/build_hann.py
"""
F = "https://folk.ntnu.no/richahan/Publications/"
RF = "https://richahan.folk.ntnu.no/Publications/"
PB = "https://prosjektbanken.forskningsradet.no/project/FORISS/"

DATASETS_HEADER = "Datasets"
DATASETS = [
("Hann, R. (2026). Drone-based glacier mapping of Nordenskiöldbreen and Tunabreen in Svalbard, 2026, Dataset. Zenodo, Version 1. doi.org/10.5281/zenodo.22881363","https://doi.org/10.5281/zenodo.22881363","Drone-based glacier mapping of Nordenskiöldbreen and Tunabreen in Svalbard, 2026"),
("Hann, R. (2026). Scientific Applications of Unmanned Vehicles in Svalbard, Dataset, Zenodo, Version 2. doi.org/10.5281/zenodo.17187542","https://doi.org/10.5281/zenodo.17187542","Scientific Applications of Unmanned Vehicles in Svalbard"),
("Hann, R., Gajek, W., Pearce, D., & Harcourt, W. (2025). Drone-based glacier mapping of Borebreen in Svalbard, 2025, Dataset, DataverseNO, Version 1. doi.org/10.18710/ZAJLVT","https://doi.org/10.18710/ZAJLVT","Drone-based glacier mapping of Borebreen in Svalbard, 2025"),
("Hann, R., Lockhart, K. (2025). Drone-based glacier mapping of Fridtjovbreen, Vallakrabreen, Paulabreen, and Scheelebreen, DataverseNO, Version 1. doi.org/10.18710/GA1FTV","https://doi.org/10.18710/GA1FTV","Drone-based glacier mapping of Fridtjovbreen, Vallakrabreen, Paulabreen, and Scheelebreen"),
("Harcourt, W., Pearce, D., Gajek, W., Lovell, H., Luckman, A., Benn, D., Kohler, J., Kääb, A., Hann, R. (2024). Svalbard Surge Database 2024, Dataset, Zenodo. doi.org/10.5281/zenodo.14229560","https://doi.org/10.5281/zenodo.14229560","Svalbard Surge Database 2024"),
("Hann, R., Gajek, W., Pearce, D., & Harcourt, W. (2024). Drone-based glacier mapping of Borebreen in Svalbard, 2024, Dataset, Zenodo. doi.org/10.5281/zenodo.13837315","https://doi.org/10.5281/zenodo.13837315","Drone-based glacier mapping of Borebreen in Svalbard, 2024"),
("Hann, R., Gajek, W., Pearce, D., & Harcourt, W. (2024). Drone-based geomorphology mapping of Borebreen in Svalbard, 2024, Dataset, Zenodo. doi.org/10.5281/zenodo.13837009","https://doi.org/10.5281/zenodo.13837009","Drone-based geomorphology mapping of Borebreen in Svalbard, 2024"),
("Hann, R. (2024). Drone-based mapping of surging glaciers in Rindersbukta, Svalbard, DataverseNO, Version 2. doi.org/10.18710/IBBSGD","https://doi.org/10.18710/IBBSGD","Drone-based mapping of surging glaciers in Rindersbukta, Svalbard"),
("Hann, R. (2024). Drone-based glacier mapping of Nordenskiöldbreen and Tunabreen in Svalbard, 2024, Dataset. Zenodo, Version 1. doi.org/10.5281/zenodo.13623723","https://doi.org/10.5281/zenodo.13623723","Drone-based glacier mapping of Nordenskiöldbreen and Tunabreen in Svalbard, 2024"),
("Hann, R., Rhodes, N., Gajek, W., Pearce, D., Harcourt, W. (2024). Drone-based mapping of calving rates of Borebreen in Svalbard, DataverseNO, Version 1. doi.org/10.18710/B553MB","https://doi.org/10.18710/B553MB","Drone-based mapping of calving rates of Borebreen in Svalbard"),
("Hann, R., Rinne, E. (2024). Drone-based mapping of Larsbreen, Longyearbreen, and Tellbreen in Svalbard, DataverseNO, Version 1. doi.org/10.18710/L41RKZ","https://doi.org/10.18710/L41RKZ","Drone-based mapping of Larsbreen, Longyearbreen, and Tellbreen in Svalbard"),
("Hann, R. (2023). Drone-based mapping of crevassed glaciers in Svalbard, DataverseNO, Version 1. doi.org/10.18710/KLISS5","https://doi.org/10.18710/KLISS5","Drone-based mapping of crevassed glaciers in Svalbard"),
("Hann, R. (2022). Drone-based mapping of Gruvefjellet in Spring and Summer for cornice risk assessment, DataverseNO, Version 1. doi.org/10.18710/0NO42L","https://doi.org/10.18710/0NO42L","Drone-based mapping of Gruvefjellet in Spring and Summer for cornice risk assessment"),
("Hann, R., Meier, K., Garreau, A. (2022). Validation data for wind speed and wind direction measurements with quadcopter drones, DataverseNO, Version 1. doi.org/10.18710/AFDYLS","https://doi.org/10.18710/AFDYLS","Validation data for wind speed and wind direction measurements with quadcopter drones"),
("Hann, R. (2022). Drone-based mapping of Sassendalen for reindeer counting in Svalbard. DataverseNO, Version 1. doi.org/10.18710/KHQKWH","https://doi.org/10.18710/KHQKWH","Drone-based mapping of Sassendalen for reindeer counting in Svalbard"),
("Hann, R., et al. (2022). Scientific literature that utilizes unmanned vehicles in Svalbard. Svalbard Integrated Arctic Earth Observing System, SIOS.","https://sios-svalbard.org/UAV_Svalbard","Scientific literature that utilizes unmanned vehicles in Svalbard"),
("Hann, R. (2021). Drone-based mapping of the Endalen alluvial fan in Svalbard. DataverseNO, Version 1. doi.org/10.18710/AED5GT","https://doi.org/10.18710/AED5GT","Drone-based mapping of the Endalen alluvial fan in Svalbard"),
("Hann, R. (2021). Aerodynamic roughness length of crevassed tidewater glaciers from UAV mapping in Svalbard. DataverseNO, Version 1. doi.org/10.18710/JMWF3E","https://doi.org/10.18710/JMWF3E","Aerodynamic roughness length of crevassed tidewater glaciers from UAV mapping in Svalbard"),
("Hann, R. (2021). Drone-based mapping of the Lagoon Pingo in Svalbard. DataverseNO, Version 1. doi.org/10.18710/IMPEG8","https://doi.org/10.18710/IMPEG8","Drone-based mapping of the Lagoon Pingo in Svalbard"),
("Hann, R., Müller, N. (2020). Icing Validation Database. DataverseNO, Version 1. doi.org/10.18710/5XYALW","https://doi.org/10.18710/5XYALW","Icing Validation Database"),
("Hann, R., Wallisch, J. (2020). UAV Specification Database. DataverseNO, Version 1. doi.org/10.18710/L41IGQ","https://doi.org/10.18710/L41IGQ","UAV Specification Database"),
]

# People: list of (section title, [(subheading or None, [entries])])
PEOPLE = [
("Postdocs", [(None, [
  ("Bogdan Løw-Hansen, Atmospheric icing detection and system identification for disruptive aircraft, 2026–202X, NTNU, funded by RCN and UBIQ Aerospace.","",""),
])]),
("PhD Students", [("Current", [
  ("Lars Klein, UAV Icing Detection with LiDAR, 2026–2029, NTNU, main supervisor, ongoing.","",""),
  ("Kaelan Lockhart, Real-time vegetation mapping in Antarctica, Queensland University of Technology (QUT), co-supervisor, ongoing.","",""),
  ("Kristoffer Kvist, Helicopter icing, 2024–202X, The Arctic University of Norway (UiT), co-supervisor, ongoing.","",""),
  ("Markus Lindner, Icing performance of UAVs, 2022–202X, NTNU, main supervisor, ongoing.","",""),
  ("Michael Cheung, Path-planning of UAVs in icing conditions, 2021–202X, NTNU, main supervisor, ongoing.","",""),
 ]), ("Completed", [
  ("Bogdan Løw-Hansen, Modeling and Validation of Atmospheric Icing Effects on Small Fixed-Wing UAVs, 2021–2026, NTNU, main supervisor, completed.","https://hdl.handle.net/11250/5533084","Modeling and Validation of Atmospheric Icing Effects on Small Fixed-Wing UAVs"),
  ("Nicolas Müller, Icing, performance penalties, and ice protection systems for UAV propellers, 2021–2026, UBIQ Aerospace / NTNU, main supervisor, completed.","https://hdl.handle.net/11250/5536902","Icing, performance penalties, and ice protection systems for UAV propellers"),
  ("Joachim Wallisch, Reducing Energy Consumption of UAVs in Icing Conditions with Active Electrothermal De-Icing Ice Protection Systems, 2021–2026, NTNU, main supervisor, completed.","https://hdl.handle.net/11250/5534819","Reducing Energy Consumption of UAVs in Icing Conditions with Active Electrothermal De-Icing Ice Protection Systems"),
  ("Mauro Ghirardelli, SAMURAI - Development, Test and Validation of an Airborne Sonic Anemometer, 2021–2024, University of Bergen (UiB), co-supervisor, completed.","https://bora.uib.no/bora-xmlui/handle/11250/3170691","SAMURAI - Development, Test and Validation of an Airborne Sonic Anemometer"),
 ])]),
("Master Students", [("Current", [
  ("Knut Olav Nordgarden Kragh, Duo Drone, NTNU, main supervisor, 2026.","",""),
  ("Jonas Kalkenberg Guttormsen, Path planning, NTNU, co-supervisor.","",""),
 ]), ("Completed", [
  ("Modest Röhl, On the Redesign and Characterization of a Small-Scale Icing Wind Tunnel Using Experimental and Numerical Methods, UBIQ Aerospace / Uni Stuttgart, 2025, main supervisor.",RF+"2025_R%c3%b6hl_Thesis.pdf","On the Redesign and Characterization of a Small-Scale Icing Wind Tunnel Using Experimental and Numerical Methods"),
  ("Noel Ernsting, Icing on Airborne Wind Energy, NTNU / Uni Stuttgart, 2025, main supervisor.",RF+"2025_Ernstig_Thesis.pdf","Icing on Airborne Wind Energy"),
  ("Jakob Röß, Experimental and Numerical Investigation on Aerodynamic Performance Degradation on an UAV Airfoil, NTNU / Uni Stuttgart, 2024/25, co-supervisor.",RF+"2025_R%c3%b6%c3%9f_Thesis.pdf","Experimental and Numerical Investigation on Aerodynamic Performance Degradation on an UAV Airfoil"),
  ("Michael Henzler, CFD Simulation of Icing on a Flying-Wing UAV, NTNU / Uni Stuttgart, 2023/24, main supervisor.",F+"2024_Henzler_Thesis.pdf","CFD Simulation of Icing on a Flying-Wing UAV"),
  ("Samuel Göhring, Development of a Photogrammetry Method to Digitize Ice Shapes on UAVs, NTNU / Uni Stuttgart, 2023/24, main supervisor.",F+"2024_Goehring_Thesis.pdf","Development of a Photogrammetry Method to Digitize Ice Shapes on UAVs"),
  ("Markus Frey, Numerical investigation of heat transfer on propeller ice protection systems for unmanned aerial vehicles, 2023, NTNU / Uni Stuttgart, main supervisor.",F+"2023_Frey_Thesis.pdf","Numerical investigation of heat transfer on propeller ice protection systems for unmanned aerial vehicles"),
  ("Lukas Wurst, CFD icing simulations on a fixed-wing UAV engine inlet, 2022/23, NTNU / Uni Stuttgart, main supervisor.",F+"2023_Wurst_Thesis.pdf","CFD icing simulations on a fixed-wing UAV engine inlet"),
  ("Henidya Heramarwan, CFD Icing Simulations on Rotors for eVTOL Unmanned Aircraft, 2022/23, NTNU / Uni Stuttgart, main supervisor.",F+"2023_Heramarwan_Thesis.pdf","CFD Icing Simulations on Rotors for eVTOL Unmanned Aircraft"),
  ("Stephan Van Reen, CFD Simulation of the Air Flow Field around a Ship, 2022, NTNU / UNIS / Aalto, main supervisor.",F+"2022_van_Reen_Thesis.pdf","CFD Simulation of the Air Flow Field around a Ship"),
  ("Bogdan Løw-Hansen, Electrothermal Ice-Shedding Detection for UAVs, 2021, NTNU, supporting supervisor.","https://ntnuopen.ntnu.no/ntnu-xmlui/handle/11250/2781079","Electrothermal Ice-Shedding Detection for UAVs"),
  ("Michael Cheung, An energy consumption model for UAVs in icing conditions, 2021, NTNU, main supervisor.",F+"2021_Cheung_Thesis.pdf","An energy consumption model for UAVs in icing conditions"),
  ("Kilian Meier, Wind Estimation with multirotor UAVs, master thesis, 2021, UNIS / École Polytechnique Fédérale de Lausanne, main supervisor.",F+"2021_Meier_Thesis.pdf","Wind Estimation with multirotor UAVs"),
  ("Ruben Kleiven, Robust and Gain Scheduled Flight Control of Fixed-wing UAVs in Wind and Icing Conditions, master thesis, 2021, NTNU, supporting supervisor.","https://ntnuopen.ntnu.no/ntnu-xmlui/handle/11250/2781074","Robust and Gain Scheduled Flight Control of Fixed-wing UAVs in Wind and Icing Conditions"),
  ("Johannes Oswald, UAV Icing: Numerical and Experimental Study of Performance Penalties on an RG-15 Airfoil, master thesis, 2020/21, Uni Stuttgart / von Karman Institute / NTNU, main supervisor.",F+"2021_Oswald_Thesis.pdf","UAV Icing: Numerical and Experimental Study of Performance Penalties on an RG-15 Airfoil"),
  ("Max Nüßle, Heat Transfer Simulations of Crevassed Glaciers, master thesis, 2020/21, Uni Stuttgart / UNIS / NTNU, main supervisor.",F+"2021_Nuessle_Thesis.pdf","Heat Transfer Simulations of Crevassed Glaciers"),
  ("Mikkel Tiller, Advanced path planning for UAVs in icing conditions, master thesis, 2020/21, NTNU, co-supervisor.","https://ntnuopen.ntnu.no/ntnu-xmlui/handle/11250/2786767","Advanced path planning for UAVs in icing conditions"),
  ("Nicolas Müller, Numerical simulation of the ice accretion on a propeller of a small fixed-wing UAV, master thesis, 2020, NTNU / Uni Stuttgart, main supervisor.",F+"2020_M%C3%BCller_Thesis.pdf","Numerical simulation of the ice accretion on a propeller of a small fixed-wing UAV"),
  ("Armin Dachauer, Aerodynamic Roughness Length of Crevassed Tidewater Glaciers from UAV Mapping, master thesis, 2020, UNIS / ETH Zürich, main supervisor.",F+"2020_Dachauer_Thesis.pdf","Aerodynamic Roughness Length of Crevassed Tidewater Glaciers from UAV Mapping"),
  ("Arthur Garreau, Validation and Application of Novel Wind Estimation Methods with Quadcopter UAVs in the Arctic, master thesis, 2020, UNIS / École nationale de la météorologie (ENM), main supervisor.",F+"2020_Garreau_Thesis.pdf","Validation and Application of Novel Wind Estimation Methods with Quadcopter UAVs in the Arctic"),
  ("Edvard Frimann Løes Narum, Mission planning for fixed-wing UAVs in wind and icing conditions, master thesis, 2020, NTNU, co-supervisor.",F+"2020_Narum_thesis.pdf","Mission planning for fixed-wing UAVs in wind and icing conditions"),
  ("Joachim Wallisch, Design of a low-speed icing wind tunnel for UAVs, master thesis, 2020, NTNU / Uni Stuttgart, main supervisor.",F+"2020_Wallisch_Thesis.pdf","Design of a low-speed icing wind tunnel for UAVs"),
  ("Nicolas Fajt, The Influence of Meteorological Conditions on the Icing Performance Penalties on a UAV Airfoil, master thesis, 2019, NTNU / Uni Stuttgart, main supervisor.",F+"2019_Fajt_Thesis.pdf","The Influence of Meteorological Conditions on the Icing Performance Penalties on a UAV Airfoil"),
  ("Adrian Winter, Systems Identification, Flight Performance, and Control of a Fixed-Wing UAV in Icing Conditions, master thesis, 2019, NTNU / Uni Stuttgart, main supervisor.",F+"2019_Winter_Thesis.pdf","Systems Identification, Flight Performance, and Control of a Fixed-Wing UAV in Icing Conditions"),
  ("Julie Krøgenes, Aerodynamic Performance of the NREL S826 Airfoil in Icing Conditions, master thesis, 2017, NTNU, co-supervisor.","http://hdl.handle.net/11250/2454897","Aerodynamic Performance of the NREL S826 Airfoil in Icing Conditions"),
  ("Lovisa Brandrud, Aerodynamic Performance of the NREL S826 Airfoil in Icing Conditions, master thesis, 2017, NTNU, co-supervisor.","http://hdl.handle.net/11250/2454897","Aerodynamic Performance of the NREL S826 Airfoil in Icing Conditions"),
 ])]),
]

FUNDING_HEADER = "16× National: 56.1 MNOK & 4× EU: 2.4 MEUR"
FUNDING = [
("Clean Aviation, HORIZON-JU-CLEAN-AVIATION-2026-04-FTA-01: Development and Demonstration of a Smart, Low-power, Hybrid Ice Protection System for Ultra-Efficient Regional Aircraft (DELIA). 0.5 MEUR (total 5.0 MEUR). Co-principal investigator.","",""),
("Horizon Europe, 2026–2030, HORIZON-INFRA-2025-01-TECH-01: Smart Solutions for Climate/Environment-Neutral Arctic Research Infrastructures (SUSTAIN-ICE). 0.5 MEUR (total 5.0 MEUR). Co-principal investigator.","",""),
("Research Council of Norway, 2026–2029, project number 359116: Industrial PhD on Ice Detection with LiDAR. 4.6 MNOK. Co-principal investigator.",PB+"359116","Industrial PhD on Ice Detection with LiDAR"),
("Research Council of Norway, 2025–2030, project number 357451: Norwegian Centre for Embodied AI (NCEI). 5.0 MNOK (total 200 MNOK). Co-principal investigator.","https://www.ntnu.edu/ncei","Norwegian Centre for Embodied AI (NCEI)"),
("European Defence Fund, 2024–2027, EDF-2023-DA-C4ISR-TRPAS: Advanced capabilities & Certification for Tactical UAV Systems (ACTUS). 0.6 MEUR (total 42.0 MEUR). Co-principal investigator.","https://defence-industry-space.ec.europa.eu/document/download/8817c0c4-dedb-46e2-9d02-30be8da42b24_en?filename=EDF-2023-DA-C4ISR-TRPAS%20ACTUS.pdf","Advanced capabilities & Certification for Tactical UAV Systems (ACTUS)"),
("European Defence Fund, 2023–2026, EDF-2022-LS-RA-SMERO-NT-TDRIC: Tactical Drones in Rain and Icing Conditions (TDRIC). 0.8 MEUR (total 4.0 MEUR). Co-principal investigator.","https://defence-industry-space.ec.europa.eu/system/files/2023-06/TDRIC-Factsheet_EDF22.pdf","Tactical Drones in Rain and Icing Conditions (TDRIC)"),
("Research Council of Norway, 2024–2027, project number 350469: Zero Ice Shield: D•ICE Ice Protection for Aviation's Green Evolution. 9.1 MNOK. Co-principal investigator.",PB+"350469","Zero Ice Shield: D•ICE Ice Protection for Aviation's Green Evolution"),
("Research Council of Norway, 2024, project number 350269: Linking past and present surge dynamics at Borebreen from drone surveys. 80 kNOK. Investigator.",PB+"350269","Linking past and present surge dynamics at Borebreen from drone surveys"),
("Research Council of Norway, 2022–2023, project number 333170: Drone-mapping Surging Glaciers in Svalbard. 50 kNOK. Principal investigator.",PB+"333170","Drone-mapping Surging Glaciers in Svalbard"),
("Research Council of Norway, 2021–2026, project number 316425: Icing effects, detection and mitigation on unmanned aerial vehicles (UAVs). 12.4 MNOK. Co-principal investigator.",PB+"316425","Icing effects, detection and mitigation on unmanned aerial vehicles (UAVs)"),
("Research Council of Norway, 2021–2025, project number 318000: Adverse weather mission planning for unmanned aerial vehicles (UAVs). 14.9 MNOK. Principal investigator.",PB+"318000","Adverse weather mission planning for unmanned aerial vehicles (UAVs)"),
("Research Council of Norway, 2021–2024, project number 321667: Industrial PhD on Propeller Icing on Unmanned Aerial Vehicles. 2.5 MNOK. Principal investigator.",PB+"321667","Industrial PhD on Propeller Icing on Unmanned Aerial Vehicles"),
("Research Council of Norway, 2020, project number 310702: Validation and Application of Novel Wind Estimation Techniques with UAVs in the Arctic. 29 kNOK. Co-principal investigator.",PB+"310702","Validation and Application of Novel Wind Estimation Techniques with UAVs in the Arctic"),
("Research Council of Norway, 2019–2022, project number 296228: Autonomous icing protection solution for unmanned aircraft rotors. 6.4 MNOK. Post-doc.",PB+"296228","Autonomous icing protection solution for unmanned aircraft rotors"),
("Research Council of Norway, 2019–2020, project number 296355: Using UAVs to investigate effects of crevasses upon glacier surface melting. 78 kNOK. Principal investigator.",PB+"296355","Using UAVs to investigate effects of crevasses upon glacier surface melting"),
("Svalbard Integrated Arctic Earth Observing System, 2024, SESS Report 2024: Surging glaciers in Svalbard: Current knowledge and perspectives for monitoring. 200 kNOK. Principal investigator.","https://sios-svalbard.org/SESS_Issue7","Surging glaciers in Svalbard: Current knowledge and perspectives for monitoring"),
("Svalbard Integrated Arctic Earth Observing System, 2023, Access Call: Drivers of surge activation at Borebreen. 200 kNOK. Investigator.","https://sios-svalbard.org/BorebreenSurge","Drivers of surge activation at Borebreen"),
("Svalbard Integrated Arctic Earth Observing System, 2022, SESS Report 2022: Practical Guidelines for Scientific Application of Uncrewed Aerial Vehicles in Svalbard. 200 kNOK. Principal investigator.","https://sios-svalbard.org/SESS_Issue5","Practical Guidelines for Scientific Application of Uncrewed Aerial Vehicles in Svalbard"),
("Svalbard Integrated Arctic Earth Observing System, 2021, SESS Report 2021: Update to Scientific Applications of Unmanned Vehicles in Svalbard. 70 kNOK. Principal investigator.","https://sios-svalbard.org/SESS_Issue4","Update to Scientific Applications of Unmanned Vehicles in Svalbard"),
("Svalbard Integrated Arctic Earth Observing System, 2020, SESS Report 2020: Scientific Applications of Unmanned Vehicles in Svalbard. 240 kNOK. Principal investigator.","https://sios-svalbard.org/SESS_Issue3","Scientific Applications of Unmanned Vehicles in Svalbard"),
]

PROJECTS = [
("Icing effects, detection and mitigation on unmanned aerial vehicles (UAVs). Funded by the Research Council of Norway (IKTPLUSS). 2020 – today.","",""),
("Center of Excellence, Autonomous Marine Operations and Systems (AMOS). Funded by the Research Council of Norway, NTNU, Equinor, DNV GL and the Sintef Group. 2016 – 2023.","http://www.ntnu.edu/amos","AMOS"),
("NTNU Unmanned Aerial Vehicles Laboratory (UAV-lab). 2016 – today.","http://www.itk.ntnu.no/english/lab/unmanned","UAV-lab"),
("NTNU Unmanned Aerial Vehicles Icing Laboratory (UAV Icing Lab). 2021 – today.","https://www.uavicinglab.com/","UAV Icing Lab"),
("UAV Crevasse – Using UAVs to investigate effects of crevasses upon glacier surface melting (RIS-ID 11148). 2019 – 2022.","https://www.researchinsvalbard.no/project/9044","RIS-ID 11148"),
("Arctic ABL Wind – Novel method for wind measurements in the arctic atmospheric boundary layer (RIS-ID 11372). 2020 – 2021.","https://www.researchinsvalbard.no/project/9389","RIS-ID 11372"),
("2nd AIAA Ice Prediction Workshop (IPW). 2022 – 2023.","http://folk.ntnu.no/richahan/IPW/","IPW"),
("1st AIAA Ice Prediction Workshop (IPW). 2020 – 2021.","http://folk.ntnu.no/richahan/IPW/","IPW"),
("D•ICE ROTORS – Protecting the unmanned aircraft industry, funded by Research Council of Norway (BIA) and UBIQ Aerospace. 2019 – 2022.","https://www.ubiqaerospace.com/","UBIQ Aerospace"),
("Centre for integrated remote sensing and forecasting for arctic operations (CIRFA). 2016 – 2020.","http://cirfa.uit.no/","CIRFA"),
("NATO AVT-388 – Operation of Unmanned Aerial Vehicles (UAVs) in Icing Environments. Co-chair. 2023 – today.","",""),
("NATO AVT-ET-214 – Operation of Unmanned Aerial Vehicles (UAVs) in Icing Environments. Co-chair. 2020 – 2022.","",""),
("NATO AVT-299 – Assessment of Anti-Icing and De-Icing Technologies for Air and Sea Vehicles. Participant. 2018 – 2021.","",""),
]
