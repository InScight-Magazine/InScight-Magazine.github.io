---
author-affiliation:
- Visiting Professor,International Centre for Theoretical Sciences Bangalore, India.
author-bio: '*Sury* was at the TIFR in Bombay during 1981-1999 and at the I.S.I. in Bangalore during 1999-2025. He is an elected Fellow of the National Academy of Sciences, India and was the National Co-ordinator for the Mathematics Olympiad Programme in India. His areas of research interest are Algebra and Number Theory. At present, he is a Visiting Professor at ICTS-TIFR, Bangalore.'
authorImage: sury.jpeg
authors:
- B Sury
category: article
date:
  day: 7
  month: 12
  year: 2025
excerpt: "Sury offers a panoramic journey through Diophantine equations, weaving together history, puzzles, deep theorems, and modern breakthroughs\u2014from Diophantus and Fermat to elliptic curves, Hilbert\u2019s 10th problem, and the ABC conjecture. Blending rigorous mathematics with anecdotes, poetry, and cultural context, it reveals how deceptively simple integer equations lead to some of the most profound ideas in mathematics."
hero-image: Sury.svg
issue: 7
permalink: /issue7/b-sury-diophantus/
refs-file: surryrefs
title: The World of Diophantus
---

No excuse is needed to celebrate mathematics, but there are two special days selected by the community. The National Mathematics Day is celebrated in India on Ramanujan’s birthday, the 22nd of December but I defer the celebration of this to another time. The other one is Pi day, the 14th of March, which has been selected and universally accepted as the International Mathematics Day (there is actually a building in Hong Kong which is shaped like π). Regarding this choice of π-day, I would say:

> We had this year’s Pi Day
> 
> nine months back on a Friday.
> 
> To Pi, 22 by 7 is closer
> 
> but somehow 3.14 is kosher.
> 


## Diophantus of Alexandria


{% include figure.html image='diophantus.jpeg' caption='Diophantus of Alexandria, Egypt lived during the 3rd century AD. Joseph-Louis Lagrange called Diophantus "the inventor of algebra".' width=700 %}

Metrodorus indicated the life span of Diophantus through a puzzle poetically as: 
> ’Here lies Diophantus,’ the wonder behold.
> 
> Through art algebraic, the stone tells how old:
> 
> ’God gave him his boyhood one-sixth of his life,
> 
> One twelfth more as youth while whiskers grew rife;
> 
> And then yet one-seventh ere marriage begun;
> 
> In five years there came a bouncing new son.
> 
> Alas, the dear child of master and sage
> 
> after attaining half the measure of his father’s life chill fate took him.
> 
 This puzzle implies that Diophantus’s age x =?? is a solution of the equation: 

$$x = \frac{x}{6} + \frac{x}{12} + \frac{x}{7} + 5 + \frac{x}{2} + 4.$$


For those who wish to verify the answer they got, here is a crossword type of hint: endless Hindustani Classical flautist!
Diophantus was interested in solving polynomial equations in many variables where he sought solutions in integers or, more generally, in rational numbers. He wrote a number of books titled ‘Arithmetica’ many of which have got lost. Thus, the nomenclature of Diophantine equations arose to describe the broad subject of finding integer solutions of polynomial equations. For instance, the Diophantine equation $$x^{2} + y^{2} = z^{2}$$ seeks integer triples (the so-called Pythagorean triples) describing the lengths of the sides of a right-angles triangle.
The amateur mathematician Pierre de Fermat had, in his copy of Bachet’s translation of Diophantus’s Arithmetica, made a famous marginal note which came to be known as Fermat’s last theorem and which is now a theorem. It says that for any n &gt; 2 there are no solutions of the equation $$x^{n} + y^{n} = z^{n}$$ in non-zero integers x, y, z; see the departure from the case $$n = 2$$ when we get infinitely many Pythagorean triples.
{% include figure.html image='bachet.jpeg' caption='Diophantus"s Arithmetica by Bachet. Arithmetica is the major work of Diophantus and the most prominent work on premodern algebra in Greek mathematics. It is a collection of 290 algebraic problems giving numerical solutions of determinate equations (those with a unique solution) and indeterminate equations.' width=700 %}

In regard to the history of Fermat’s last theorem, many famous mathematicians like Cauchy had unsuccessfully attempted (and thought to have solved) it. The first seriously successful attempt was by Kummer when he proved Fermat’s assertion for certain types of primes called regular primes. Sophie Germain (who had to go under an alias of a male name as women were not allowed to enrol at the university at that time) was a protege of Gauss and she proved the truth of Fermat’s assertion when the exponent $$n$$ is a prime p such that $$1 + 2p$$ is also a prime. Only in the 1980s, the whole picture changed with the advent of highly state-of-the-art methods into this topic by Gerd Faltings, Gerhard Frey, Kenneth Ribet and finally ending with the deep work of Andrew Wiles supported by Richard Taylor. One might say:

