---
author-affiliation:
- Department of Mathematics and Statistics, IISER Kolkata
author-bio: '**Abhratanu Ray** is a 4th year student at DMS, IISER Kolkata. He is interested in algebraic topology and stochastic processes. Above all, he enjoys solving problems and wishes to apply his skills in the world of finance and business strategy in the near future.'
authorImage: abhratanu.jpeg
authors:
- Abhratanu Ray
category: article
date: 2026-2-22
excerpt: '**Sometimes, the most fun problems to work on are the** ones easiest to visualise. We will go through 2 proofs of a deceptively simple statement conjectured by James Joseph Sylvester in 1893: one of them is a surprisingly short one by Kelly (1986) and the other is a more conceptually dense one by Melchior (1941).'
hero-image: abhratanu.svg
issue: 8
permalink: /issue8/abhratanu-ray-proofs/
refs-file: null
reviewed-by:
- Debanuj Chatterjee
title: "Finite Points, \u201CInfinity Lines\u201D and a Couple of Nice Proofs"
---


## Introduction

 Sometimes, the most fun problems to work on are the ones easiest to visualize. Especially in geometry, problems like this are everywhere. The simplest ideas can generate non-trivial problems, with beautiful solutions. Thinking about random point arrangements (the basis of incidence geometry; that is, the geometry that deals with sets of points and lines through points), one stumbles upon a problem that is easy enough to come up with: the following problem, presented by James Joseph Sylvester in 1893.

**Problem:** Prove that it is not possible to arrange any finite number of real points so that a straight line through every two of them shall pass through a third, unless they all lie in the same straight line.

Or rephrased, in every arrangement of a finite number of real points on the Euclidean plane (which is just the familiar flat, infinite, two-dimensional surface of standard high-school geometry), there is a straight line passing through only two of these points, unless all points are collinear.

To get an initial hold of this problem, imagine some points, all in the same line. We know there is some unique line passing through all of them. Now, we displace one of these points slightly. <br>
 {% include figure.html image='abhratanu1.png' caption='' width=800 %}

We can see that some line has been generated that passes through only two of the points: the displaced point, and the adjacent point to it. The idea of the problem is to show such a line, passing through **exactly two points**, exists in all possible arrangements of finite points.

On first instinct, proof by contradiction seems to be the way to go. And it was, for Kelly, although this proof was pretty pervasive, and went undiscovered for decades, it is a really short and simple one.

**We shall go through two proofs of the problem statement**. One given by **Eberhard Melchior**, in 1941, after Paul Erdős popularised the problem; and the other much later, in 1986, by **Leroy Milton Kelly**. The former proof is a much more general one, made using concepts of graph theory, and projective plane geometry (I will try my best to explain this, to the extent at which I am able to grasp it myself), and the latter is a much simpler and more elegant one, although not being nearly as useful in application to other spheres or problems as Melchior's.

We list 2 standard definitions for our proofs:

**Definition 1:** Let $$P = \left\{ n_{1},n_{2},n_{3}\ldots \right\},n \geq 3$$ be a set of not all collinear points in the euclidean plane. A line that contains two or more points of P is called a connecting line and is **ordinary**, if it contains exactly two points.

**Definition 2:** If a line passes through $$n$$ points on the plane P, it is called **$$n$$-rich**.

We restate **Problem 1** as the following theorem, then proceed to prove it.

**Theorem 1.1:** **(Sylvester-Gallai Theorem)** Every such set P determines at least one ordinary line.

Let us first look at Kelly's proof, a truly beautiful and simple one, with elementary geometrical construction, proving the theorem by contradiction.

## Kelly's Proof

 _Proof._ Let $$l$$ be a line in the plane, such that it passes through $$n$$ points in the plane, and there exists some point $$P$$ in the plane, whose perpendicular distance to $$l$$ is the minimal perpendicular distance between any point-line pair in the plane. Note that since we have an arrangement of a finite number of points (in the set P) in our plane, the set of lines determined by the points in P is also finite. <br>
 {% include figure.html image='abhratanu2.png' caption='' width=800 %}

Now we draw a perpendicular $$PP'$$ onto $$l$$. There must exist at least one point on either side of $$P$$, on $$l$$. We have two cases:


+ $$l$$ is ordinary.


+ $$l$$ is not ordinary, it is $$n$$-rich for some $$n > 2.$$

We assume Case 2 to be true. Then, there must be more than one point on the left or right of $$P'$$. Let us say there are two points $$B$$ and $$C$$ to the right of $$P'$$, such that $$B$$ is the first point on the right of $$P'$$, and $$C$$ is some other point. <br>
Now, we draw a line $$m$$, through $$PC$$. We draw a perpendicular from $$B$$ onto $$m$$. Observe that this perpendicular $$BB'$$, will have a shorter length than $$PP'$$. <br>
 Then we have found a point-pair, namely $$B$$ and $$m$$, such that the perpendicular distance is even lesser than $$PP'$$. <br>
