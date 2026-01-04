# WiDS-5.0-midterm
# Monte Carlo Simulations

This covers the midterm submission for the WiDS project: "From calculating area to Gambling in BlackJack", spanning over the course of 2 weeks.

# WEEK 1:

**1. The Gambler's ruin**

This assignment required simulation of 10,000 gamblers playing a simple coin flip game simultaneously and analyzing their wealth over time.

  1. Each gambler started with a payroll of $100
  
  2. 1000 rounds of fair coin flip were played, where:
  
      1. Heads(+1): win $1
      
      2. Tails(-1): lose $1
      
  3. Game over: when payroll touches 0

Numpy was used to generate random outcomes over 1000 steps for 10000 gamblers and finding the payroll of each gambler at each step.

A spaghetti plot(using matplotlib) was used to display the trajectories(payroll vs time) of all gamblers. Mean wealth at each stage, max winner and max loser were highlighted.

A histogram(using matplotlib) was used to showcase the final wealth distribution(no. of gamblers vs final wealth) with mean wealth highlighted.
