---
author-affiliation:
- IMSc, India
- CMI, India
author-bio: '**Anup Dixit** is an Assistant Professor at the Institute of Mathematical Science (IMSc) India. His research interest lies in number theory. Apart from various outreach programs for school students, he is also involved in training students for the Mathematics Olympiad.<br><br>**Siddhi Pathak** is an Assistant Professor at the Chennai Mathematical Institute (CMI). Her research focuses on topics in number theory. She is a corresponding editor for the mathematics magazine "Bhavana".'
authorImage: anupSiddhi.png
authors:
- Anup Dixit
- Siddhi Pathak
category: article
date:
  day: 22
  month: 12
  year: 2025
excerpt: "Prime numbers appear to be scattered at random, yet their overall distribution follows striking statistical laws. This article explores how probabilistic thinking\u2014especially Cram\xE9r\u2019s random model for primes\u2014helps predict typical gaps between primes while revealing surprising limitations. Along the way, it shows how randomness and arithmetic structure coexist in one of mathematics\u2019 oldest problems."
hero-image: primes.svg
issue: 7
permalink: /issue7/anup-dixit-probability/
refs-file: null
title: Patterns In Primes Via Probability
---


## Introduction

The idea of a _number_ lies at the very foundation of human civilization. Some of the earliest archaeological records of writing already reveal an awareness of natural numbers, marking a crucial step in the development of abstract thought. Reflecting on this, R. Dedekind famously wrote that "numbers are free creations of the human intellect; they serve as a means of grasping more easily and more sharply the diversity of things". Since numbers provide a lens through which we interpret the world, their study has fascinated mathematicians for centuries.

One of the earliest and most profound discoveries in mathematics, dating back to Euclid, is that every natural number can be written as a product of prime numbers. In this sense, primes serve as the fundamental building blocks of arithmetic. A _prime number_ is a natural number $$n > 1$$ that has no divisors other than 1 and itself. For instance, 2, 3, 5, 7, and 11 are prime, whereas $$9 = 3^{2}$$ is not. The study of prime numbers has attracted many of the greatest mathematicians, including Euler, Gauss, Dirichlet, and Riemann.

{% include figure.html image='primes100.jpg' caption='Apparent lack of patterns among the primes.' width=700 %}

 One of the first striking facts about primes is Euclid’s theorem asserting that there are infinitely many of them. Yet even a brief inspection of the primes among the first 100 natural numbers reveals an apparent lack of regularity. Aside from the trivial observation that all primes except 2 are odd, no simple pattern emerges. It is therefore unsurprising that there is no fast and fully deterministic procedure for locating very large primes. Indeed, the largest known prime as of December 2025 is 

$$2^{136,279,841} - 1,$$

 a number discovered through extensive computation rather than a simple formula.

Despite this apparent irregularity, prime numbers exhibit remarkable _statistical_ regularities. In the late eighteenth century, Adrien-Marie Legendre and Carl Friedrich Gauss independently observed, based on extensive numerical evidence, that the number of primes up to a large number $$N$$ satisfies 

$$\pi(N): = \#\left\{ p \leq N:p\text{ is prime } \right\} \sim \frac{N}{\log N}\text{ as }N \rightarrow \infty.$$

 Gauss further suggested that primes occur near a large number $$n$$ with density approximately $$1/\log n$$, leading to the refined approximation 

$$\pi(N) \sim \int_{2}^{N}\frac{\text{ dt }}{\log t} = :\text{ li}(N),$$

 known as the _logarithmic integral_. This approximation is surprisingly accurate: for example, there are exactly 78498 primes below $$10^{6}$$, while $$\text{li}\left( 10^{6} \right) \approx 78627$$, an error of only about $$0.16\%$$.

