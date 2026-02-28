---
author-affiliation:
- Postdoctoral Researcher, University of Cologne
authorImage: koustav.jpeg
authors:
- Koustav Banerjee
category: article
date:
  day: 18
  month: 12
  year: 2025
excerpt: "This article explores the mathematics of integer partitions, a simple counting\
  \ problem with deep consequences. Beginning with Euler\u2019s ideas, we trace how\
  \ the subject evolved through the work of Hardy, Ramanujan, and Rademacher. The\
  \ story shows how combinatorics, number theory, and analysis come together to reveal\
  \ the hidden structure behind counting numbers."
hero-image: koustav.svg
permalink: /issue7/koustav-analysis/
refs-file: koustavRefs
title: 'Integer Partitions in Three Acts: Combinatorics, Number Theory, and Analysis'
author-bio: "*Koustav Banerjee* has obtained his doctoral degree from Research Institute of Symbolic Computation (RISC), Johannes Kepler University, Austria under supervision of Prof. Peter Paule. After spending one year and nine months as a postdoctoral fellow under mentorship of Prof. Paule, he has joined Prof. Kathrin Bringmann's group.  Since November, 2024, he is working as a post-doc at University of Cologne with Prof. Bringmann."
---


## The Partition Function: A Combinatorial Genesis

Primarily, there are two ways of decompose a natural number. One way is multiplicative, precisely, factoring a number into primes and other way is additive. In this section, we discuss the additive decomposition in brevity. This additive decomposition is well-known as “integer partitions”. In the history of the literature on partitions, Leibniz seems to be the first person who defined integer partitions. In a 1674 letter [12, page 37], he asked J. Bernoulli about the number of “divulsions” of an integer. In modern terminology, “divulsion” is rephrased as the number of partitions of a positive integer. Leibniz observed that there are three partitions of 3 counted by 3, 2 + 1, 1 + 1 + 1, five partitions of 4 counted by 4, 3 + 1, 2 + 2, 2 + 1 + 1, 1 + 1 + 1 + 1, seven partitions of 5 and eleven partitions of 6. This examples lead to a problem which is still open:

> Are there infinitely many integers $$n$$ for which the total number of partitions of $$n$$ is a prime?

Keeping this question aside, let us move on define the partition function.

A _partition_ of a positive integer $$n$$ is a finite non-increasing sequence of positive integers $$\lambda_{1},\ldots,\lambda_{r}$$ such that $$\sum_{j = 1}^{r}\lambda_{j} = n$$. The $$\lambda_{j}$$ are called the parts of the partition. The partition $$\left( \lambda_{1},\lambda_{2},\ldots,\lambda_{r} \right)$$ is denoted by $$\lambda$$, and we write $$\lambda \vdash n$$ to denote that $$\lambda$$ is a partition of $$n$$. The partition function $$p(n)$$ is the number of partitions of $$n$$. The set of all partitions of $$n$$ is denoted by $$P(n)$$. Euler undertook a rigorous and systematic investigation of the theory of partitions. Ph. Naudé $$\lbrack 6\rbrack$$ wrote a letter to Euler asking about the number of partitions of $$n$$ with the total number of parts in each partition being $$m$$. Precisely the question of Naudé was: what is the total number of partitions of $$50$$ into seven distinct parts? It is quite unlikely to get the total number by writing down all the partitions of $$50$$ into seven distinct parts. To avoid this, Euler introduced the concept of generating functions. Let $$p_{m(n)}$$ denote the number of partitions of $$n$$ into $$m$$ parts. Then following Euler"s observation, we get


$$\begin{aligned}
\sum\limits_{m,n \geq 0}p_{m}(n)z^{m}q^{n} & = \prod\limits_{k = 1}^{\infty}\left( 1 + \text{zq}^{k} \right) \\
 & = \left( 1 + \text{zq} \right)\prod\limits_{k \geq 1}\left( 1 + \left( \text{zq} \right)q^{k} \right) \\
 & = \left( 1 + \text{zq} \right)\sum\limits_{m,n \geq 0}p_{m}(n)z^{m}q^{m + n}.
\end{aligned}$$


Comparing the coefficients of $$z^{m}q^{n}$$ on both sides of the above identity, we find the following recursive formula


