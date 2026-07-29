---
author-affiliation:
- Post Doctoral Fellow, Ashoka University, Sonepat
- Professor at Ashoka University Sonepat, Former Director and Honorary Professor at IISER Kolkata
author-bio: '**Dr Anu Arora** is a postdoctoral researcher at Ashoka University, Sonepat, and she works with Prof. Sourav Pal. Her research interests include computational quantum material science, particularly first-principle studies of spin-polarised phenomena and their applications in spintronics, quantum materials and energy conversion applications.


  **Prof. Sourav Pal** is a leading theoretical and computational chemist, right now serving as Head of the Chemistry Department at Ashoka University, Sonepat. His work focuses on the development of new methodologies and conceptual frameworks in many-body electronic structure theory, density-based approaches to chemical reactivity, along with the investigation of catalytic as well as hydrogen storage materials, through computational material science. '
authorImage: sourav.png
authors:
- Anu Arora
- Sourav Pal
category: article
date: 2026-4-29
excerpt: "What if the electron never truly orbited the nucleus, not because its path was too small to be observed, but because the very idea of a definite path was the wrong question? A century ago, quantum mechanics forced science to forsake the familiar language of classical motion and rethink how nature itself should be described. This article traces the remarkable journey- from Heisenberg\u2019s rejection of electron orbits to the quantum theories of chemical bonding, electron correlation, and modern computational science, revealing how one conceptual revolution transformed our understanding of atoms, molecules and materials."
hero-image: sourav2.svg
issue: 9
permalink: /issue9/anu-arora-science/
refs-file: sourav
reviewed-by:
- Archita Sarkar
- Dishari Dasgupta
title: "Quantum at 100: From Heisenberg\u2019s Revolution to Modern Science"
---


> What we observe is not nature itself, but nature exposed to our method of questioning. _— Werner Heisenberg_

## The Birth of New Science (1925)

At the beginning of the 20th century, classical physics, comprising Newtonian mechanics and Maxwell’s electrodynamics, was regarded as a nearly complete theoretical framework. The two pillars of physics seemed complete until experimental observations at microscopic scales revealed their limitations.

One of the earliest inconsistencies arose with the failure of blackbody radiation. According to the classical theory, Rayleigh–Jeans law, the emitted energy would diverge at high frequencies, becoming infinitely large, resulting in the ultraviolet catastrophe [1]. To overcome this problem, Max Planck proposed in 1900 that electromagnetic radiation is exchanged in discrete energy packets, or quanta, with energy [2] 

$$E = h\nu.$$

 Shortly thereafter, Albert Einstein extended this concept to light, explaining the photoelectric effect by introducing light quanta (photons), thereby establishing the particle nature of electromagnetic radiation [3].

Despite these successes, the structure of the atom remained partially understood. The Bohr–Sommerfeld model (1913–1916) introduced a semi-classical picture in which electrons occupy discrete orbits around the nucleus [4] and transition between them via quantised angular-momentum conditions, 

$$\int pdq = nh/2\pi,$$

 [5] $$(n = 1,2,3\ldots)$$. While this model successfully explained the hydrogen spectrum, it could not accurately describe fine spectral properties like anomalous Zeeman effect [6], Stark splitting [7], or transition intensities, indicating the absence of a theoretical foundation.

A major turning point occurred in 1925, when Werner Heisenberg rejected the classical idea that electrons move along well-defined trajectories around the nucleus. Instead, he argued that the atomic theory should be constructed entirely from quantities that can be experimentally observed. In his correspondence with Wolfgang Pauli, Heisenberg criticised the orbital picture of electrons and proposed that atomic behaviour should be described using measurable spectroscopic quantities such as transition frequencies and spectral intensities. Expressing his discontent with classical orbitals, Heisenberg explicitly stated: 

> All of my pitiful efforts are directed at completely killing off the concept of orbits, which, after all, cannot be observed, and replacing it with something more suitable.

In this new approach, physical quantities were represented through a transition between quantum states rather than through a definite electron path. The central aspect of the new formalism was that the ordering of operators is essential, such that $$xy \neq yx$$ [8-9]. The formalism was later extended into matrix multiplication by Max Born and Pascual Jordan, who represented physical observables as matrices acting on quantum states. This new theory successfully explained atomic spectra, including discrete energy levels and transition rules.

Although quantum mechanics initially emerged to explain atomic phenomena, it soon developed into a broader framework for understanding systems across multiple length scales, ranging from electrons to molecules to material and biological systems.