{% include figure.html image='hexagon.pdf' caption='The above construction represents numbers in a hexagonal pattern (the innermost hexagon shows 1 through 6, and then the numbers keep spiralling outward). The green mini hexagons represent prime numbers, and their frequency decays as the numbers get bigger (from inside to outside). This relationship is consistent with the prime number theorem which says that the frequency of prime numbers goes down as $$1/\log n$$. [Idea for the hexagonal representation - Quanta Magazine]' width=700 %}

This observation, now known as the _Prime Number Theorem_, was proved independently by Jacques Hadamard and Charles Jean de la Vall'ee Poussin in 1896, building on ideas introduced earlier by Riemann. Thus, although primes may appear erratic, their overall distribution follows a precise and elegant law.

Still, the intuition that primes behave in many ways like an unpredictable sequence remains useful. In this article, we explore how this perspective can lead to meaningful predictions, focusing in particular on the behavior of gaps between consecutive primes. The smallest possible gap is 2, as seen in twin primes such as $$(3,5)$$ or $$(11,13)$$. On the other hand, by considering the numbers 

$$n! + 2,n! + 3,\ldots,n! + n,$$

 one can construct arbitrarily long stretches of composite numbers, and hence arbitrarily large gaps between primes. This naturally raises the question: near a large number $$N$$, what should a _typical_ gap between consecutive primes look like? {% include figure.html image='Urns.jpg' caption='Cramér’s conjecture is a prediction about how large the gaps between consecutive prime numbers can get. Using a probabilistic model in which an integer near $$n$$ is “randomly prime” with probability $$1/\log n$$, Cramér argued that unusually large gaps should be rare and that the largest prime gaps near $$n$$ should grow no faster than about $$\left( \log n \right)^{2}$$. In simple terms, the conjecture says that although prime gaps do grow without bound, they grow much more slowly than the primes themselves, and their size is tightly constrained by logarithmic factors.' width=700 %}

To investigate this, consider an interval $$\lbrack N,N + H\rbrack$$, where $$N$$ is large and $$H$$ is much smaller than $$N$$, but still large enough to contain many primes. The Prime Number Theorem predicts that the number of primes in this interval is approximately 

$$\pi(N + H) - \pi(N) \approx \frac{H}{\log N}.$$

 Dividing the length of the interval by the number of primes it contains suggests that the _average_ gap between consecutive primes near $$N$$ is about $$\log N$$. This reasoning also reinforces Gauss’s original insight that roughly one out of every $$\log N$$ numbers near $$N$$ is prime.

This line of thought inspired the Swedish mathematician Harald Cramér in 1936 to introduce a probabilistic model for primes. Imagine an infinite sequence of urns 

$$\left( U_{n} \right)_{n \in \mathbb{N}}.$$

 The urn $$U_{1}$$ contains only blue balls, $$U_{2}$$ only red balls, and for $$n \geq 3$$, the urn $$U_{n}$$ contains both colors. Suppose that when drawing a ball from $$U_{n}$$, the probability of obtaining a red ball is $$1/\log n$$. Drawing independently from each urn produces an infinite sequence of red and blue outcomes. Let $$P_{n}$$ denote the index of the urn from which the $$n$$-th red ball is drawn. The resulting sequence $$\left( P_{n} \right)_{n \in \mathbb{N}}$$ is increasing and serves as a model for the sequence of prime numbers.

{% include figure.html image='gaps.pdf' caption='A histogram of gaps between consecutive prime numbers in a large numerical range. While individual prime gaps fluctuate irregularly, the distribution as a whole reflects the Prime Number Theorem: most gaps cluster around a size comparable to $$\log N$$ for primes near N. This visualization supports the heuristic argument that, despite their apparent randomness, primes obey predictable average behavior—an idea that motivates probabilistic models such as Cramér’s and underlies modern conjectures on extreme prime gaps. [Source: _InScight_]' width=700 %}

 If we define 

$$\Pi(N): = \#\left\{ n \in \mathbb{N}:P_{n} \leq N \right\},$$

 then 

$$\mathbb{E}\left\lbrack \Pi(N) \right\rbrack = \sum_{n = 1}^{N}\frac{1}{\log n} \approx \text{ li}(N) \approx \frac{N}{\log N}.$$