But, this contradicts our choice of $$l$$ and $$P$$ as the closest point-line pair.

Hence, Case-1 must be true, and $$l$$ is proved to be ordinary. 

On first read, this proof felt extremely satisfying to me, like it was out of Erdős' "**Book**". But in a way, this proof is "a bit too clever". There isn't much of anything we can extend this to. <br>
 For the purpose of extension, and to find some results we can apply to other areas of Mathematics, we turn now, to **Melchior's proof**.

## Melchior's Proof

 In this proof, the concepts of the **Projective Plane** and **Graph Theory** have been used. We will go through the specific results/concepts we need.

### Projective Plane

**Definition 3:** A **projective plane** $$\pi$$ is a triple $$(\mathbb{P},\mathbb{L},\mathbb{I})$$ such that $$\mathbb{P}$$ is a set of points, $$\mathbb{L}$$ is a set of lines and $$\mathbb{I}$$ is an incidence relation generated by the following binding axioms:


+ $$\exists$$ a unique line in the set $$\mathbb{L}$$ joining any 2 distinct points from the set $$\mathbb{P}$$.


+ $$\exists$$ a unique point of intersection of any 2 distinct lines from the set $$\mathbb{L}$$.


+ $$\exists$$ $$\geq 3$$ non-collinear points in the set $$\mathbb{P}$$.


+ $$\exists$$ $$\geq$$ 3 points on each line in the set $$\mathbb{L}$$.

The modification made to our "normal" notions of geometry here, is that **all** lines intersect. More precisely, all parallel lines now intersect at **one, distinct point** which is placed "at infinity" and on the **line at infinity**.

**Definition 4:** A **affine plane** is a triple $$(\mathbb{P},\mathbb{L},\mathbb{I})$$ such that $$\mathbb{P}$$ is a set of points, $$\mathbb{L}$$ is a set of lines and $$\mathbb{I}$$ is an incidence relation generated by the following binding axioms:


+ Every pair of points in the set $$\mathbb{P}$$ lies on a unique line in the set $$\mathbb{L}$$


+ Given any line $$l \in \mathbb{L}$$ and any point $$P \in \mathbb{P}$$ which doesn't lie on $$l$$, $$\exists$$ a unique line $$m \in \mathbb{L}$$ such that P lies on $$m$$ and $$l \cap m = \varnothing$$ (no point lies on both $$l$$ and $$m$$).


+ $$\exists$$ $$3$$ non-collinear points in the set $$\mathbb{P}$$.

The affine plane represents pretty much what our "normal" notion of geometry is. The euclidean plane, which we are most used to, is an example of an affine plane.

**Definition 5:** A **pencil** of parallel lines is the set of all lines which are parallel, in the affine plane.

**Theorem:** Let $$\pi = (\mathbb{P},\mathbb{L},\mathbb{I})$$ be a projective plane. <br>
 Removing any line $$l_{\infty}$$ of $$\pi$$ as well as all points on it, forms a new triple $$\pi^{l_{\infty}}$$, such that $$\pi^{l_{\infty}}$$ is an affine plane.

_Proof._ We verify the 3 points in Definition 4. <br>
 **1.** Let $$P,Q$$ be two distinct points, not on $$l_{\infty}$$. Then, there is a unique line $$m$$ through them in $$\mathbb{L}$$, by the definition of a projective plane. Hence, $$m$$ is a line in $$\mathbb{L} - \left\{ l_{\infty} \right\}$$ passing through $$P$$ and $$Q$$.

**2.** Let $$m \in \mathbb{L} - \left\{ l_{\infty} \right\}$$ and $$P \in \mathbb{P}$$ be a point not on $$m$$. Then, in the projective plane $$\pi$$, there is a unique line passing through $$P$$ and $$I = m \cap l_{\infty}$$. Then, clearly $$n \neq m$$ and $$n$$ only intersects $$m$$ at $$I$$ in $$\pi$$, so that in the new plane, $$n$$ and $$m$$ are parallel. The uniqueness of $$n$$ follows from the fact that the line passing through $$P$$ and $$I$$ in $$\pi$$ is unique. <br>
**3.** Follows directly from the definition of a projective plane. 

**Theorem 3.1:** **(Theorem of Duality)** If $$\mathbb{T}$$ is a valid theorem in the projective plane, and $$\mathbb{T}'$$ is a new statement obtained from $$\mathbb{T}$$, by making the following changes:


+ "point" $$\leftrightarrow$$ "line"


