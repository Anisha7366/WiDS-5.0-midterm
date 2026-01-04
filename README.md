# WiDS-5.0-midterm
# Monte Carlo Simulations

This covers the midterm submission for the WiDS project: "From calculating area to Gambling in BlackJack", spanning over the course of 2 weeks.

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