> Solved first by the great Cauchy.
> 
> What a mistake made - Gosh, he!
> 
> Then it was Kummer’s time.
> 
> He did every regular prime.
> 
> Germain came and shouted ‘Whoopee!
> 
> Done, if we know about 1 + 2p’.
> 
> The uproar after Faltings, Gerd
> 
> went ‘Mordell’s done; spread the good word!’
> 
> We know who then jumped into the fray
> 
> whose elliptic curve could exist no way!
> 
> Ribet said ‘Taniyama does
> 
> put a stop to all this fuss!’
> 
> And then Wiles was heard telling Taylor
> 
> now’s the time; let’s go and nail her!’
> 
> We conclude from this saga of Fermat
> 

The problem of finding integer solutions of polynomial equations is so basic and ubiquitous that it is not surprising Diophantine equations arise in diverse situations from the most abstract to the very concrete. In the following article, we take a peek into many Diophantine equations that arise in mathematics ranging from the recreational kind of questions to those that are more fundamental and deeper.

## Sums of Powers

 Fermat had conjectured that every positive integer is a sum of four squares of integers. Later in 1770, Waring conjectured that every positive integer N is a sum of at the most 9 cubes of positive integers. This was proved by Wieferich (1909) - with a correction carried out by Kempner (1912). In fact, if N is large enough, 7 cubes suffice (Linnik 1942); can 7 be reduced to 6 or 5 or 4? The answer is still unknown.
If we allow cubes of negative integers also, then 5 cubes suffice but, it is again unknown if 4 cubes suffice. Therefore, the problem as to which integers are sums of three integer cubes becomes very interesting.
Regarding this last question, by 2021, the only two elusive cases of 33 and 42 remained among the numbers up to 100. This was finally settled by Andrew Booker from Bristol, and Andrew Sutherland from MIT - authorities on parallel computations. They used ‘Charity Engine’, a world-wide computer that harnessed idle, unused computing power from over 500000 home PCs to create a crowd-sourced platform.
The most difficult case of 42 resolved using a computing platform reminiscent of ‘Deep Thought’, the giant machine which gave the answer 42 in Douglas Adams’s Hitchhiker’s Guide to the Galaxy. For those who have not had the pleasure of reading this work, we recall from it: The Earth was actually a giant supercomputer, created by another supercomputer, Deep Thought. ‘Deep Thought’ built by its creators to give the answer to the “Ultimate Question of Life, the Universe, and Everything”. After eons of calculations, the answer was given simply as “42”. Deep Thought was then instructed to design the Earth supercomputer to determine what the Question actually is!
For the sake of those who are interested, here is the solution expressing 42: 

$$42 = ( - 80538738812075974)^{3} + (80435758145817515)^{3} + (12602123297335631)^{3}.$$


In passing, we mention that it is easy to see the smallest solutions to expressing 3 as a sum of three cubes of integers are: 

$$3 = 1^{3} + 1^{3} + 1^{3} = 4^{3} + 4^{3} + ( - 5)^{3.}$$

 For those who wonder how big the next solution could be, here it is: 

$$3 = (5699368212219628380720)^{3} + ( - 569936821113563493509)^{3} + ( - 472715493453327032)^{3.}$$

 Concerning such questions, Terence Tao suggests as a challenge for the clairvoyant:

> It occurs to me that these sorts of questions would be excellent challenge questions to pose to any psychics who claim to be in contact with superintelligent aliens, since the solutions are already expected to be produced by computer search in a few years but would be instantly verifiable evidence of some extraordinary computational or intellectual resource if produced sooner.


## The Fab cab

 Everyone must have heard of the famous taxicab number 1729 and Ramanujan’s story thanks to Mahalanobis, who was a contemporary of Ramanujan at Cambridge (and who actually taught him for the first time how to get inside an English bed after realizing that for months Ramanujan had been freezing without being privy to this know-how). The Ramanujan taxicab number concerns the Diophantine equation $$x^{3} + y^{3} = 1729$$. When Hardy mentioned that the taxicab he travelled bore the number 1729 and this number appeared dull to Hardy, Ramanujan immediately responded that this was far from a dull number as it was the smallest positive integer which is a sum of two cubes of integers in two different ways. The two integer solutions (12, 1) and (10, 9) are the only ones which is easy to prove, but a nice exercise it to check that each number < 1729 has at the most one expression as a sum of two cubes.
However, in this context, what may not be well-known is that $$x^{3} + y^{3} = 1729$$ has infinitely many rational solutions. For instance, if u, v is a solution, then so is $$U = u\left( u^{3} - 3458 \right)/\left( 1729 - 2u^{3} \right)$$ and $$V = v\left( u^{3} + 1729 \right)/\left( 1729 - 2u^{3} \right)$$.
{% include figure.html image='ramanujan.jpeg' caption='Ramanujan (1887-1920) from India was deeply interested in Diophantine equations, contributing explicit solutions to sums of two cubes and to Pell-type equations using continued fractions.' width=700 %}
 