$$p_{m}(n) = p_{m}(n - m) + p_{m - 1}(n - m),$$


which gives $$p_{7}(50) = 522$$. Euler proceeded further to obtain a generating function for $$p(n)$$. Euler"s calculation can be put in the following way:


$$\begin{aligned}
P(q): & = \sum\limits_{n \geq 0}p(n)q^{n} \\
 & = \left( 1 + q^{1} + q^{1 + 1} + \ldots \right)\left( 1 + q^{2} + q^{2 + 2} + \ldots \right) \\
 & \ \ \ \left( 1 + q^{3} + q^{3 + 3} + \ldots \right)\ldots \\
 & = \prod\limits_{n \geq 1}\left( 1 + q^{n} + q^{n + n} + \ldots \right) = \prod\limits_{n \geq 1}\frac{1}{1 - q^{n}}.
\end{aligned}$$


Note that, rather than working with sequences, we are now in the regime of function, a switch between discrete to continuous. In order to simplifying (and doing fast) calculations for $$p(n)$$, Euler realized that a power series expansion for $$\prod_{n = 1}^{\infty}\left( 1 - q^{n} \right)$$ is essential. His empirical discovery leads to the following identity which is known as Euler"s Pentagonal Number Theorem.

 {% include figure.html image='/Euler.jpeg' caption='_**Leonhard Euler** (1707–1783), who introduced generating functions and laid the foundational framework for the theory of integer partitions._' width=400 %}
 


$$\prod\limits_{n \geq 1}\left( 1 - q^{n} \right) = \sum\limits_{n \in {\mathbb{Z}}}( - 1)^{n}q^{\frac{3n^{2} - n}{2}}.$$


This identity was proved by Euler himself many years after the discovery. For a modern exposition of Euler"s proof, we refer to Andrews" [1]. Putting (1.1) and (1.2) together, we see that


$$\sum\limits_{n \geq 0}p(n)q^{n}\sum\limits_{n \in {\mathbb{Z}}}( - 1)^{n}q^{\frac{3n^{2} - n}{2}} = 1,$$


and comparing the coefficients of $$q^{n}$$ on both sides of the last identity, Euler found the following recurrence for $$p(n)$$: $$p(0) = 1$$, and for all $$n \geq 1$$,


$$p(n) - p(n - 1) - p(n - 2) + p(n - 5) + p(n - 7) - \ldots = 0.$$


After Euler, the theory of partition propagates through the works of Sylvester, Cayley, Jacobi, MacMahon, Hardy, Ramanujan, Rademacher, Gordon, and Andrews among many others. The reader can consult Andrews" magnum opus [2]. In addition to that, the entire history of partitions up to 1918 is documented in [5], and for a survey article, we refer to [7].

The counting problem for $$p(n)$$ (for large values of $$n$$) has been one of the most predominant themes in the literature on integer partitions. First of all, we point out a simple fact: $$\left( p(n) \right)_{n \geq 1}$$ is a strictly increasing sequence. For a partition $$\pi \vdash n - 1$$, define a map $$\phi:P(n - 1) \rightarrow P(n)$$ by $$\phi(\pi) = (\pi,1)$$; i.e., insertion of $$1$$ as part in $$\pi$$ that yields a partitions of $$n$$ and it is clear that $$\phi$$ is an injective map and $$P(n) / \phi(P(n - 1))$$ is the set of all partitions of $$n$$ where $$1$$ is not a part (also known as non-unitary partitions of $$n$$). Let us try to formulate the problem of counting $$p(n)$$ in terms of counting partitions of $$n$$ subject to the condition that each partition has at most $$k$$ parts. Let $$p_{\leq k}(n)$$ denotes total number of such partitions of $$n$$. Observe that for $$k = n$$, $$p_{\leq k}(n) = p(n)$$. Cayley [4] and Sylvester [18] gave a number of formulas for $$p_{\leq k}(n)$$ with small values of $$k$$, which was anticipated by Herschel [10]. For example, 
$$$$
. Now the question we may ask how far we can compute $$p(n)$$. Is there any simple formula for counting $$p(n)$$ apart from (1.3)? Using (1.3), MacMahon computed $$p(200)$$ by hand and


$$p(200) = 3972999029388.$$


