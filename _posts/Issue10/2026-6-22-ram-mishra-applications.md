---
author-affiliation:
- IISER Pune
author-bio: '**Ram Mishra** is a professor in mathematics at IISER Pune. She obtained her doctoral degree from IIT Bombay in 1994. She works in knot theory. She has served in IIT Delhi and IIT Kharagpur before joining IISER Pune. Her research interests lie in low dimensional topology, real algebraic geometry and applications of knot theory in other areas of science.'
authorImage: mishra.jpeg
authors:
- Ram Mishra
category: article
date: 2026-6-22
excerpt: "A knot may look simple, but proving whether it can be untangled\u2014or telling one knot from another\u2014can take sophisticated mathematics. This article introduces knot theory\u2019s tools for answering those questions, then follows their surprising reach from the twisting of DNA and protein structure to the braided particles proposed for quantum computing."
hero-image: mishra.svg
issue: '10'
permalink: /issue10/ram-mishra-applications/
refs-file: mishra
reviewed-by: Puppala Ainesh Kumar, Debanuj Chatterjee
title: The Mathematics Behind Knots and Its Fascinating Real World Applications
---


Knots have a rich and long history and have been used for various activities like fishing, hunting and building. To understand knots we pick a rope and tie it as in .

{% include figure.html image='tying-a-knot.jpg' caption='Tying a knot' width=800 %}

Now if we want to describe it mathematically, we model the rope by the real line $$\mathbb{R}$$ and the process of tying a knot as embedding $$\mathbb{R}$$ in $$\mathbb{R}^{3}$$ [6]. We can obtain several different knots. Some of them are shown in .

{% include figure.html image='types-of-knot.jpg' caption='Different knots with a rope' width=800 %}

We may simplify a knot to make sure if it is truly knotted. However there may be a mistake in drawing an inference while simplifying the knot.

To overcome this confusion, we join the ends of the rope and hence it is no longer an embedding of $$\mathbb{R}$$ in $$\mathbb{R}^{3}$$ but now it is embedding of $$S^{1}$$ (circle) in $$\mathbb{R}^{3}$$. Since $$S^{3}$$ is a one point compactification of $$\mathbb{R}^{3}$$ [1], we can consider a knot as embeddings of $$S^{1}$$ in $$S^{3}$$ to avail the advantage of compactness. Mathematicians take this as definition of a knot! Thus, a knot is the image of a smooth embedding of $$S^{1}$$ in $$\mathbb{R}^{3}$$ or in $$S^{3}$$ and it will be a simple closed curve in $$3$$ dimensional space. This is also referred to as a classical knot. If the simple closed curve is drawn without a strand passing under another strand, it is called a _trivial knot_ or an unknot. Mathematicians have developed a beautiful subject called **_knot theory_** that has found applications in several real life problems.  shows some examples of classical knots.

Knots generalize to links and we define a link with $$r$$ components to be a smooth embedding of $$S^{1} \cup S^{1} \cup \cdots \cup S^{1}$$ ($$r$$ copies) in $$\mathbb{R}^{3}$$. Thus a knot is a link with $$1$$ component. In  we can see links with 2 and 3 components.

{% include figure.html image='knot-examples.svg' caption='Examples of classical knots' width=800 %}

{% include figure.html image='links.png' caption='Examples of links with 2 and 3 components. [Sci Rep 7, 12420 (2017)]' width=800 %}

## A brief history of knot theory

 Knot theory [3] was first introduced in 1771 by **Vandermonde** who noted the significance of topology in his discussion regarding the properties of knots in relation to the geometry of position. In the 19th century, studies led to **Peter Guthrie Tait** created the first knot table. In 1885, the Scottish mathematician and physicist showed fellow mathematician Sir **William Thomson** (later to become Lord Kelvin) his device that generated smoke rings. Kelvin did develop a theory which theorized that atoms might consist of knotted vortex tubes of the ether, but this theory was later rejected. Table of knots prepared by Tait using his conjectures motivated the early theorists of knot theory.

