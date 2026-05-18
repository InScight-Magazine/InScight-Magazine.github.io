---
author-affiliation:
- Department of Earth Sciences, IISER Kolkata
author-bio: '**Baibhab Karmakar** is a 4th year BS-MS student at IISER Kolkata, pursuing studies in geosciences and computer science under the joint supervision of Prof. Supriyo Mitra and Dr. Arjun Datta. Beyond academics, he is passionate about photography and actively engages in sports, balancing scientific curiosity with creative and athletic pursuits.'
authorImage: baibhav.jpeg
authors:
- Baibhab Karmakar
category: article
date: 2025-11-1
excerpt: The Asian megacities of Kolkata and Dhaka sit atop the sediment-filled expanse of the Bengal Basin, one of world's most densely populated but far from the Great Himalayas. New research focused on the boundary between the ancient Shillong Plateau and the soft, deep sediments of the Bengal Basin has revealed a mechanism for earthquake wave amplification that is so severe it could multiply shake intensity by two to five times in urban areas.
hero-image: baibhav.svg
issue: 8
permalink: /issue8/baibhab-karmakar-hazard/
refs-file: baibhav
reviewed-by:
- Suddhajit Bishayee
- Shibaraj Sahu
- Sushrat Mishra
title: 'Earthquake Amplification in the Bengal Basin: Insights into Basin-Induced Seismic Hazard'
---


The Asian megacities of Kolkata and Dhaka sit atop the sediment-filled expanse of the Bengal Basin, one of the world's most densely populated region but far from the Great Himalayas. For decades, seismic hazard assessments have focused heavily on major fault lines and rupture zones, but a critical, often underestimated factor is now demanding attention– the ground itself.

New research focused on the boundary between the ancient, rigid Shillong Plateau and the soft, deep sediments of the Bengal Basin has revealed a mechanism for earthquake wave amplification that is so severe it could multiply shake intensity by two to five times in urban areas. This work highlights a global imperative to move beyond simplified velocity models and account for the complex interaction between earthquake waves and the heterogeneous, soft subsurface.

{% include figure.html image='baibhav1.jpg' caption='Topographic and seismotectonic map of our study area' width=800 %}

 

## Understanding Seismic Wave Amplification in the Bengal Basin

The world of seismology is rich with complexities, especially in regions where geological structure strongly controls how seismic waves travel and evolve. This is particularly true in the Bengal Basin, where thick sedimentary layers [1] overlying transitional crust can significantly modify ground motion, making seismic hazard assessment more challenging. In such settings, soft, loose, and water-saturated sediments can amplify shaking, prolong wave trains, and in some cases enhance damage through secondary effects like liquefaction. Historical earthquakes from the broader eastern India–Himalaya–NE India region provide striking examples of how this can play out in practice: the 1934 Bihar–Nepal earthquake (Mw  8.1) is often cited for severe destruction patterns that were influenced not only by the rupture itself but also by the amplification of shaking in sediment-filled basins and plains, helping illustrate how distant earthquakes can still produce disproportionately strong impacts in soft-ground regions (bhookampan.co.in). Similarly, the 1897 Shillong earthquake (Mw  8.1) caused widespread shaking across northeastern and eastern India, with later reports and hazard documents noting that alluvial and deltaic deposits—such as those beneath Kolkata and surrounding areas—can intensify ground motion compared to hard rock (wbdmd.gov.in; cires1.colorado.edu). Further, large events like the 1950 Assam–Tibet earthquake (Mw  8.6–8.7) demonstrate how unconsolidated, saturated sediments can contribute to destructive ground failures, including sand blows and lateral spreading—mechanisms that are especially relevant for thick sedimentary basins such as the Bengal delta system (sciencedirect.com). For readers eager to explore these dynamics in depth, our analysis of the Bengal Basin highlights how sedimentary architecture and local site conditions can strongly shape seismic wave behaviour—and ultimately influence seismic risk across the region.