This was a remarkable achievement and of great importance [^1]. Now the question is

**Problem 1.1.** _How fast does $$p(n)$$ grows?_

To understand the problem and in order to get an answer, we need some artillery from analysis and number theory, precisely, the notion of asymptotics and modular forms.

## Preliminaries



**Approximations and asymptotics:** According to Russell,

> All exact science is dominated by the idea of approximation."

Since antiquity, the notions of approximations have played a crucial role in major disciplines of science and philosophy. The formula for approximating the square root of a number is often attributed to the Babylonians. Since then, mathematical formulae were developed to assist in approximating transcendental functions. Probably the first application of theory of approximations was due to Euler who tried to solve a problem of drawing a map of the Russian empire with exact latitudes. After Euler [^2], Gauß, Laplace, Fourier, Cauchy, Chebyshev, Lagrange, Poisson, Fejér, Weierstraß, Runge among many others expanded the theory of approximations while working on several problems in different domains of mathematics and physics. Asymptotic analysis is a branch of mathematical analysis that provides a rigorous foundation to understand the language of approximation. Let us start with a well-known asymptotic result, so-called Stirling"s formula: $$\lim\limits_{n \rightarrow \infty}\frac{n!}{\sqrt{2\pi n}n^{n}e^{- n}} = 1$$. In the language of asymptotics, we say $$n! \sim \sqrt{2\pi n}n^{n}e^{- n}$$, as $$n \rightarrow \infty$$. Now, the question naturally arises what is the significance of this limit formula when one can easily compute $$n!$$ with a computer? The point is, as $$n$$ became larger, we do not know how the function $$n!$$ really behaves. Thanks to Stirling"s approximation, we have now the information that $$n!$$ has exponential growth, i.e., we perceive the "unknown" function $$n!$$ in terms of well-known elementary functions. Let us conclude this section with another deep and famous asymptotic formula. Let $$x \in {\mathbb{R}}_{> 0}$$ and $$\pi(x)$$ denotes the number of primes not exceeding $$x$$. Based on the tables by Felkel and Vega, Legendre conjectured in 1797-1798 that $$\lim\limits_{x \rightarrow \infty}\frac{\pi(x)}{\left( \frac{x}{A\log x + B} \right)} = 1$$, and later in $$1808$$, he proposed that $$A = 1$$ and $$B \approx - 1.08366$$. The prime number theorem, originally conjectured by Gauß, and independently proved by Hadamard [8] and de la Vallée Poussin [14], states that


$$\pi(x) \sim \frac{x}{\log(x)}\text{ as }x \rightarrow \infty.$$


For an elementary proof of the prime number theorem, we refer the reader to Selberg"s proof [16].

**Modular Forms:** We begin with elementary trigonometric functions. Euler discovered that $$e^{ix} = \cos x + i\sin x$$, where $$i$$ is an imaginary number (termed by Descartes) satisfying $$i^{2} = - 1$$. In 1807, Fourier introduced a series, what is well-known as "Fourier series", for the purpose of solving the heat equation in a metal plate. Roughly we can say that a Fourier series is an infinite sum that represents a periodic function as a sum of sine and cosine functions. Both sine and cosine function are periodic with period $$2\pi$$, i.e., 
$$\sin(x + 2\pi) = \sin x$$
 and trivially, $$\sin(x + 2\pi k) = \sin x$$ for all $$k \in {\mathbb{Z}}$$. In group theoretic language, it is equivalent to say that $$\sin 2\pi x$$ is invariant under the abelian group $$({\mathbb{Z}}, + )$$. Therefore, the question arises which class of functions are invariant under the action of a non-abelian group? Before giving an example of such a class of functions, let us introduce a few preliminary definitions.

