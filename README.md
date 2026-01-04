# WiDS-5.0-midterm
# Monte Carlo Simulations

This covers the midterm submission for the WiDS project, Monte Carlo Simulations: "From calculating area to Gambling in BlackJack", spanning over the course of 2 weeks.

# WEEK 1:

**1. The Gambler's ruin**

**This assignment required simulation of 10,000 gamblers playing a simple coin flip game simultaneously and analyzing their wealth over time.**

  1. Each gambler started with a payroll of $100
  
  2. 1000 rounds of fair coin flip were played, where:
  
      1. Heads(+1): win $1
      
      2. Tails(-1): lose $1
      
  3. Game over: when payroll touches 0

Numpy was used to generate random outcomes over 1000 steps for 10000 gamblers and finding the payroll of each gambler at each step.

A spaghetti plot(using matplotlib) was used to display the trajectories(payroll vs time) of all gamblers. Mean wealth at each stage, max winner and max loser were highlighted.

A histogram(using matplotlib) was used to showcase the final wealth distribution(no. of gamblers vs final wealth) with mean wealth highlighted.

**2. BlackJack**

**This assignment required the implementation of Blackjack as a terminal game in python**

**1. Card.py**
  
  1. The Card class: stores the suit, rank and represents the card when called (eg. "4, Hearts")
      
  2. The Deck class: contains a list of card objects(all 52 cards), function to shuffle the deck(using random module), function to draw a card(using list functions) and   function to reset the deck.
  
  3. The Hand class: contains the cards held by the player(or dealer), function to add cards to the hand, function to flush, calculate the value of a hand(**with consideration to ace which can be 1 or 11**) and get the value of the hand.

**2. Blackjack.py: contains the Blackjack class**

  1. Runs a single round
    
  2. Maintains the players hand and dealers hand(**with blackjack rules applied- eg. the dealer's second card is hidden**)

  3. Methods to Hit or Stand(to accept a card or not)

  4. Checks for Bust, Blackjack and ties.

**All 4 classes were made accordingly**

# WEEK 2:

**This week involved using monte carlo integration to estimate areas, volumes and constants such as e and pi.**

**1. Estimating e:**

  1. method 1: finding the area under the graph of "y vs 1/x" to find the log value and by extension "e".

     generating N points with x coordinate between 1 and a given integer n(n>1), y coordinates from 0 to 1(**using np.random**). Finding number points that lie below y=1/x and estimating e accordingly. Comparing with the analytical value of e (using **np.e**)

  2. method 2: generating N random sequences(u(k)) of numbers between 0 and 1 and finding a specific index n where u(n+1)>=u(n). Taking average of these over N sequences gives e(using **np.mean**). Comparing with the analytical value of e(**np.e**)

The code was runned using the 2 methods seperately(**with test cases from 2-100 and desired input**), perecentage error, value of e were reported accordingly.

**2. Estimating pi**

  1. method: finding the area of a unit circle using monte carlo integration(using np.random). That involves generating random points with -1<=x<=1, -1<=y<=1 and finding the number of points that lie inside the circle.

  2. Plot1: Estimated value of pi vs the number of testcases. Plot2: Percentage error(with np.pi) vs the number of testcases.

The function was runned for N from 10 to 10**7 and the resulting value of pi was plotted accordingly.

**3. Modular shape estimator**

   1. method: the code was refactored to be modular. A function was made which accepts the function/ predicate as argument. (generating points within the bounds and calculating area using monte carlo integration)
    
   2. function 1: Circle(standard pi estimation)--> x** 2+y** 2<1 true area=pi

   3. function 2: Parabola(area under y=x**2 for 0<=x<=1), true area=1/3

   4. function 3: Gaussian(area under y=e**(x**2) for 0<=x<=2), true area estimated using scipy.special.erf

the functions were runned for N from 2 to 10,000 and 2 plots for each function (error percentage vs N) and (calculated value vs N) were plotted.

**4. Other Applications**

  1. volume of a n dimension sphere and area of intersection between 2 circles:
     
    1. function 1: finds volume of an n dimension sphere using monte carlo integration by sampling 1,000,000 points.

    2. function 2: finds area of intersection between 2 circles using monte carlo integration by taking coordinates of centers of circles and radii as input.(samples 100,000 points)

  **the functions were run with some generic inputs**

  2. comparing reimann sum and monte carlo integration in different dimensions.

    1. 1D:
    
      1. created a grid of 100,000 points to find the reimann sum(of rectangle areas) to find integration of sinxdx from 0 to pi.
      
      2. applied monte carlo integration and compared the two results.
      
      3. reimann sum proved to be much more accurate

    2. 10D:
    
      1. created a grid of 1,000,000 points, 4 points per axis and found the reimann sum to find the volume of a 10D sphere.
      
      2. applied monte carlo integration accordingly by sampling 1,000,000 points randomly and compared the two results.

      3. monte carlo proved to be much more accurate

    3. 6D

      1. applied taylor series in a function(upto 8 terms) to find the value of the gaussian integral (from -1 to 1) and raised it to the power 6.

      2. reimann sum with 10 points per axis i.e 1,000,000 points to find the integral.

      3. applied montecarlo integration by sampling 1,000,000 random points and compared all the results.

      4. taylor series proved to be the most accurate followed by monte carlo. reimann sum was inaccurate.

# This concludes the midterm submission for the WiDS project, Monte Carlo Simulations: "From calculating area to Gambling in BlackJack", spanning over the course of 2 weeks. 