+ "collinear" $$\leftrightarrow$$ "concurrent"


+ "join" $$\leftrightarrow$$ "intersection"

Then, $$\mathbb{T}'$$ holds for the projective plane.

The proof for Theorem 3.1 is omitted here, but it is quite easy to see why it works with an example, as given below. <br>
We consider the Theorem of Pappus as an example.

**Theorem 3.2:** **(Pappus' Theorem)** Let $$l,l'$$ be two lines in the plane. Let


+ $$A,B,C$$ be points of $$l$$.


+ $$A',B',C'$$ be points of $$l'$$.


+ all these points be distinct from $$l \cap l',$$

Then, $$L = AB' \cap A'B,M = AC' \cap A'C,N = BC' \cap B'C$$ are collinear. <br>
 <br>
 **(Dual Version of the Theorem)** Let $$P,P'$$ be two points in the plane. Let


+ $$a,b,c$$ be lines concurrent at P.


+ $$a',b',c'$$ be lines concurrent at P'.


+ all these lines be distinct from that joining $$P,P'.$$

Then, $$l$$ joining $$(a \cap b')$$ and $$(b \cap a')$$, $$n$$ joining $$(a \cap c')$$ and $$(c \cap a')$$, $$m$$ joining $$(c \cap b')$$ and $$(b \cap c')$$ are concurrent at some point $$Q$$.

Below are the standard, and dual versions of the theorem in a diagrammatic form. {% include figure.html image='abhratanu3.png' caption='' width=800 %}

### Some concepts of Graph Theory

 **Definition 6:** A **graph** is defined as an object consisting of 2 sets: $$V_{G}$$, a set of vertices and $$V_{E}$$, a set of edges, which are 2 point sets. <br>
 For example, a graph G can be written as &#123;&#123;P,Q,R,S,T},&#123;&#123;P,Q},&#123;R,S},&#123;Q,T}}}.

**Definition 7:** The **degree** of a vertex is equal to the number of edges connecting at that vertex.

**Definition 8:** The **Euler Characteristic $$\chi$$** is defined for graphs, by the formula $$\chi = V - E + F$$, where $$V$$ is the number of vertices, $$E$$ is the number of edges and $$F$$ is the number of connected regions (including unbounded regions).

**We take it as a fact that for projective planes, $$\mathbf{\chi = 1.}$$** The rigorous proof for this is quite convoluted, but we can accept the intuition that for planar graphs, it is easy to prove that $$\chi = 2$$ and in the projective plane, the line at infinity acts like an "extra edge". <br>
 Proofs of this fact use algebraic topology and are out of the scope of this article.

### Proceeding with the proof

 Now we can finally attempt to understand Melchior's proof, with the knowledge of preceding subsections. <br>
_Proof._ Let P be a finite set of points in a projective plane $$\pi = (P,L,I)$$. Let us consider a **dual collection** of $$n$$ lines:

$$P^{\ast} = \left\{ p^{\ast}:p \in P \right\}$$.

We know from that (for the projective plane) 

$$V - E + F = 1.$$

 Now, by duality, we can write 

$$V = \sum_{k = 2}^{n}N_{k},$$

 where $$N_{k}$$ is the number of lines passing through only k vertices. (By duality, this sums up all vertices of degree 2, then of degree 3, and so on till degree $$n$$, which spans all vertices.) <br>
 Also, the degree of a vertex $$l^{\ast},d(l^{\ast})$$ is twice the number of lines passing through it, since a line through a point consists two edges for that point. This degree (by duality) can be written as $$\mathbf{2|P \cap l|}$$, which is equal to twice the number of points of $$P$$ on any line in the arrangement. <br>
 Summing over all lines $$l$$: 

$$2E = \sum_{l}d(l^{\ast}) = 2\sum_{l}|P \cap l| = 2\sum_{k = 2}^{n}kN_{k}.$$

 Let $$M_{s}$$ be the number of faces with $$s$$ edges. Since every face is bounded by at least 3 edges, and each edge is incident to 2 faces, we can write 

$$2E = \sum_{s = 3}^{n}sM_{s}.$$

 Combining equations 1,2,3 and 4, we can find our required result. 

$$$$

 which implies the Sylvester-Gallai Theorem. 

 Surprisingly enough, this proof not only shows that one ordinary line shall exist, but rather that **three must exist**, for any finite arrangement.

This proof gives us a "better" result, although it is way more convoluted than what Kelly came up with. It is quite stunning how elusive the prior proof was. It took decades after Melchior's publication, for someone to revisit the problem, after Paul Erdos brought it back up, so this elegant and beautiful proof could be presented to the world. <br>
The most satisfying mathematics is not always the most applicable, or "the best". Beauty, in many cases, arises from simplicity. 