{% include figure.html image='baibhav2.svg' caption='Conceptual diagram illustrating seismic wave amplification as waves propagate from bedrock into soft surface soils, producing stronger ground shaking at the surface and higher impact on buildings.' width=800 %}

 

## The Geophysical Context

At the heart of our study lies the interaction between surface waves and geological structures. The Bengal Basin is known for its considerable sedimentary deposits, which contrast sharply with the more stable crystalline rocks of the Shillong Plateau. In between these contrasting geological structures the Dauki Fault is present, which acts as a discontinuity between them. This transition creates conditions conducive to the amplification of seismic surface waves, a critical factor that can influence the intensity of seismic shaking during earthquakes [2].

When seismic surface waves travel from the dense, rigid terrain of the Shillong Plateau into the softer, sediment-filled valleys of the Bengal Basin, several factors come into play. Primarily, the lower shear-wave velocities intrinsic to the sediments and the impedance differences across the boundary of these terrains lead to significant surface wave amplification [2]. From an energy-conservation viewpoint, the seismic wave carries energy (energy flux) as it propagates. When it enters soft sediments, the wave speed drops sharply; to transmit nearly the same energy across this slower medium, the particle motion must increase; so the ground oscillates with larger amplitude. In addition, the impedance contrast at the bedrock–sediment boundary causes partial reflections, trapping energy inside the sediment layer and further enhancing shaking through resonance. This phenomenon is crucial for understanding the potential seismic hazards faced by nearby urban centres, which often occupy these sedimentary basins.

## A Tectonic Fault Line: Hard Rock Meets Soft Sediment

The danger zone lies along a stark geological transition. To the north, the Shillong Plateau is composed of crystalline bedrock, a dense, high-velocity crustal block [5] that serves as a relatively stable foundation. In stark contrast, the adjacent Bengal Basin is a colossal bowl of earth, filled with thick layers of Cenozoic and Quaternary sediments; silt, sand, and clay; deposited by the mighty Ganga and Brahmaputra River systems over millions of years[1].

The key scientific problem, and the source of the amplified shaking, is the impedance contrast at the boundary where these two terrains meet. Seismic waves travel through hard, crystalline rock (like the Shillong Plateau) quickly. When these waves encounter the much softer, lower-density sediments of the Bengal Basin, they behave like a fast car hitting a patch of deep mud: they slow down drastically.

This sharp change in velocity, specifically the lower shear-wave velocities (Vs) in the basin sediments, causes the seismic energy to be concentrated and amplified. In addition, several other mechanisms can further enhance seismic wave amplification in sedimentary basins, including (i) resonance effects when the incoming wave frequency matches the natural frequency of the sediment column, (ii) basin geometry and edge effects, where waves are reflected and focused within the basin, leading to localized “hot spots” of stronger shaking, and (iii) wave trapping and multiple reflections between the sediment-bedrock interface and the free surface, which can prolong shaking duration and increase surface motion. This effect is particularly pronounced for surface waves, which travel along the Earth's surface and carry a majority of the destructive energy, especially at lower frequencies.

## Methodology: Shear Velocity Profiles and Modeling Techniques

To analyse the challenges posed by seismic amplification in this region, we employed a comprehensive approach using one-dimensional shear velocity profiles derived from various sites within the Bengal Basin and its adjacent crystalline terrains. Our study employed two main modeling approaches: semi-analytical simulations of surface wave propagation using SWRT (Surface Wave Reflection and Transmission) [4], and full waveform modeling with SPECFEM2D [5]. The outcomes from both methods were then compared with real seismic observation dataset to validate the results.

{% include figure.html image='baibhav3.svg' caption='Workflow for surface-wave amplification analysis showing the main steps: development of 1D shear-wave velocity (Vs) profiles, SWRT-based modeling, and numerical validation using SPECFEM2D simulations' width=800 %}

The first computational method used was SWRT. This technique is semi-analytical, meaning it uses simplified mathematical equations to model how surface waves propagate across a sharp, vertical boundary—the kind that separates the Shillong Plateau from the Bengal Basin.