## Enter Sylvester

 As alluded to earlier, Diophantine equations are polynomial equations for which one seeks integer or rational solutions. Existence of rational solutions is often an easier problem to study than that of determining if integer solutions exist. A heuristic reason is that the set of rational solutions may have a much better structure - for instance it often has the structure of a group where two rational points can be composed to give a new third rational point. For example, a Diophantine equation like $$y^{2} = x^{3} + 54$$ has only two integer solutions (x, y) = (3, 9), (3,−9) whereas if we consider a picture of the real locus of this equation, one may produce a new point with rational co-ordinates from two points with rational co-ordinates simply by drawing a chord between the two points and then reflecting about the x-axis the third point where this chord intersects the graph. To start with one can draw the tangent at (3, 9) and take the point where it cuts the graph and reflecting that point. In this manner, we can produce infinitely many solutions with rational co-ordinates! Of course, an equations like $$y^{2} = f(x)$$ with $$f(x)$$ a cubic polynomial with distinct roots are special; they are called ‘elliptic curves’ and they have a group law as described above where two points give rise to a third point.
Many classical problems lead to Diophantine equations which involve elliptic curves. One such is a problem due to Sylvester. Determining which integers n are sums of TWO rational cubes, has a rich history tracing back to Sylvester who predicted that prime numbers p which leave a remainder 2 or 5 when divided by 9 are not sums of two rational cubes, while primes which leave a remainder of 4, 7, or 8 are sums of two rational cubes. In contrast, primes p that leave a remainder of 1 or 8 when divided by 9 may or may not be sums of two rational cubes. The problem gets related to the elliptic curve $$y^{2} = x^{3} - 432p^{2}$$. Only very recently the last prediction mentioned above (considered particularly difficult) has been proved for infinitely many prime numbers.
In passing, we mention an amusing anecdote involving Sylvester. While teaching in the United States, he had an encounter with an unruly student and believed that the student had been fatally wounded by Sylvester during a skirmish. Sylvester returned to England still under the mistaken impression that he had killed a student! While in England, he had tutored many people in mathematics and statistics, one of whom was Florence Nightingale. Sylvester was also responsible for introducing several interesting names in mathematics - like syzygy.

## Not as easy as Pi


Like the Diophantine equations, a related notion that arises in many situations is that of Diophantine approximation - we briefly mention one place where π occurs. Here is a routine-looking question? Is the infinite series $$\Sigma\frac{1}{n^{3}\sin^{2}(n)}$$ convergent?
The convergence of the series depends on the behavior of the sequence $$n|\sin(n)|$$ as $$n$$ gets infinitely large and, this behavior is mysterious. It depends on how well can $$\pi$$ be approximated by rational numbers - something unknown as yet! To make it a bit more precise, we briefly describe something called the _irrationality measure_ $$\mu(\alpha)$$ of an irrational number α.Consider the positive numbers a &gt; 0 for which the distance $$|\alpha - p/q|$$ of $$\alpha$$ from a rational number can be less than the quantity $$1/q^{a}$$ only for finitely many $$p,q$$. The smallest (or the infimum of) all such $$a > 0$$ is defined to be the irrationality measure of $$\alpha$$. It quantifies how well-approximable the number $$\alpha$$ is by rational numbers.
The Dirichlet box principle implies that the irrationality measure $$\mu(\alpha) \geq 2$$ and generically (that is, almost all) $$\alpha$$ have $$\mu(\alpha) = 2$$. For a specific number, it is difficult to find $$\mu$$; for instance, $$\mu(e) = 2$$ but, the constant $$\mu(\pi)$$ is still unknown! One knows $$\mu(\pi) < 8$$ but not much more is known Here is the shocker - the series 

$$\Sigma\frac{1}{n^{3}\sin^{2}(n)}$$

 diverges if $$\mu(\pi) > \frac{5}{2}$$ and converges if, $$\mu(\pi) < \frac{5}{2}$$. So, take your pick! Before we move on to other things, we recall an interesting mnemonic to remember the first few digits of $$\pi$$:

> Now I want a drink, alcoholic of course, after the heavy lectures involving quantum mechanics!”

{% include figure.html image='pcm.jpeg' caption='Mahalanobis(1893- 1972) engaged with Diophantine problems and played a role in sustaining and promoting mathematical research traditions in India.' width=700 %}
 
## Hilbert’s 10th problem

 We already mentioned that many problems of mathematics can be formulated as seeking solutions of certain Diophantine equations. However, this statement goes much further. In a sense of formal mathematical logic, every mathematical problem can be so formulated! This is formally the so-called Hilbert’s 10th problem - one of the 23 problems posed by david Hilbert during the 1900 International Congress of Mathematicians to lead the way for mathematics in the next several years.
Hilbert’s famous 10th problem asserted: 
> Given a diophantine equation with any number of unknown quantities and with rational integral numerical coefficients: To devise a process according to which it can be determined by a finite number of operations whether the equation is solvable in rational integers.

