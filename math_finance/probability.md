---
layout: post
title: Probability Tips
---

Just want to summarize some tips on doing probability and brain teaser questions in interviews: (1-3 are useful in all cases, remaining are useful in particular probability question)

- (1) Start a small number. For instance, if a question asks that 5 (or 100) pirates divide 100 gold coins by majority voting, that is, 50% of the group shall agree on the proposal, otherwise the most senior one will be fed into shark, how would they divide the coins at last (assuming all pirates are rational)?

  WLOG, let's name the least senior one as 1, the most senior one 5. Say we only have 2 pirates, then pirate 2 can directly get all, and 1 will get nothing. If there're 3 pirates, since pirate 3 knows 1 will get nothing if he does not vote for 3's proposal (assuming 1 will let 3 die when 1 can get nothing), 3 will give 1 coin, 3 get the 99. Then if there're 4 pirates, 4 knows 2 knows 2 will get nothing if 2 does not support 4, so it's 4 get 99 and 2 get 1. When there're 5 pirates, 5 knows 3 and 1 are clear they will get nothing if they do not support 5, so 5 will give 1 to 3 and 1, 5 get the remaining 98. 

- (2) Symmetry. This is useful in all cases. Two symmetric events have the same probability. Say, flipping N times a fair coin, A and B will have the same probability of getting more heads. Notice that there will still be the probabiliy of being tie, let it be $y$. Then $2x+y=1$.  This is extremely useful to simplify a lot of problems. If we can segment the sample space, $2x+y$ doesn't have to be equal to 1, it can $2/3$ or other things.

- (3) Invert. Almost always invert. The interested event $A$ asked by the question is often easier to computer by $1-Pr(A^c)$

- (4) Mutually exclusive (more generally, disjoint). This is useful in summing up probabilities. $P(A\cup B)=P(A)+P(B)-P(AB)=P(A)+P(B)$. Often times, when two events $A$ and $B$ are disjoint, their joint probability is maximized. Side note: $P(A\cup B)$ is minimized when one event include another, that is $P(A\cup B)=\min\{P(A),P(B)\}$, this case $P(AB)=P(A)$ ($P(B)$) and when summing up, one of P(A), P(B) got canceled out

- (*) Independence. This is a quite common point that everyone notices. 

- (5) There're three ways to get an interested probability/expecation. First, the most direct way is to count, by the sample space. Second, probably easier in complicated sample space, use condition probability and multiply those together. The third, often used in expectation, is to start over $E[X]$. Say, two players flip coins until A gets $HT$ (meaning B flips H and then A flips T following), then A's winning probability is starting over again given A throws H, B throws H. 

Tricks for expansion an integer: 
...