Define $${\mathbb{H}} ≔ \left\{ \tau \in {\mathbb{C}}:\text{ Im }\tau > 0 \right\}$$. Let $$\text{GL}_{2}({\mathbb{Z}})$$ be the set of $$2 \times 2$$ matrices with integer entries and non-zero determinant. The special linear group [^3] $$\text{SL}_{2}({\mathbb{Z}})$$ be a subgroup of $$\text{GL}_{2}({\mathbb{Z}})$$ with determinant one. The non-abelian group $$\text{SL}_{2}({\mathbb{Z}})$$ acts on $$\mathbb{H}$$ in the following way: for $$\gamma \in \text{ SL}_{2}({\mathbb{Z}})$$ and $$\tau \in {\mathbb{H}}$$, $$\gamma\tau ≔ \frac{a\tau + b}{c\tau + d}$$. Let $$k \in \frac{1}{2}{\mathbb{Z}}$$ and a holomorphic function $$f:{\mathbb{H}} \rightarrow {\mathbb{C}}$$ is called a _modular form_ of weight $$k$$ over $$\text{SL}_{2}({\mathbb{Z}})$$ if for 
$$\gamma = \begin{pmatrix}
a & b \\
c & d
\end{pmatrix} \in \text{ SL}_{2}({\mathbb{Z}})$$
 and $$\tau \in {\mathbb{H}}$$, it satisfies [^4] $$f(\gamma\tau) ≔ (c\tau + d)^{k}f(\tau)$$ (up to an automorphy factor) along with $$f$$ is bounded as $$v \rightarrow \infty$$ (with $$\tau = u + iv$$). Note that if $$k = 0$$, then $$f$$ is invariant under the non-abelian group $$\text{SL}_{2}({\mathbb{Z}})$$.

Note that for $$\gamma = T$$, we have $$f(\tau + 1) = f(\tau)$$. From the theory of complex analysis, we know that such a periodic function admits a Fourier expansion and thus $$f(\tau) = \sum_{n \geq - m}a_{f}(n)q^{n}$$, where $$q = e^{2\pi i\tau}$$ and $$a_{f}(n)$$ are called Fourier coefficients. The partition function $$p(n)$$ are Fourier coefficients of $$q^{- \frac{1}{24}}\eta(q)$$, where $$\eta(\tau)$$ is the Dedekind eta function [^5], defined by $$\eta(\tau) ≔ q^{\frac{1}{24}}\prod\limits_{n \geq 1}\left( 1 - q^{n} \right)$$. For a more brief overview on modular forms, we refer to [3].

In the next section, we will see how these two topics, seemingly different, comes together to address Problem 1.1.

## Asymptotic Formula for $$p(n)$$



In 1918, using the modularity of $$P$$, Hardy and Ramanujan [9] developed the Circle Method and found an asymptotic series for $$p(n)$$. The simplest form of their result reads


$$p(n) \sim \frac{1}{4n\sqrt{3}}e^{\pi\sqrt{\frac{2n}{3}}}\text{ as }n \rightarrow \infty.$$


A few years later, Uspensky [19] independently discovered this. In [9, equation (2.11)], Hardy and Ramanujan first proved that there exist $$H,K > 0$$ such that for $$n \in {\mathbb{N}}$$, $$\frac{H}{n}e^{2\sqrt{n}} < p(n) < \frac{K}{n}e^{2\sqrt{2n}}$$. Thus, the next step is to determine $$C$$, where $$C = \lim\limits_{n \rightarrow \infty}\frac{\log p(n)}{\sqrt{n}}$$, which is documented in [9, Section 3]. Next, applying the Cauchy integral formula, we have


$$p(n) = \frac{1}{2\pi i}\int_{\Gamma}\frac{P(q)}{q^{n + 1}}dq,$$


 {% include figure.html image='/Hardy.jpg' caption='_**G. H. Hardy** (1877–1947), whose analytic approach and development of the Circle Method led to the first asymptotic formula for the partition function $$p(n)$$._' width=400 %}
 

where the path $$\Gamma$$ encloses the origin and lies entirely inside the unit circle. Truncating (1.1), we observe that $$P_{N}(q) ≔ \prod_{n = 1}^{N}\frac{1}{1 - q^{n}}$$ has a pole at $$q = 1$$ of order $$N$$, a pole at $$q = - 1$$ of order 
$$$$
, poles at $$q = e^{\frac{2\pi i}{3}}$$ and $$q = e^{\frac{4\pi i}{3}}$$ of order 
$$$$
, and so on. Hardy and Ramanujan defined the following auxiliary function $$F(q) ≔ \frac{1}{\pi\sqrt{2}}\sum_{n \geq 1}\Psi(n)q^{n}$$, where $$\Psi(n) ≔ \frac{d}{dn}\left( \frac{\cosh C\lambda_{n} - 1}{\lambda_{n}} \right)$$, $$C = \pi\sqrt{\frac{2}{3}}$$, and $$\lambda_{n} = \sqrt{n - \frac{1}{24}}$$. Now the behaviour of $$P$$ and $$F$$ is similar inside the unit circle and in the neighbourhood of $$q = 1$$. Applying Cauchy"s integral formula for $$P - F$$, they obtain the first term of the asymptotic series