{% include figure.html image='images/sourav-1.svg' caption='Timeline of key milestones in quantum mechanics and computational chemistry, from Max Planck’s radiation quanta to modern approaches including Density Functional Theory and advanced post-Hartree–Fock approaches for atomic and molecular systems.' width=800 %}

 

## From Orbits to Bonds: Birth of Quantum Chemistry (1927)

 With quantum mechanics, chemists had a new question: _how do atoms combine and form stable molecules?_

Before the 1920s, the bonding was described through empirical valence rules and structural observations, without a rigorous microscopic explanation. There was no microscopic explanation for why two hydrogen atoms form a stable molecule. In 1927, Walter Heitler and Fritz London presented their study on H2 [12] using the wave mechanics introduced by Erwin Schrödinger. The electronic behaviour of the molecules is governed by the time-independent Schrödinger equation 

$$H\Psi = E\Psi,$$

 where $$H$$ is the Hamiltonian operator, $$\Psi$$ is a two-electron wavefunction, and $$E$$ is the corresponding energy eigenvalue. For the hydrogen molecule, the full molecular Hamiltonian in atomic units ($$ħ = m_{e} = e = 1$$) takes the form: 

$$\hat{H} = - \frac{1}{2}\nabla_{1}^{2} - \frac{1}{2}\nabla_{2}^{2} - \left( \frac{1}{r_{1A}} + \frac{1}{r_{1B}} + \frac{1}{r_{2A}} + \frac{1}{r_{2B}} \right) + \left( \frac{1}{r_{12}} + \frac{1}{r_{AB}} \right)$$

 where $$\nabla_{1}^{2}$$ and $$\nabla_{2}^{2}$$ are the Laplacian operators representing the kinetic energy of electrons 1 and 2, respectively, $$r_{1A}$$, $$r_{1B}$$, $$r_{2A}$$ and $$r_{2B}$$ denote the distances of each electron from nuclei A and B, $$r_{12}$$ is the interelectronic distance, and $$R_{AB}$$ is the internuclear separation. The first two terms are kinetic energy, the next four terms are electron-nuclear attraction, and the last two terms are electron-electron and nuclear-nuclear repulsion,

As atoms come close together, their electronic wave functions interact and mix. Because electrons are indistinguishable fermions, the total electronic wavefunction must satisfy the antisymmetric condition imposed by the Pauli exclusion Principle. This produces two distinct arrangements:


+ **Bonding state (symmetric spatial part, spin singlet)**: the overlap of electronic wavefunctions increases electron density in the region between the nuclei. This lowers the total energy and stabilises the molecule.


+ **Antibonding state (antisymmetric spatial part, spin triplet)**: the overlap generates a nodal region between the nuclei, decreasing electron density in the internuclear region. As a result, the energy increases and the molecular configuration become unstable.

The energy lowering in the bonding state comes from the quantum mechanical exchange effect, a direct consequence of anti-symmetrisation of the wavefunction. This was the first quantum mechanical explanation of the covalent bond, and it became the basis of Valence Bond Theory, making the shift from qualitative valence rules to quantitative solutions of the Schrödinger equation.

## Solving the Molecular Problem: The Born–Oppenheimer Approximation (1927)

Understanding bonding in principle was one part. Solving the Schrödinger equation for real molecules, with all electrons and all nuclei interacting simultaneously, remained a serious challenge. Born and Oppenheimer introduced a powerful simplification based on physical observation. The nuclei are approximately $$10^{3} - 10^{4}$$ times heavier than electrons. This means electrons respond almost instantaneously to any nuclear motion, while nuclei move on a much smaller timescale. The two motions are nearly decoupled.

This approximation enables the total molecular wavefunction to be separated into two simpler parts: one associated with electronic motion and the other describing the nuclear motion.


+ **Electronic part**: Solve for electrons in a fixed nuclear framework to obtain $$E_{e}(R)$$.


+ **Nuclear part**: Use $$E_{e}(R)$$ as an effective potential governing nuclear motion.

This separation is the foundation on which quantum chemistry is built. It converts an intractable coupled problem to a manageable sequence of calculations.

## The Hartree–Fock Method and the "Mean-Field" Approximation

Even after fixing the nuclear positions within the Born-Oppenheimer approximation, the resulting electronic problem remains highly nontrivial. The motion of one electron is inherently coupled to that of all others through Coulombic interactions, making the many-electron Schrödinger equation intractable. To render the problem, approximate methods must be employed, of which Hartree-Fock (HF) is among the most foundational. The HF method was developed by Hartree in 1927-1928 and rigorously reformulated by Fock and Slater in 1930 [14-15].

