---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Current position
======
* **Senior Researcher and Director, UAV Icing Lab** – Norwegian University of Science and Technology (NTNU), Department of Engineering Cybernetics, Trondheim, Norway
* **Lead aerodynamics engineer and shareholder** – UBIQ Aerospace, Trondheim, Norway

Education
======
* **PhD**, Engineering Cybernetics, Norwegian University of Science and Technology (NTNU), 2020
  * Thesis: *Atmospheric Ice Accretions, Aerodynamic Icing Penalties, and Ice Protection Systems on Unmanned Aerial Vehicles* (NTNU 2020:200)
* **Dipl.-Ing. Aerospace Engineering**, University of Stuttgart, Germany, 2013 (graduated with distinction)
  * Diplomarbeit: *Aeroakustische Analyse vereister Profile einer Windenergieanlage*
  * Studienarbeit (2012): *Thermische Untersuchung der Eisbildung und des Anti-Icings an einem Rotorblatt für Windenergieanlagen*

Professional experience
======
* **NTNU**, Department of Engineering Cybernetics – Senior Researcher and Director of the UAV Icing Lab; previously postdoctoral researcher (2020–) and PhD candidate (2016–2020) within NTNU AMOS and CIRFA
* **SIOS – Svalbard Integrated Arctic Earth Observing System**, Longyearbyen – Secondment (2024)
* **UBIQ Aerospace**, Trondheim – Lead aerodynamics engineer, development of ice protection systems for UAVs
* **Petroleum industry** – Upstream project engineer (approx. three years, 2013–2016)

Awards and recognition
======
* AIAA 30/30 recipient, Aerospace Sciences category (2026)
* SIOS Early Career Researcher Award (2021)

Research funding
======
{{ site.data.folk.funding_header }} – see [Funding](/funding/)

<ul class="folk-list">
{% for f in site.data.folk.funding %}  <li>{{ f }}</li>
{% endfor %}</ul>

Professional service
======
* Organiser, International UAV Icing Workshop, Trondheim (2022, 2024)
* Guest editor, special issue on UAV icing, *MDPI Drones* (2024–), with E. Villeneuve
* Guest editor, special issue "Atmospheric Measurements Using Unmanned Systems", *MDPI Drones* (2020–2021)
* Member, AIAA Atmospheric and Space Environments Technical Committee
* Member, SAE AC-9C Aircraft Icing Technology Committee (2018–)
* 1st and 2nd AIAA Ice Prediction Workshop (2020–2023)
* Co-chair, NATO AVT-388 Operation of UAVs in Icing Environments (2023–); co-chair, AVT-ET-214 (2020–2022); participant, AVT-299 Assessment of Anti-Icing and De-Icing Technologies (2018–2021)
* Reviewer for several international journals

Skills
======
* CFD for icing: ANSYS FENSAP-ICE, NASA LEWICE
* Icing wind tunnel, wind tunnel and flight testing of UAVs
* Design and optimisation of electrothermal ice protection systems
* Drone-based mapping and photogrammetry in Arctic field conditions
* Atmospheric sampling of persistent organic pollutants

Publications
======
{% include compact-list.html items=site.publications %}
  
Talks
======
{% include compact-list.html items=site.talks %}
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Supervision
======
* 1 postdoc, 9 PhD students and 27 master students – see [People](/people/)