## Equivalence between knots and links

 In non-technical terms, if we can change a knot into another knot without cutting or tearing it, then we say that these two knots are equivalent. For examples, these two knots drawn in  are equivalent and it is easy to prove it.

{% include figure.html image='equivalence-eps-converted-to.svg' caption='Two equivalent knots' width=800 %}

One can try hard but cannot convert the knot A into the knot B in . However, it is difficult to prove this.

A formal definition of knot equivalence is as follows: A knot $$k_{1}$$, is said to be ambient isotopic to knot $$k_{2}$$ if there exists an orientation preserving diffeomorphism $$h:S^{3} \rightarrow S^{3}$$ such that $$h(k_{1}) = k_{2}$$. This definition can be extended for links as well. We shall only use the term knot that will mean knots and links both. This matches with our intuitive idea of knot equivalence. However, it is very difficult to prove the knot equivalence using this definition. Thus, we need to find some properties or the structures or quantities that are preserved under this equivalence. These are known as **_knot invariants_**. The main objective in knot theory is to invent effective knot invariants. The simplest questions one might ask are: _given a knot can we detect if it is NOT un-knot_?, _Can a knot be equivalent to its mirror image_?, _given two knots $$k_{1}$$ and $$k_{2}$$ can we detect if $$k_{2}$$ is neither equivalent to $$k_{1}$$ nor to the mirror image of $$k_{1}$$_? Till date none of these questions are answered completely. There is no invariant that is complete and can be computed easily. The most popular method to define knot invariants is by representing knots by a diagram [7]. For that we choose to project our knot into a plane such that the projected image is a _generic immersion_ [5]. It consists of only transverse double points as in  (Diagram A). It should not have multiple points as in  (B), tangential intersections as in  (C) and cusps as in  (D). Such a projection always exists. This type of projection is known as a regular projection.

{% include figure.html image='inequivalence-eps-converted-to.svg' caption='Two non-equivalent knots' width=800 %}

{% include figure.html image='regularprojections-eps-converted-to.svg' caption='Regular and non-regular projections' width=800 %}

After obtaining a regular projection, at each double point we provide a choice of over/under crossing information and the resulting picture is called a _knot diagram_ as shown in .

{% include figure.html image='trefoildiagram-eps-converted-to.svg' caption='A typical knot diagram' width=800 %}

Knot diagrams are a sufficient data to tell us about the knot, except that there may be several knot diagrams for a particular knot. We need an equivalence at the diagram level! There are moves (shown in the figure below), known as Reidemeister moves [7] that capture the isotopy at the diagram level and we have the following:

**Theorem**: _Two knot diagrams represent isotopic knots if and only if one can be transformed into the other by a sequence of finitely many Reidemeister Moves_, mentioned in .

{% include figure.html image='rmoves-eps-converted-to.svg' caption='Reidemeister Moves' width=800 %}

When we define properties/ quantities/structures associated to a knot diagram, we need to check that it does not change when we perform any of the Reidemeister move. Then, we can say that the associated object is an invariant for knots and links.

One of the easiest invariants that can be defined using a knot diagram is _tri-colorability_ [4]. A knot diagram is tri-colorable (sometimes called simply colorable) if each arc can be colored with one of three colors such that: at least two colors are used in the diagram; and at every crossing, either: all three colors are used; or only one color is used, as depicted in .

It is easy to check that tri-colorability is a knot invariant by verifying its invariance under all Reidemeister moves (shown in ). Using this we can prove that the trefoil knot is actually knotted (). Also the trefoil knot and the figure eight knot are not equivalent (). Tri-colorability has been generalized to _n- colorability_ [7] and there is an invariant called _coloring number_ that is useful in distinguishing between few knots.

