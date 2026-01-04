import cards
from cards import Card,Deck,Hand

#4.Blackjack class

class Blackjack:
    #1. checking if a hand is a bust
    def bust(match,hand):
        return hand.get_value()>21
    
    #2. checking for a blackjack
    def blackJack(match,hand):
        return  hand.get_value()==21

    #3. checking for a winner
    def check_winner(match,player_hand,dealer_hand,first_turn=False):
        if match.bust(player_hand):
            print("you busted, dealer wins!")
            return True
        elif match.bust(dealer_hand):
            print("dealer busted, you win!")
            return True
        elif match.blackJack(player_hand) and match.blackJack(dealer_hand):
            if first_turn:
                print("it's a tie!")
                return True
        elif match.blackJack(player_hand):
            if first_turn:
                print("blackjack! you win!")
                return True
        elif match.blackJack(dealer_hand):
            print("blackjack! dealer wins!")
            return True
        return False
    
        #player only gets a blackjack on the first turn
        #in the process of hitting even if the player gets 21 it doesn't count as a blackjack
        #if the player gets a blackjack, dealer checks their cards too, no longer hidden
        
    #4. displaying cards, one dealer card is hidden until the end where it is displayed
    #dealer checks if the hand being dealt is the dealers or the players
    def display(match,hand,dealer,showAllDealerCards=False):

        print(f'''{"Dealer's" if dealer else "Your"} hand:''')

        for index,card in enumerate(hand.cards):
            if index== 1 and dealer and not showAllDealerCards and not match.blackJack(hand):
                print("hidden")
            else:    
                print(card)


    #5. final game
    def run_match(match):
        
        #1.shuffling the deck, handing 2 cards, displaying cards according to rules
        #checking if player got blackjack
        deck = Deck()
        deck.shuffle()
        
        player_hand = Hand()
        dealer_hand= Hand()

        for i in range(2):
            player_hand.add_card(deck.draw())
            dealer_hand.add_card(deck.draw())

        match.display(player_hand,False)
        print()
        match.display(dealer_hand,True)
        print()

        if match.check_winner(player_hand,dealer_hand,True):
            return

        #2. hit and stand methods
        choice=input("stand or hit(s/h): ")

        while player_hand.get_value()<21 and choice=='h':
            player_hand.add_card(deck.draw())
            match.display(player_hand,False)
            print()
            if match.check_winner(player_hand, dealer_hand):
                return
            choice=input("stand or hit(s/h): ")
            
        if match.check_winner(player_hand, dealer_hand):
            return

        #3. continuation ater standing 
        player_hand_value=player_hand.get_value()
        dealer_hand_value=dealer_hand.get_value()

         # dealer rules,displaying dealer cards, checking if dealer has blackjack
        while dealer_hand_value<17:
            dealer_hand.add_card(deck.draw())
            dealer_hand_value=dealer_hand.get_value()
        
        match.display(dealer_hand,True,True)
        print()

        if match.check_winner(player_hand, dealer_hand):
            return

        #4. final results

        print("Final results")
        print("Your hand:", player_hand_value)
        print("Dealer's hand:", dealer_hand_value)

        if player_hand_value>dealer_hand_value:
            print("you win!")
        elif player_hand_value==dealer_hand_value:
            print("it's a tie!")
        else:
            print("dealer wins!")

        print("\nThanks for playing")
               
game=Blackjack()
game.run_match()