As it turned out, the answer was obtained in 1970 and unfortunately, it turned out to be negative. More precisely, the resolution due to Martin Davis, Putnam, Julia Robinson and Yuri Matiyasevich proves that there is no general algorithm that, given any Diophantine equation, decides whether it has solutions in positive integers or not. In more technical terms, the notions of ‘effectively enumerable’ sets and ‘Diophantine’ sets coincide.
The ideas appearing in the resolution of the 10th problem yield interesting implications such as:

> There exists a polynomial in 26 variables for which the set of positive values when the variables take positive integer values, equals the set of prime numbers!
 One can write the polynomial down explicitly using the symbols a to z for the 26 variables.

## Pell-Mell

 We discuss a type of equation that arises in many contexts and we start with an elementary problem that leads to it.
Think of a fruit-seller arranging her fruits in a triangular pattern in the morning and in a square pattern in the evening. Can she do both of these with the same number of fruits? For instance, if he has 36 fruits, he can do this because $$6^{2} = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8$$. Which other squares are so expressible as ‘triangular numbers’?
If $$n^{2} = 1 + 2 + \ldots + k = k(k + 1)/2$$, then $$8n^{2} = 4k(k + 1) = (2k + 1)^{2} - 1$$. Thus, $$(2k + 1,2n)$$ is a solution of the equation $$x^{2} - 2y^{2} = 1$$. Being aestheticallyminded fruit-sellers, all of us of course want to know what the solutions of $$x^{2} - 2y^{2} = 1$$ are! Before addressing how to solve this equation, we jump to another instance when the same equation arises and it involves Ramanujan.
In the Strand magazine, Mahalanobis had seen the following problem which he mentioned to Ramanujan: Imagine that you are on a street with houses marked 1 through n. There is a house in between such that the sum of the house numbers to the left of it equals the sum of the house numbers to its right. If n is between 50 and 500, what are n and the house number? Ramanujan thought for a moment and replied “Take down the solution” and dictated something called a ‘continued fraction’ (to be explained below) saying that it contained the solution! Evidently, Ramanujan wanted to have some fun instead of directly giving the answer! So, what is behind this?
If the house number is $$r$$, then we have 

$$1 + 2 + \ldots + (r - 1) = (r + 1) + \ldots + n$$

 The LHS is $$(r - 1)r/2$$ and if we add $$1 + 2 + \ldots + r = \frac{r(r + 1)}{2}$$ to both sides, we have $$r^{2} = n(n + 1)/2$$ . Multiplying by 8 and adding 1, we have $$8r^{2} + 1 = (2n + 1)^{2}$$, the very same equation encountered by the fruit-seller! One can similarly look at $$m^{2} - dn^{2} = 1$$ for any square-free positive integer d.These equations are popularly (and erroneously!) known as _Pell equations_. Interestingly, it turns out that there are infinitely many pairs m, n of positive integer solutions of $$m^{2} - dn^{2} = 1$$ and essentially, they are all generated froma single pair. The ancient Indian mathematicians (especially Brahmagupta,Bhaskara II and Jayadeva) studied the equations $$x^{2} - dy^{2} = \pm 1$$ and solved them. What is more - they gave an algorithm (the so-called Chakravala or cyclic method) which produces all the solutions.
{% include figure.html image='indianMaths.svg' caption='From left, Brahmagupta (598-670 AD) formulated general solutions for quadratic Diophantine equations and composition rules, while Bhaskaracharya (1114-1185 AD) systematized and perfected the Chakravāla method for solving equations of the form $$x^{2} - Ny^{2} = 1$$.' width=700 %}

In 1657, Fermat, writing to his friend Frenicle, he posed “to the English mathematicians and all others” the problem of finding a solution of $$x^{2} - Ny^{2} = 1$$ “pour ne vous donner pas trop de peine” like N = 61, 109.
The 20th century great Andr´e Weil’s comment on this was: “What would have been Fermat’s astonishment if some missionary, just back from India, had told him that his problem had been successfully tackled there by native mathematicians almost six centuries earlier ?”
Indeed, in 1150 A.D., Bhaskara II gave the explicit solutions 

$$$$

 Indeed, Brahmagupta (598-665) had already solved this equation in 628 A.D. for several values like N = 83 and N = 92.
Brahmagupta had remarked, “Kurvannaavatsaraad ganakah” - meaning (approximately), _“a person who is able to solve these within a year is truly a mathematician”’_ !
The wrong attribution to Pell of these equations is due to the most prolific of mathematicians - Leonhard Euler, but the name has stuck. In view of the above understanding of mathematical history, now the equations are being increasingly referred to as the Brahmagupta-Pell equations. Perhaps the oldest Diophantine equation to be considered is one posed by Archimedes (287 −212 B.C.) to Eratosthenes known as the cattle problem. We avoid the long wording and just state the modern equivalent which is to find the smallest solution of the equation 