This mirrors the behavior of $$\pi(N)$$, reinforcing the analogy between $$\left( P_{n} \right)$$ and the primes. In particular, one may expect the largest gaps between primes to resemble the largest gaps between successive $$P_{n}$$.

Using results from probability theory, Cramér showed that with probability one, 

$$\limsup\limits_{n \rightarrow \infty}\frac{P_{n + 1} - P_{n}}{\left( \log P_{n} \right)^{2}} = 1.$$

 Motivated by this, he conjectured that prime gaps satisfy a similar bound.

**Conjecture 1** (Cramér’s Conjecture)<br>
 Let $$2 = p_{1} < p_{2} < p_{3} < \ldots$$ be the sequence of prime numbers. 
+ (Strong form) $$\limsup\limits_{n \rightarrow \infty}\frac{p_{n + 1} - p_{n}}{\left( \log p_{n} \right)^{2}} = 1$$ 
+ (Weak form) $$p_{n + 1} - p_{n} \ll \left( \log p_{n} \right)^{2}$$

Although powerful, Cramér’s model is undeniably simplistic. It ignores basic arithmetic constraints, such as the fact that all primes except 2 are odd, or that no number divisible by 3 can be prime. Consequently, relying on the model without modification can lead to misleading predictions.

A striking example concerns twin primes—pairs of primes $$(p,p + 2)$$. While it is widely believed that infinitely many twin primes exist, this remains unproven. Cramér’s model predicts that the number of twin primes up to $$N$$ should be approximately 

$$\sum_{n = 2}^{N}\frac{1}{\log(n)\log(n + 2)} \approx \frac{N}{\left( \log(N) \right)^{2}}$$

 However, the same reasoning would predict a similar number of _consecutive_ primes, which is clearly impossible beyond the pair $$(2,3)$$. This illustrates the limitations of the model.

{% include figure.html image='gaussCramer.svg' caption='Gauss’s (left) empirical observations on the density of prime numbers led to the Prime Number Theorem and the logarithmic integral. Cramér’s (right) probabilistic model builds on this viewpoint to predict the typical and maximal size of gaps between consecutive primes, highlighting both the power and the limitations of treating primes as a random sequence.' width=700 %}

 Nevertheless, when refined to account for divisibility by small primes, Cramér’s framework yields more accurate predictions. Granville showed that such corrections replace the constant $$1$$ in the strong conjecture with $$2e^{- \gamma} \approx 1.229$$, where $$\gamma$$ is Euler’s constant. Similarly, the refined model predicts that the number of twin primes up to $$N$$ should be 

$$\sim 2C_{2}\frac{N}{\left( \log N \right)^{2}},\quad C_{2} = \prod_{p\text{ is prime}p \geq 3}\left( 1 - \frac{1}{(p - 1)^{2}} \right) \approx 0.66016$$

Cramér’s model also sheds light on the distribution of primes in short intervals. Under this framework, intervals $$\lbrack N,N + H)$$ with $$\left( \log N \right)^{2 + \delta} < H < N$$ typically contain about $$H/\log N$$ primes. In 1943, assuming the Riemann Hypothesis, A. Selberg showed that this holds for _almost all_ such intervals. For many years, it was believed that this behavior should hold uniformly. However, in a groundbreaking result, H. Maier demonstrated in 1985 that there are infinitely many short intervals where the number of primes deviates significantly from this expectation.

Seen in this light, Cramér’s model reveals both the power and the limitations of probabilistic reasoning in number theory. It captures the correct scale of prime gaps while falling short of fully encoding arithmetic structure. Its successes and failures together show why such models are best viewed as guiding principles rather than final answers. By exploring where the model works, where it breaks down, and how it can be refined, mathematicians continue to uncover subtle patterns beneath the surface, ensuring that the study of prime numbers remains a vibrant and evolving field.