There are plethora of invariants defined using diagrams. Some of them are numerical invariants such as _bridge number_ and _unknotting number_ [7]. Some invariants are algebraic. Many of them are polynomials. Alexander polynomial [7] is the most understood invariant but it cannot differentiate a knot from the unknot and also a knot from its mirror image.

Another successful approach towards defining invariants is using the connection of links with braids [7]. Jones polynomial [7] is one of the celebrated invariants that was discovered in 1984 using representation theory of braid groups and it revolutionized the entire community. Many unresolved conjectures were proved with the help of Jones polynomial and it fetched the most prestigious award "Fields medal" to Vaughan Jones who discovered it. The surprising thing is that the Jones polynomial can be explained using the diagram in a very simple manner skipping the deep mathematics behind it. Around the same time when Vaughan Jones came up with his polynomial, **Louis Kauffman** [7] defined a polynomial invariant purely from diagram which turned out to be same as the Jones polynomial upon a change of variable! Thus the Jones polynomial was re-invented.

We need to incorporate an orientation into a diagram as shown in  and provide a weight $$+ 1$$ or $$- 1$$ at each crossing as per the convention shown in . The writhe $$w(D)$$ of a knot diagram $$D$$ is defined to be the sum of the weights at all the crossings of knot diagram as in . Note that writhe is not an invariant since it is not an invariant under Reidemeister Move I, even though it is preserved under Moves II and III.

{% include figure.html image='tricolor.jpg' caption='A tri-colorable diagram' width=800 %}

{% include figure.html image='tricolorinvariance.png' caption='Try-colorability is invariant under Reidemeister Moves' width=800 %}

Note that in a given knot diagram flipping one crossing from over to under (or vice-versa) reduces the complexity of the knot. The reason being, every knot can be converted into an unknot if we perform this change a certain number of times. Also a knot/link with higher number of times it crosses is considered as more complex. Thus in an oriented diagram, if we skip the crossing and follow the orientation of the knot, we are reducing the complexity. This is called smoothing. Some invariants for a given knot can be computed if one knows their values for knots obtained after performing above two operations at a fixed crossing. This may not be possible for every invariant. Invariants possessing this property come under a class known as _skein invariants_ [7]. To understand them, we first define skein related diagrams. Three oriented diagrams are said to be skein related if they are identical everywhere except at one crossing and at that they look as shown in the .

Suppose $$\mathcal{I}$$ is an invariant for knots and links that takes values in a ring $$R$$. We say that $$\mathcal{I}$$ is a **linear skein invariant** if (i) $$\mathcal{I}(\mathcal{O}) = 1$$ and (ii) there exist three invertible elements $$a_{+},a_{-}$$ and $$a_{0}$$ in $$R$$ such that whenever we have three skein related diagrams $$\mathcal{L}_{+}$$, $$\mathcal{L}_{-}$$ and $$\mathcal{L}_{0}$$ the invariants evaluated at these knots satisfy the linear relation: 

$$a_{+}\mathcal{I}(\mathcal{L}_{+}) + a_{-}\mathcal{I}(\mathcal{L}_{-}) + a_{0}\mathcal{I}(\mathcal{L}_{0}) = 0.$$

 In fact, these coefficients are unique for an invariant except up to a change of variable.

{% include figure.html image='tricolorable.png' caption='Proof that the trefoil knot is truly knotted' width=800 %}

Alexander polynomial and Jones polynomial both are skein invariants. They take values in the ring $$\mathbb{Z}\lbrack t,t^{- 1}\rbrack$$. For a knot $$K$$ its Alexander polynomial $$\Delta(K)$$ satisfies the skein relation 

$$\Delta(L_{+}) - \Delta(L_{-}) - (t^{\frac{1}{2}} - t^{- \frac{1}{2}})\Delta(L_{0}) = 0$$

 and its Jones polynomial $$J(K)$$ satisfies the skein relation 