$$X^{2} - 410286423278424Y^{2} = 1;$$

 it turns out that the smallest solution has at least 206545 digits.
We make a brief interlude on continued fractions and indicate how they are used in solving the Brahmagupta-Pell equations.
A simple continued fraction (SCF) is a nested expression


$$a_{0} + \frac{1}{a_{1}} + \frac{1}{a_{2}} + \ldots$$


where $$a_{i}$$ are integers and $$a_{n} > 0$$ for all n &gt; 0. That is, consider the sequence of fractions $$a_{0},a_{0} + \frac{1}{\ell_{1}}$$, where $$\ell_{1} = a_{1} + \frac{1}{\ell_{2}}$$, where $$\ell_{2} = a_{2} + \frac{1}{\ell_{3}}$$ etc. The above infinitely nested expression stands for the limiting value of the fractions $$\ell_{1},\ell_{2},\ell_{3},\ldots$$ (which can be easily shown to exist). The main point is every real number $$t$$ can not only be expanded as a decimal but also expanded as a simple continued fraction by the ‘greedy’ algorithm: Consider any real number $$t$$ which is not already an integer. Then, take $$a_{0}$$ to be the greatest integer $$\lbrack t\rbrack$$ not exceeding $$t$$. Next consider the real number


$$t_{1} ≔ \frac{1}{t - a_{0}} < 1.$$

 Take $$a_{1} = \left\lbrack t_{1} \right\rbrack$$ and consider $$\frac{1}{t_{1} - a_{1}}$$ etc. In this manner, we get a continued fraction expansion 

$$t = \left\lbrack a_{0};a_{1},a_{2},a - 3,\ldots \right\rbrack.$$

 It is easy to see that this is eventually periodic if and only if $$t$$ is the root of a quadratic polynomial with rational coefficients. For any square-free positive integer N, the SCF of $$\sqrt[N]{}$$ looks like $$\left\lbrack b_{0};\overline{b_{1},b_{2},\ldots,b_{n - 1},2b_{0}} \right\rbrack$$.
{% include figure.html image='fermat.jpeg' caption='Pierre de Fermat (August 17, 1601 to January 12, 1665). Fermat initiated the systematic study of Diophantine equations, introducing the method of infinite descent and posing problems that shaped number theory for centuries.' width=700 %}
 For instance, using the greedy algorithm, let us find the SCF for the irrational number$$\sqrt[7]{}$$.


$$\sqrt[7]{} = 2 + \left( \sqrt[7]{} - 2 \right) = 2 + \frac{3}{\sqrt[7]{} + 2} = 2 + \frac{1}{\left( \sqrt[7]{} + 2 \right)/3}.$$




$$\frac{\sqrt[7]{} + 2}{3} = 1 + \left( \frac{\sqrt[7]{} + 2}{3} - 1 \right) = 1 + \frac{\sqrt[7]{} - 1}{3}$$




$$\sqrt[7]{} - 2 = \frac{1}{1 +}\frac{\sqrt{7} - 1}{3} = \frac{1}{1 +}\frac{1}{\left( \sqrt{7} + 1 \right)/2} = \frac{1}{1 +}\frac{1}{1 +}\frac{\sqrt{7} - 1}{2} = \frac{1}{1 +}\frac{1}{1 +}\frac{1}{1 +}\frac{1}{\sqrt{7} + 2} = \frac{1}{1 +}\frac{1}{1 +}\frac{1}{1 +}\frac{1}{4 + \sqrt{7} - 2}$$


Thus, we have a repetition and 

$$\sqrt{7} - 2 = \frac{1}{1 +}\frac{1}{1 +}\frac{1}{1 +}\frac{1}{4 +}\frac{1}{1 +}\frac{1}{1 +}\frac{1}{1 +}\frac{1}{4 +}\ldots$$

 So, $$\sqrt[7]{} = \left\lbrack 2;\overline{1,1,1,4} \right\rbrack$$.
Here is the interesting thing about SCFs of $$\sqrt[N]{}$$ and their relation to the Pell equation $$x^{2} - Ny^{2} = 1$$. 

$$\sqrt[N]{} = \left\lbrack b_{0};\overline{b_{1},b_{2},\ldots,b_{n - 1},2b_{0}} \right\rbrack,$$

 the rational numbers $$b_{0} + 1/b_{1}$$,$$b_{0} + 1/\left( b_{1} + \left( 1/b_{2} \right) \right)$$ etc. are called convergents of the SCF. When the SCF is periodic like that for $$\sqrt[N]{}$$ , the penultimate convergent p_(n−1)/q_(n−1) before the recurring period gives a solution of $$x^{2} - Ny^{2} = ( - 1)^{n}$$. This is so simple to prove that it is explained in the classical school level text by Hall and Knight. This is how Ramanujan could give the solution to the house number problem quickly.