The central idea of the theory is based on a simple assumption that, instead of explicitly treating the instantaneous interaction of every electron with all other electrons, each electron is expected to move independently within a mean field generated by the remaining electrons. Under this approximation, the many-electron Schrödinger equation is transformed into a set of coupled single-electron equations that can be solved self-consistently.

In the HF framework, the N-electron wavefunction is expressed as a Slater determinant[16], a determinant of a matrix of single-electron orbitals. This construction automatically satisfies the antisymmetry property, i.e. swapping any two rows of a determinant flips its sign. This enforces the Pauli exclusion principle.

The resulting HF equations are then solved using an iterative method in which an initial guess for the electronic density is made, from which an effective potential is constructed. Then the resulting equations are solved for new orbitals, and this procedure is repeated until self-consistency is reached.

HF treats electron-electron repulsion on average. But the real electrons correlate; when one electron is at a given position, the other instantaneously avoids it. This dynamical correlation is completely absent from HF theory because the wavefunction is restricted to a single Slater determinant [16]. Thus, the method systematically overestimates the electronic ground-state energy. The missing contribution is called correlation energy, and recovering this energy became the motivation for developing more advanced quantum chemistry methods.

## Electron Correlation and Beyond Hartree-Fock (1960)

From 1960 onwards, the central challenge of quantum chemistry became recovering electron correlation, the instantaneous correlation motion, the correlated motion of electrons that HF misses. Two broad families of methods emerged: wavefunction (which work directly with $$\Psi$$) based approaches and density-based approaches (which work with $$\rho(r)$$)

## Density Functional Theory

Density Functional Theory (DFT) is one of the most widely used theoretical frameworks in modern computational chemistry, material science and solid-state physics. This fundamental principle was first formulated by Pierre Hohenberg and Walter Kohn [17]. Its central insight is both simple and non-obvious. The complete information about the ground state of many-electron systems, including its energy and other properties, is fully encoded in the electron density $$\rho(r)$$, which depends only on 3D position coordinates in space. So, in principle, there is no need of 3N dimensional wavefunction. Hohenberg-Kohn proved that the functional $$E\lbrack\rho\rbrack$$ exists but did not provide a way to compute it.

Thus, **Kohn and Sham** introduced an approach in which the interacting many-electron system is reformed by a fictitious system of non-interacting electrons moving in an effective potential [18]. Although this system is hypothetical, it produces the exact ground-state electron density of the actual interacting system. Within this framework, the total energy is written as 

$$E\lbrack\rho\rbrack = T_{s}\lbrack\rho\rbrack + \int V_{\text{ext }}\rho + E_{H}\lbrack\rho\rbrack + E_{\text{xc }}\lbrack\rho\rbrack,$$

 where, $$T_{s}\lbrack\rho\rbrack$$ is the kinetic energy of an auxiliary system of non-interacting electrons, $$E_{H}\lbrack\rho\rbrack$$ is the classical Hartree term describing electron–electron electrostatic repulsion, and $$E_{\text{xc }}\lbrack\rho\rbrack$$ is the exchange–correlation functional.

The corresponding Kohn–Sham equations take the form: 

$$\left\lbrack - \frac{1}{2}\nabla^{2} + V_{\text{eff }}(r) \right\rbrack\varphi_{i}(r) = \varepsilon_{i}\varphi_{i}(r),$$

 where $$V_{\text{eff }}(r)$$ is an effective potential and $$\varphi_{i}(r)$$ is the $$i$$-th Kohn-Sham orbital and $$\varepsilon_{i}$$ is the corresponding Kohn-Sham orbital energy eigenvalue. The electron density is therefore constructed from the orbitals as follows: 

$$\rho(r) = \sum_{i}|\varphi_{i}(r)|^{2.}$$

These equations are solved iteratively until convergence, yielding a stable ground-state density and energy of the system. This procedure is called the self-consistent field (SCF) method.

### Jacob’s Ladder: Systematic Improvement of DFT

 {% include figure.html image='images/sourav-2.png' caption='Schematic representation of Jacob’s ladder in DFT, approximations from LDA → GGA → meta-GGA → hybrid → double hybrid, showing increasing accuracy.' width=800 %}

To systematically enhance the accuracy of density functional calculations, John P. Perdew introduced the concept of Jacob’s ladder[19], which organises density functional approximations into a hierarchy of increasing sophistication:


+ Local Density Approximation (LDA): depends only on local density


+ Generalised Gradient Approximation (GGA): incorporates both density and its spatial gradients


+ Meta-GGA: further includes quantities such as the kinetic energy density


+ Hybrid functionals: combine DFT exchange with exact exchange


+ Double hybrids: include perturbative correlation corrections.

As we move up Jacob’s ladder, more physical information is included, improving the description of exchange-correlation. Although DFT relies on approximate functionals, it offers an excellent balance between computational accuracy and cost (approximately $$N^{4}$$ scaling, where $$N$$ represents the number of atoms). Therefore, it is widely used in studying larger molecules, solids and condensed matter systems.

## Coupled Cluster and Relativistic Coupled Cluster

 For highly accurate calculations, especially when electron correlation effects are substantial, Coupled Cluster (CC) Theory was developed as one of the most compelling and systematically improvable approaches. The method is widely recognised as the benchmark, or “gold standard” for molecular energies and related properties.

Within the CC scheme, the correlated wavefunction is expressed using an exponential ansatz in the form of 

$$~|~\Psi_{\text{cc }}\rangle = e^{T}~|~\Phi_{0}\rangle,$$

 where $$T$$ is the cluster excitation operator that accounts for electron correlation effects through a hierarchy of excitations built upon the reference Slater determinant $$|\Phi_{0}\rangle$$ [20]. In practical applications, the expansion is commonly truncated to obtain computationally feasible methods such as coupled cluster single and double excitations (CCSD) and coupled cluster single and double excitations including perturbative triple excitations (CCSD(T)). These methods frequently yield molecular energies and related properties with near experimental accuracy, especially for small and medium-sized molecular systems.

Figure 3 presents the computational scaling of widely used electron structure methods. The steep growth in computational expense with increasing system size N underscores the difficulty of extending highly accurate correlation-based approaches to large molecular systems.

The standard CC starts from a single HF reference, which assumes one electronic configuration dominates. This breaks for systems exhibiting near-degeneracy effects, such as bond dissociation or strongly correlated electronic states. Thus, multireference extensions of CC become necessary. It captures both static and dynamic electron correlation effects within a unified framework[21-22].

Beyond energies, CC theory is extended to compute molecular properties analytically, dipole moments, polarizabilities, NMR shielding, spectroscopic constant and more. The Z-vector method makes this an efficient method[23]. It solves a linear response equation and computes all first-order properties rather than differentiating the CC wavefunction.

{% include figure.html image='images/sourav-3.png' caption='Comparison of computational scaling with increasing system size for electronic-structure methods. The log of CPU time is plotted against the number of atoms $$N$$, showing characteristic polynomial scalings: semi-empirical methods ($$- N^\{2\}$$), DFT ($$- N^\{4\}$$), MP2 ($$- N^\{5\}$$), CCSD ($$- N^\{6\}$$), and CCSD(T) ($$- N^\{7\}$$). The figure highlights the rapidly increasing computational expense of higher-accuracy correlated methods with system size.' width=800 %}

 For systems having heavy elements, relativistic effects become necessary for achieving accurate theoretical predictions. The most famous example is that gold and silver are predicted to exhibit similar chemical and optical properties. But the relativistic correction of the 6s orbital of gold results in the change in s-d orbital energy gaps, which directly explains gold’s anomalous optical appearance and chemical behaviour. Relativistic effects are also crucial in phenomena such as parity non-conservation [24] and electron electric dipole moment studies in heavy molecules like HgF [25].

To consistently incorporate both relativistic and electron correlation effects in a consistent manner, CC theory is extended to the relativistic coupled cluster framework (RCC). Together with response theory approaches such as Z vector methods, RCC enables highly accurate calculations of spectroscopic and electromagnetic properties, including hyperfine constant, transition moments and parity violation interactions [26-27]. Consequently, relativistic quantum many-body methods have become indispensable tools in modern quantum science and precise quantum measurements.

## Next Century of Quantum Mechanics

 The modern quantum mechanics is increasingly moving towards highly accurate and scalable approaches based on advanced many-body methods such as CC theory and its relativistic extensions. These methods provide a rigorous description of electron correlation and chemical bonding, often achieving near experimental accuracy even for heavy element systems and strongly correlated materials. At the same time, machine learning techniques are being incorporated to accelerate electronic structure calculations while preserving first-principles accuracy. Overall, the field is evolving towards a combination of quantum many-body theory and data-driven methods, enabling reliable prediction of molecular and material properties.