A crucial capability of SWRT is its ability to explicitly incorporate mode conversion, i.e., the process in which seismic wave energy is redistributed into different wave modes when it encounters a strong contrast in subsurface properties. As a surface wave (such as a fundamental Rayleigh or Love wave) reaches a boundary, it cannot continue in the same form entirely; instead, part of its energy is transferred into other modes, often generating higher-mode surface waves that propagate differently through the layered basin sediments. This mechanism of energy conversion helps trap seismic energy and redistribute it within the basin, contributing to the overall amplification.

The SWRT results were then validated using SPECFEM2D, a more computationally intensive full waveform simulation tool. SPECFEM2D solves the complete elastic wave equation, providing a highly accurate, dynamic picture of how the entire seismic wavefield interacts with the two-dimensional geological structure. By showing where the energy goes, SPECFEM2D essentially acts as a high-fidelity 'virtual seismograph' to confirm the predictions of the more simplified SWRT model.

{% include figure.html image='baibhav4.svg' caption='S-wave Velocity Profiles. This figure shows the S-wave (shear-wave) velocity variation with depth for two distinct regions: Medium 1 representing the Shillong area, and Medium 2 representing the Agartala area.' width=800 %}

 

## The Terrifying Forecast: Two to Five Times Higher Amplitudes

The predictions from both independent modeling techniques were starkly consistent: Both SWRT and SPECFEM2D predict 2-5 times higher amplitudes in the Bengal Basin sediments than in the adjacent crystalline terrain.

This significant amplification occurs across a crucial frequency band: 0.01-0.15 Hz. This low-frequency range is particularly dangerous because it corresponds to the natural resonant frequencies of tall structures like high-rise buildings and bridges [6]. The amplified shaking at these frequencies can drive buildings into destructive resonance, magnifying structural damage far beyond what would be expected based solely on the earthquake's magnitude.

## Confirmation from the Earth

Crucially, these computational predictions were not just theoretical. We compared their calculations to observations from a regional earthquake recorded at actual seismic stations located on both the plateau and the basin. The analysis revealed that the observed amplification, particularly in the transverse component of the ground motion, showed good agreement with the model predictions. This observed match confirms that the combined effects of the low shear-wave velocity [7] and mode conversion at the lateral discontinuity are evident and must be integrated into future hazard models.

## Future Directions and Importance of the Study

{% include figure.html image='baibhav5.svg' caption='Predicted amplification of love wave for different modes using SWRT.' width=800 %}

 Our study is just the beginning. We are committed to expanding our research by analysing a more extensive dataset, focusing on both the vertical and radial components of seismic waves. By further refining our understanding of wave propagation in this dynamic environment, we hope to develop more robust models for predicting seismic hazards in megacities situated on complex sedimentary basins.

The implications of our findings are immense; not only for the affected regions but also for the global community. As urban populations continue to grow and megacities emerge in geologically diverse areas, understanding the effects of lateral heterogeneities and sedimentary basins becomes paramount. Building resilience in these urban structures requires meticulous seismic hazard assessments informed by accurate geophysical models.

## Conclusion

For science enthusiasts, the exploration of the Bengal Basin serves as a fascinating case study of how geological structures can mediate seismic risks in urban contexts. By understanding wave amplification, we help improve seismic hazard assessment and reduce earthquake risk for communities living in vulnerable sedimentary regions. As our research progresses, we invite continued engagement and curiosity from both academic and public spheres as we strive to enhance our understanding of seismic dynamics in sedimentary basins around the globe. {% include figure.html image='baibhav6.png' caption='Frequency-dependent transmission ratio of Rayleigh waves comparing the raw observed trend with SWRT-based predictions. Smoothed curves (moving average/LOWESS) highlight the overall amplification pattern, while the sum of all SWRT modes is compared against the SPECFEM transmission ratio to evaluate the model’s agreement with numerical observations.' width=800 %}

 