$$p(n) = \frac{1}{2\pi\sqrt{2}}\frac{d}{dn}\left( \frac{e^{C\lambda_{n}}}{\lambda_{n}} \right) + O\left( e^{D\sqrt{n}} \right)$$


where $$D > \frac{C}{2}$$. Taking $$n \rightarrow \infty$$, (3.3) gives (3.1). But how close the formula (3.3) with real values of $$p(n)$$? For example, taking $$n \in \left\{ 61,62,63 \right\}$$, (3.3) gives $$1121538.672,1300121.359,1505535.606$$, whereas the exact values are $$1121505,1300156,1505499$$. So the errors alternate in sign. To explain this factor, the same principle is applied near the point $$- 1$$ on the unit circle which contributes to the second term in the series for $$p(n)$$; i.e.,


$$\begin{aligned}
p(n) & = \frac{1}{2\pi\sqrt{2}}\frac{d}{dn}\left( \frac{e^{C\lambda_{n}}}{\lambda_{n}} \right) + \frac{( - 1)^{n}}{2\pi}\frac{d}{dn}\left( \frac{e^{\frac{C\lambda_{n}}{2}}}{\lambda_{n}} \right) + O\left( e^{D\sqrt{n}} \right),
\end{aligned}$$


where $$D > \frac{C}{3}$$. This process can be continued further by taking into consideration the points on the unit circle where $$P$$ has singularities. For example, the singularities which are important after $$q = - 1$$ are $$q = e^{\frac{2\pi i}{3}}$$ and $$q = e^{\frac{4\pi i}{3}}$$, and so on. The major obstacle to proceeding systematically is to construct the auxiliary functions associated with the points $$q = e^{\frac{2\pi ih}{k}}$$ of singularity lying on the unit circle. To illustrate this, define $$F_{h,k}(q) ≔ \omega_{h,k}\frac{\sqrt{k}}{\pi\sqrt{2}}F_{\frac{C}{k}}\left( q_{h,k} \right)$$, where $$\omega_{h,k}$$ is a $$24$$th root of unity, $$q_{h,k} = qe^{\frac{- 2\pi ih}{k}}$$, and for $$\alpha$$ being positive and independent of $$n$$, define


$$\Phi(q) ≔ P(q) - \sum\limits_{k = 1}^{\alpha\sqrt{n}}\sum\limits_{\begin{array}{r}
1 \leq h \leq k \\
(h,k) = 1
\end{array}}F_{h,k}(q)$$


If then $$F_{h,k}(q) = \sum c_{h,k,n}q^{n}$$, we obtain from Cauchy integral formula,


$$p(n) - \sum\limits_{k = 1}^{\alpha\sqrt{n}}\sum\limits_{\begin{array}{r}
1 \leq h \leq k - 1, \\
(h,k) = 1
\end{array}}c_{h,k,n} = \frac{1}{2\pi i}\int_{\Gamma}dq\left( \Phi(q) \right)/\left( q^{n + 1} \right),$$


where $$\Gamma$$ is a circle of radius $$R < 1$$ and its center is the origin. By dissecting the circle $$\Gamma$$ by means of Farey series and computing the bounds of the integral on the right-hand side of (3.5), Hardy and Ramanujan finally proved that the error term is of order $$O\left( \frac{1}{n^{4}} \right)$$. The final form of their formula for $$p(n)$$ can be stated as follows.

**Theorem 3.1.** _There exists an $$\alpha \in {\mathbb{R}}_{> 0}$$ such that $$n \gg 1$$,_