For example, $$\sqrt[7]{} = \left\lbrack 2;\overline{1,1,1,4},\ldots \right\rbrack$$ gives the penultimate convergent beforethe period to be [2;1,1,1] = 8/3.Then, (8, 3) is a solution of $$x^{2} - 7y^{2} = 1$$ (as the period is of even length). Note that $$x^{2} - 7y^{2} = - 1$$ has no solution as seen by looking at the remainders on dividing by 4.
Another example is $$\sqrt[13]{} = \left\lbrack 3;\overline{1,1,1,1,6},\ldots \right\rbrack$$ which has the penultimate convergent before the period to be [3; 1, 1, 1, 1] = 18/5. Then (18, 5) is a solution of $$x^{2} - 13y^{2} = - 1$$(as the period is of odd length). Think of this as the equality 

$$\left( 18 + 5\sqrt[13]{} \right)\left( 18 - 5\sqrt[13]{} \right) = - 1.$$

 From this a solution for $$x^{2} - 13y^{2} = 1$$ can be obtained by considering $$\left( 18 + 5\sqrt[13]{} \right)^{2} = 649 + 180\sqrt[13]{}$$. Then (649, 180) is a solution of $$x^{2} - 13y^{2} = 1$$.

## Congruent Number Problem

 This is one of the oldest problems in Diophantine equations. A natural number d is said to be a congruent number if there is a right-angled triangle with rational sides and area d. For example, 5, 6, 7 are congruent numbers. Of course, 6 is congruent as seen from the usual 3, 4, 5 triangle. To see that 5 is a congruent number, we consider the right-angled triangle with sides $$3/2,20/3,41/6$$. For 7, look at a right triangle with sides $$35/12,24/5,337/60$$. How did we guess this? More importantly, how do we decide if a given number is a congruent number? This will be done by relating it to another problem! This is the following one.
Can we have an arithmetic progression of three terms which are all squares of rational numbers and the common difference d? That is, can $$x^{2} - d,x^{2},x^{2} + d$$ be squares of rational numbers and x rational? The congruent number problem and the above question are equivalent!
Indeed, Let $$u \leq v < w$$ be the sides of a right triangle with rational sides. Then $$x = w/2$$ is such that $$\frac{(v - u)^{2}}{4},\frac{w^{2}}{4},\frac{(u + v)^{2}}{4}$$ form an arithmetic progression. Conversely, if $$x^{2} - d = y^{2},x^{2},x^{2} + d = z^{2}$$ are three rational squares in arithmetic progression, then: $$z - y,z + y$$ are the legs of a right angled triangle with rational legs, area $$\left( z^{2} - y^{2} \right)$$/2 = d and rational hypotenuse 2x because $$2\left( y^{2} + z^{2} \right) = 4x^{2}$$.
Now 1, 2, 3 are not congruent numbers. The fact that 1, 2 are not congruent numbers is essentially equivalent to Fermat’s last theorem for the exponent 4(!) Here is the argument. If $$a^{2} + b^{2} = c^{2},\frac{1}{2}ab = 1$$ for some rational numbers a, b, c then $$x = \frac{c}{2},y = |a^{2} - b^{2}\frac{|}{4}$$ are rational numbers satisfying $$y^{2} = x^{4} - 1$$. In terms of integers, this is the Diophantine equation $$u^{4} - v^{4} = w^{2}$$. As this has no non-zero integer solutions, it follows that 1 is not a congruent number. Similarly, if $$a^{2} + b^{2} = c^{2},\frac{1}{2}ab = 2$$ for rational numbers a, b, c, then $$x = \frac{a}{2},y = a\frac{c}{4}$$ are rational numbers satisfying $$y^{2} = x^{4} + 1$$. Again, the nonexistence of solutions shows that 2 is not congruent.
Here is a (rather unusual!) way of using the above fact that 1 is not a congruent number to show that √2 is irrational. Consider the right-angled triangle with legs √2,√2 and hypotenuse 2. If √2 were rational, this triangle would exhibit 1 as a congruent number! Though it is an ancient problem to determine which natural numbers are congruent, it is only in late 20th century that substantial results were obtained and progress has been made which is likely to lead to its complete solution. The rephrasing in terms of arithmetic progressions of squares emphasizes a connection of the problem with rational solutions of the equation $$y^{2} = x^{3} - d^{2}x$$; recall we referred to such equations as “elliptic curves”. It is easy to show that: The positive integer d is a congruent number if, and only if, the elliptic curve $$y^{2} = x^{3} - d^{2}x$$ has a solution with $$y \neq 0$$.
In fact, $$a^{2} + b^{2} = c^{2},\frac{1}{2}ab = d$$ implies $$bd/(c - a),2d^{2}/(c - a)$$ is a rational solution of $$y^{2} = x^{3} - d^{2}x$$. Conversely, a rational solution of $$y^{2} = x^{3} - d^{2}x$$ with $$y \neq 0$$ gives the rational, right-angled triangle with sides $$\left( x^{2} - d^{2} \right)/y,2xd/y,\left( x^{2} + d^{2} \right)/y$$ and area $$d$$.
In a nutshell, here is the reason we got this elliptic curve. The real solutions of the equation $$a^{2} + b^{2} = c^{2}$$ defines a surface in 3-space and so do the real solutions of $$\frac{1}{2}ab = d$$. The intersection of these two surfaces is a curve whose equation in suitable co-ordinates is the above elliptic curve! The connection with elliptic curves has been used, more generally, to show that numbers which are 1, 2 or 3 mod 8 are not congruent. This uses much deeper mathematics. Further, assuming the truth of a famous, deep, open conjecture known as the _weak Birch & Swinnerton-Dyer conjecture_, it has been shown that this is a complete characterization of congruent numbers.
{% include figure.html image='aweil.jpeg' caption='Andre Weil (May 6, 1906 to August 6, 1998) emphasized the structural depth of Diophantine equations, interpreting classical integer problems through algebraic curves and modern number-theoretic frameworks.' width=700 %}
 
