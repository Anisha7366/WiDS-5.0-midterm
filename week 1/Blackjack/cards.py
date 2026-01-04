import random

#1.forming card class
class Card:

    #1.storing suit and rank
    def __init__(card,suit,rank):
        card.suit=suit
        card.rank=rank

    #2.the print on terminal
    def __str__(card):
        return f"{card.rank['rank']}, {card.suit}"

#2.forming deck class
class Deck:

    #1.defining cards in the deck
    def __init__(deck):
        deck.cards=[]
        suits=["spades", "clubs" , "hearts" , "diamonds" ] 
        ranks=[{"rank":"A", "value" : 11},{"rank":"1", "value" : 1},{"rank":"2", "value" : 2},{"rank":"3", "value" : 3},
               {"rank":"4", "value" : 4},{"rank":"5", "value" : 5},{"rank":"6", "value" : 6},{"rank":"7", "value" : 7},
               {"rank":"8", "value" : 8},{"rank":"9", "value" : 9},{"rank":"10", "value" : 10},{"rank":"J", "value" : 10},
               {"rank":"Q", "value" : 10},{"rank":"K", "value" : 10},
            ]

        for suit in suits:
            for rank in ranks:
                deck.cards.append(Card(suit, rank))

    #2.shuffling deck
    def shuffle(deck):
        if(len(deck.cards)>1):
            random.shuffle(deck.cards)

    #3.drawing a card from the deck 
    def draw(deck):
        Cards=[]
        Cards.append(deck.cards.pop())
        return Cards
    
    #4.resetting the deck to it's original state
    def reset(deck):
        deck1=Deck()
        deck.cards=deck1.cards

#3.forming hand class
class Hand:

    #1.initializing
    def __init__(hand):
        hand.cards=[]
        hand.value=0
    
    #2.add card method
    def add_card(hand,card_list):
        hand.cards.extend(card_list)

    #3.flush
    def flush(hand):
        hand.cards=[]

    #4.calculating the hand value with the logic of aces in mind
    def calculate_value(hand):
        hand.value=0
        for card in hand.cards:
            card_value=card.rank["value"]
            hand.value+=card_value
        for card in hand.cards:
            if card.rank["rank"]=="A" and hand.value>21:
                hand.value-=10

    #5.returning hand value  
    def get_value(hand):
        hand.calculate_value()
        return hand.value
    
    
    