$$\begin{aligned}
p(n) & = \frac{1}{2\pi\sqrt{2}}\sum\limits_{k = 1}^{\alpha\sqrt{N}}\sqrt{k}A_{k}(n)\frac{d}{dn}\left( \frac{e^{\frac{C\lambda_{n}}{k}}}{\lambda_{n}} \right) + O\left( n^{- \frac{1}{4}} \right),
\end{aligned}$$


where


$$$$


 {% include figure.html image='/Rademacher.jpeg' caption='_**Hans Rademacher** (1892–1969), who perfected the Hardy–Ramanujan circle method and obtained a convergent exact series for the partition function $$p(n)$$._' width=400 %}
 

To know in detail about this collaboration, we refer the reader to [13, 17]. We end this discussion by quoting further two instances for verifying (3.6) with the actual values of $$p(n)$$. MacMahon [^6] computed values of $$p(n)$$ for $$1 \leq n \leq 200$$. The actual values for


$$p(100) = 190569292\ \text{ and }\ p(200) = 3972999029388,$$


whereas if taking the first six terms of (3.6) for $$n = 100$$ and first eight terms of (3.6) for $$n = 200$$ gives


$$p(100) \approx 190569291.996\text{ and }p(200) \approx 3972999029388.004.$$


This proves the accuracy of the formula (3.6). In [9, Section 6, 6.22], they remarked that it remains unanswered whether the infinite series (by extending $$n \rightarrow \infty$$ in (3.6)) is convergent or divergent and if it is convergent, then whether it represents $$p(n)$$. Lehmer [11] proved that (3.6) is divergent when $$N \rightarrow \infty$$. In the fall of 1936, Rademacher [^7] [15] perfected the Hardy–Ramanujan circle method and derived a convergent infinite series for $$p(n)$$ stated below


$$p(n) = \frac{1}{\pi\sqrt{2}}\sum\limits_{k \geq 1}\sqrt{k}A_{k}(n)\left\lbrack \frac{d}{dx}\left( \frac{\sinh\left( \frac{\pi}{k}\left( \frac{2}{3}\left( x - \frac{1}{24} \right) \right)^{\frac{1}{2}} \right)}{\left( x - \frac{1}{24} \right)^{\frac{1}{2}}} \right) \right\rbrack_{x = n}.$$


 {% include figure.html image='/Ramanujan.jpeg' caption='_**Srinivasa Ramanujan** (1887–1920), whose deep insights into partitions and modular forms were central to the asymptotic theory of the partition function $$p(n)$$._' width=400 %}
 

He [15] also proved that if the series (3.7) is truncated after $$N$$ terms, the absolute value of the error is bounded by


$$\frac{2\pi^{2}}{9\sqrt{3N}}e^{\frac{\pi}{N + 1}\sqrt{\frac{2n}{3}}},$$


which tends to $$0$$ as $$N \rightarrow \infty$$. If we truncate the series (3.7) at $$N$$ and compare it with (3.6), it clearly shows two significant differences between them:


+ In (3.6), the parameters $$n$$ and $$N$$ are entangled whereas in (3.7), we have the complete freedom over $$n$$ and $$N$$. 
+ The exponential function in (3.6) is replaced by hyperbolic trigonometric function (precisely $$\sinh$$) in (3.7) which made the series convergent.

So, summarizing the topics covered above, we see that how through a simple counting function $$p(n)$$, three different domains (in fact many more which is beyond the scope to present in this short exposition) in mathematics come together so that (3.7) comes into existence, like a piece of music where different notes and tones sequentially placed make a harmony to give a birth of ragas or symphonies.

## Acknowledgements



The author has received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 101001179). The author thanks Soumya Bhattacharya and IISER Kolkata for its warm hospitality during the conference entitled "Primes, Patterns & Propagation" during 08–12 December, 2025. 

## Footnotes

[^1]: We will discuss the importance in the final section.
 
[^2]: Among many others, the most celebrated one is perhaps Euler–Maclaurin summation formula.
 
[^3]: This discrete subgroup is also called the _full modular group_.
 
[^4]: This condition is called _Modularity_.
 
[^5]: This is a modular form of weight $$\frac{1}{2}$$
 
[^6]: See the table [9, page 377-378]
 
[^7]: Selberg [17, page 705] came up with the same formula Equation (3.7) for $$p(n)$$ around the same time but never published his result when he came to know that Rademacher already had it.