## Arithmetic Progressions

 Here is a set of questions on arithmetic progressions of natural numbers which leads us to some very interesting Diophantine equations. Can we have a finite arithmetic progression 

$$a,a + d,a + 2d,\ldots,a + nd$$

 such that a first part $$a,a + d,\ldots,a + (r - 1)d$$ has the same sum as that of the second part $$a + rd,a + (r + 1)d,\ldots,a + nd$$? Note 

$$20 + 25 + 30 = 35 + 4014 + 21 + 28 + 35 + 42 + 49 = 56 + 63 + 70.$$

 More generally, we can try to break an arithmetic progression into THREE parts with equal sums; here, we mean that each of the three parts consist of consecutive terms. The answer turns out to be ‘No’ which we leave as an exercise for the interested reader.
A related question is whether we can have four perfect squares of positive integers in arithmetic progression. Well, if $$a^{2},b^{2},c^{2},d^{2}$$ are in arithmetic progression, then 

$$b^{2} - a^{2} = c^{2} - b^{2} = d^{2} - c^{2},$$

 and so 

$$2a + 1,2a + 3,\ldots,2b - 12b + 1,2b + 3,\ldots,2c - 12c + 1,2c + 3,\ldots,2d - 1$$

 would be 3 parts of an A.P. whose sums are all equal, which we mentioned above does not exist. Hence, we cannot have four perfect squares of positive integers in an arithmetic progression.

## Erdös-Selfridge, Catalan

 The fact that a product of (at least 2) consecutive positive integers can not be a perfect power was settled more than 50 years back by Erd¨os & Selfridge. In other words, the Diophantine equation 

$$(x + 1)(x + 2)\ldots(x + r) = y^{2}$$

 does not solutions in positive integers $$x,y,r > 1$$.
Erdös-Selfridge theorem is so simple to state (and easy to prove for 2 or 3 consecutive numbers) that one may be tempted to think it could perhaps have an elementary proof. However, for r &gt; 3, the proof needs deeper properties of prime numbers, such as a classical theorem due to Sylvester which asserts that any set of k consecutive numbers with the smallest one &gt; k contains a multiple of a prime &gt; k. The special case of this when the numbers are $$k + 1,\ldots,2k$$ is known as Bertrand’s postulate.
Yet another Diophantine equation arises from the natural question: _Which natural numbers have all their digits to be 1 with respect to two different bases?_
Equivalently, if the bases are x, y and he numbers have m and n digits respectively, then we wish to solve 

$$\frac{x^{m} - 1}{x - 1} = \frac{y^{n} - 1}{y - 1}$$

 in natural numbers $$x,y > 1;m,n > 2$$. For example 31 and 8191 have this property; 

$$(11111)_{2} = (111)_{5},\quad(111)_{90} = 2^{13} - 1.$$

 This was observed by Goormaghtigh nearly a century ago. However, it is still unknown whether there are only finitely many solutions in $$x,y,m,n$$. In fact, no other solutions are known. For any fixed bases $$x,y$$, it was proved only as recently as in 2002 that the number of solutions for $$m,n$$ is at the most 2.
Another question is whether one can have different finite arithmetic progressions with the same product. For instance 

$$2.6\ldots(4n - 2) = (n + 1)(n + 2)\ldots(2n)$$

 for all natural numbers $$n$$. So, the question as to whether there are other solutions to the Diophantine equation 

$$x\left( x + d_{1} \right)\ldots\left( x + (m - 1)d_{1} \right) = y\left( y + d_{2} \right)\ldots\left( y + (n - 1)d_{2} \right)$$

 where $$d_{1},d_{2}$$ are positive rational numbers and $$d_{1}\not{} = d_{2}$$ if $$m = n$$ is quite open. It is only in 1999 that using deeper ideas from the subject of algebraic geometry, it was proved that if $$m,n,d_{1},d_{2}$$ are fixed, then the equation has only finitely many solutions in integers apart from some exceptions which occur when $$m = 2,n = 4$$. A deep unsolved conjecture due to Erdös in 1975 asserts:
For each $$c \in \mathbb{Q}$$, the number of $$(x,y,m,n)$$ satisfying 

$$x(x + 1)\ldots(x + m - 1) = cy(y + 1)\ldots(y + n - 1)$$

 with $$y \geq x + m,\min(m,n) \geq 3$$, is finite.
There are so-called transcendental methods that often prove by general ideas that certain classes of Diophantine equations can have only finitely many integer solutions. But, they are not ‘effective’ in the sense that one does not know any number which bounds the size of possible solutions. For instance, for the so-called Catalan equation $$x^{m} - y^{n} = 1$$, Robert Tijdeman proved (ineffectively) finiteness of the number of solutions. Later, although it was made effective by Langevin, he obtained an upper bound for $$x,y,m,n$$ that was of the order of $$\exp(\exp(\exp(\exp(730))))$$ which is out of the range of any present-day computer. Of course, later in 2024, the Catalan equation was completely solved by Preda Mihailescu by totally different methods; he showed that the only perfect powers differing by 1 are 8 and 9. A more general conjecture due to S S Pillai is still open; it asserts that the gaps in the sequence of perfect powers tends to infinity.
{% include figure.html image='apollofig.jpeg' caption='In mathematics, Apollonian circle packing is a fractal generated by starting with a triple of circles, each tangent to the other two, and successively filling in more circles, each tangent to another three. Descartes discovered the remarkable fact that the four curvatures satisfy a Diophantine equation.' width=700 %}
 
## Apollonian circle packing

 Apollonius from 200 BC discovered something beautiful. If we have three circles touching each other, one may place another circle touching all three.
In the 17th century, Descartes discovered the remarkable fact that the four curvatures (which are taken to be the reciprocals of the radii) satisfy the Diophantine equation 

$$\left( \left( C_{1} + C_{2} + C_{3} + C_{4} \right)^{2} \right) = 2\left( C_{1}^{2} + C_{2}^{2} + C_{3}^{2} + C_{4}^{2} \right)$$

 Here, the circles are supposed to have no common interior point which means by convention that the outermost circle’s exterior is the interior and the interior is the exterior and the radius is negative. Thus, if we are given 3 of the circles and they have integer curvatures, the fourth must also have integral curvature because of the equation! In the figure here, the curvatures are −1, 2, 2, 3.

## ABC-conjecture


The ABC conjecture - formulated independently by Masser and Oesterl´e - supercedes many conjectures in Diophantine equations and implies many of them. It formalizes the intuitive observation that when two numbers A and B are divisible by large powers of small primes, then A + B tends to be divisible by small powers of large primes. More precisely:

> For any $$\epsilon > 0$$, there are only finitely many triples $$A,B,C$$ of relatively prime integers satisfying $$A + B = C$$, and $$\max(A,B,C) > \text{ Rad}(ABC)1 + \epsilon$$, where $$\text{Rad}(n)$$ is the product of all distinct prime divisors of $$n$$.

For instance, the ABC-conjecture implies Fermat’s last theorem for sufficiently large exponents; in fact, it implies finiteness of the number of solutions of the generalized Fermat equation $$Ax^{r} + By^{s} = Cz^{t}$$. There is the as-yet-unsolved Beal’s conjecture (also known as the Tijdeman- Zagier conjecture); until it is actually solved, one cannot predict what methods will work. The conjecture asserts that $$x^{a} + y^{b} = z^{c}$$ for a, b, c &gt; 2 implies that $$x,y,z$$ must have a common prime factor, and was formulated in 1993 by Andrew Beal, a banker and amateur mathematician.
 One of Beal’s goals is to inspire young people to think about the equation, think about winning the offered prize, and in the process become more interested in the field of mathematics. The prize money - now a million dollars - is being held by the AMS until it is awarded. The spendable income from investment of the prize money is used to fund the annual Erd¨os Memorial Lecture and other activities of the American Mathematical Society.
The conditions are necessary as shown by the examples 

$$7^{3} + 13^{2} = 2^{9},27^{4} + 1623^{=}9^{7.}$$


Finally, we would like to mention that we have not discussed some other topics that involve the name of Diophantus. One is an unsolved problem that goes under the name of Diophantine tuples (both integer and rational) problem. Diophantus himself found a rational 4-tuple $$1/16,33/16,17/4,105/16$$. The question as to how large a set of positive rationals $$a_{1},a_{1},\ldots,a_{n}$$ can be found so that all $$a_{i}a_{j} + 1$$ are squares for $$1 \leq i < j \leq n$$ is still open? For integer tuples, 4 is the limit as was proved in 2016. Another fertile area of current research involves the so-called Frobenius Coin exchange problem: “Given n positive integers with no common factor &gt; 1, what is the largest integer that cannot be represented as a nonnegative integral linear combination of the given integers?” Finally, we only alluded to briefly while describing a rational approximation to π