$$tJ(L_{+}) - t^{- 1}J(L_{-}) - (t^{\frac{1}{2}} - t^{- \frac{1}{2}})J(L_{0}) = 0.$$

Jones polynomial helped in solving many intrinsic questions in knot theory but it still has pitfalls. There are non-equivalent knots that shared the same Jones polynomial. This has been resolved by creating more refined invariants such as Khovanov homology [12] which categorifies the Jones polynomial. There are programs written which help in computing these invariants. One can find the information about these invariants on Knot atlas <br>
 (https://katlas.org). In nutshell, researchers in knot theory have been developing tools that help in checking if the given knot is truly knotted as well as differentiating between two given knots.

Now comes the question how could knot theory be useful in the real world problems. Imagine a bunch of wires kept together in a box and the box is undergoing a continuous shaking process. Do you think the wires will remain as it is? No, there is a high chance that individual wires may get knotted and also two different wires may get linked. This is the situation that arises in nature. There are places where the structures have the potential to get entangled and knotted. The most profound application of knot theory is in the study of DNA [8] that leads to the discovery of several drugs. The double helix structure of DNA (shown in ) enables it to get knotted under the influence of certain enzymes, called _topoisomerase_. Topoisomerases act by cutting a given number of DNA strands and recombining them in a new manner (eg., see ). The number of strands that are cut and recombined is related to the unknotting number of that knot. In fact these enzymes perform operations on DNA strands similar to Reidemeister moves to be able to simplify the knotted DNA.

It is known that Cancer is a disease caused by abnormalities in the DNA of a cell. A tumor is formed when these abnormal cells accumulate in one area. Developing drugs that can fight tumors with minimal side effect has been a long term goal in the cancer treatment research. In place of using radiation and chemotherapy, knot theory can be utilized in manipulating DNA replication through enzymes. This might stop the damaged cells to multiply and eventually the tumors may shrink and hence could be an effective treatment for cancer [9].

Another situation where knot theory has been found useful is in the understanding of protein structures [10]. Proteins are complex molecules and do most work in a cell. Collagen, Keratin, hemoglobin and insulin are some of the examples of proteins in our body. Proteins are continuous linear molecules appearing as linear segments embedded in 3-space. Protein structure for a single protein is formed on three different levels (Primary, Secondary and Tertiary) as shown in .

{% include figure.html image='tref-fig8.png' caption='Trefoil and Figure eight knots are not equivalent' width=800 %}

{% include figure.html image='orienteddiagrams.png' caption='An oriented knot diagram' width=800 %}

In the primary structure of a protein amino acids are arranged in a single line- there are no branches. When looking at a chain of amino acids it is always helpful to first orient yourself by finding this **backbone pattern** starting from the N terminus to the C terminus. The sequence and the number of amino acids ultimately determine the protein's shape, size, and function. Each amino acid is attached to another amino acid by a covalent bond, known as a peptide bond. Every amino acid also has another atom or group of atoms bonded to the alpha carbon known alternately as the R group, the variable group or the side-chain. The process by which the final 3-D structure of a protein is attained is known as _Protein folding_. Classifying proteins on the basis of their structure is an important problem for biologists as structure and function are very closely related. From the mathematical perspective, a protein structure is represented as a collection of atoms together with their coordinates in three-dimensional space, $$\mathbb{R}^{3}.$$ Thus, if $$N$$ atoms are listed with coordinates we have a vector in $$(\mathbb{R}^{3})^{N}.$$ _Two protein structures are said to be the same if one can be transformed into the other by an orientation-preserving Euclidean motion._

{% include figure.html image='writhe.jpg' caption='Sign convention at a crossing' width=800 %}

It is convenient to think of a protein as a collection of piecewise linear (PL) curves formed by a sequence of points $$p_{0},p_{1},\ldots,p_{n}$$ in three-dimensional space joined by line segments. Thus the backbone of a protein is a PL curve, with no self intersections and consists of a sequence of points representing the various $$C_{a}$$ atoms proceeding from the $$N -$$terminus to the $$C -$$ terminus. By putting the atoms in sequential order, a side-chain can also be represented as a PL curve. Since the Backbone of a protein can be regarded as a PL curve, whose one end represents amide end ($$N$$ terminus) and the other end represents the carboxyl end ($$C$$ terminus). This is technically an open oriented knot. It is of interest to understand the "knottedness" of this chain. Final structure of protein after folding will largely depend on the topology of its backbone, in the sense if backbones of two different proteins are differently knotted their final structures will have different shape and hence their functions will be different. Relevant questions to ask are: How to detect if the backbone knot is trivial?, If the backbone knot is non-trivial, can we determine its knot-type? Can knot theory be used in the classification of proteins by their 3-D structure? Many scientists have tried to answer the above questions. Broadly speaking, there are two different ways of studying the conformations of "knotted" protein chains: Hold the ends fixed and deform the backbone. And then interpret the final configuration. Start with an open knot and complete it to a topological knot and then identify the knot type. It is noted that both these methods have a certain degree of uncertainty. As the backbone knot is regarded as a PL knot we use the elementary moves to simplify it. William R. Taylor developed an algorithm for detecting knots in protein backbones and this was further refined and is now know as **KMT algorithm**. If the backbone gets straightened to the straight line joining the end points, then the backbone does not contain a knot. Thus this algorithm answers the first question. Once it is detected that the backbone has a non trivial knot, with the help of simplifying the diagram we identify the knot types () . Knot invariants are useful in this.

{% include figure.html image='Skein-relation.png' caption='Skein-related diagrams' width=800 %}

{% include figure.html image='DNA.png' caption='Structure of a DNA' width=800 %}

 {% include figure.html image='knotteddna.png' caption='A knotted DNA' width=800 %}

Similar to the question of detecting two knots being ambient isotopic, scientists may _ask can two proteins be rearranged (without cutting) to be exactly alike?_ In this direction Chen and Dill used knot theory in modeling proteins by associating a knot with every protein so that if two protein Structures are equivalent then the associated knots are equivalent. This is done as follows: To each chain they associate a planar signed graph known as its _Polymer graph_. From this graph using the _medial construction_ they obtain a link diagram. Then knot theoretic tools could be used to determine the isotopy classes of these links. Application of knot theory and its tools to understanding proteins is still in a nascent stage. Some of the unanswered questions are stated below. Can the knotted protein backbones be unknotted _in vivo_? If they can be unknotted _in vivo_ then what is the mechanism for unknotting and knotting? Is there a suitable model explaining the occurrence of existing knots and predicting the kinds of knots that might occur or evolve? Given a knot $$K$$, can one construct a protein molecule whose backbone has the knot $$K$$?

Apart from biological sciences , knot theory is used in chemistry to synthesize new molecules and create new kinds of medicines. In physics, it is used to study the behavior of particles and fields in three-dimensional space. In Art, it is used to study patterns and symmetries in textile design and weaving. In the current era, the most fascinating application of knot theory has come to notice is in building _quantum computers_ [11]. The main idea of using knot theory in quantum computing is to encode and process information using the topological 'braiding' of exotic quasiparticles called _anyons_. Because these knots depend on global tangling rather than local state, they provide fault-tolerant, noise-resistant qubits that are immune to most environmental disturbances.

I would like to conclude with a statement of Collin Adams, '_Knot theory began with sailors' ropes and mathematicians' curiosities. Today, it's helping decode the fundamental processes of life itself. This marriage of pure mathematics and molecular biology shows how abstract ideas can yield concrete, even life-saving, applications_'.

{% include figure.html image='proteinstructure.svg' caption='Protein structure at different level' width=800 %}

{% include figure.html image='knottypes.svg' caption='Knot types detected in protein' width=800 %}

 