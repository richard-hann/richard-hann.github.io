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

Academic engagement & workgroups
======
<ul class="folk-list">
{% for e in site.data.folk.engagement %}  <li>{{ e }}</li>
{% endfor %}</ul>

Research projects
======
<ul class="folk-list">
{% for p in site.data.folk.projects %}  <li>{{ p }}</li>
{% endfor %}</ul>

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
<ul class="folk-list">
{% for t in site.data.folk.teaching %}  <li>{{ t }}</li>
{% endfor %}</ul>
  
Supervision
======
* 1 postdoc, 9 PhD students and 27 master students – see [People](/people/)
