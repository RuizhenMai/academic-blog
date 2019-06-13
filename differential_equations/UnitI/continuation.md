---
title: Continuation
layout: post
date: 2019-6-5
---

(Video 8) (Book p. 52)

## Mixing problem

Image a tank containing a solution— a mixture of solute and solvent— such as salt dissolved in water. And we want to know

$$
x(t)=\mathrm{amount\ of\ salt\ in\ tank\ at\ time\ } t
$$

Suppose we have an opening on top, and a solution with concentration of $$c_i$$ grams of solute per liter of solution flows into the tank at a constant rate of $$r_i$$ litters per seconds; there's another different-sized opening in the bottom, and that solution in the tank flows out at a different constant rate of $$r_0$$ liters per second. Let $$c_0$$ be the concentration of solute in the tank, then for a very small time interval  $$\Delta t$$, the change of amount of salt in the tank is 

$$
\Delta x=\mathrm{grams\ input}-\mathrm{grams\ output}\approx (r_ic_i-r_0c_0)\Delta t
$$

If we know the volume of the liquid (solution) in the tank at time $$t$$, then we can write

$$
c_0(t)=\frac{x(t)}{V(t)}
$$

Combine all these

$$
\frac{dx}{dt}=r_ic_i-\frac{x(t)}{V(t)}r_0
$$

Writing in standard form

$$
x'+\frac{r_0}{V(t)}x=r_ic_i
$$
