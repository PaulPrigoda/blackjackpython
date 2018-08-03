from random import *

#playing card class, defines rank and suit of card
class PlayingCard:
    def __init__(self,rank,suit):
        #sets variables rank and suit
        self.rank = rank
        self.suit = suit

    #returns the rank of card
    def getRank(self):
        return self.rank

    #returns the suit of card
    def getSuit(self):
        return self.suit

    #for face cards keeps the values the same
    def blackjackValue(self):
        if self.rank >= 11:
            return 10
        #returns the value
        return self.rank
            
    def __str__(self):
        #contains the value of each card
        rankList = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
        #contains the suit of each card
        suitDict = {"d":" Of Diamonds","c":" Of Clubs","h":" Of Hearts","s":" Of Spades"}
        #list of ranks as a string
        rankString = rankList[self.rank - 1]
        #list of suits as a string
        suitString = suitDict[self.suit]
        #reutns the rank and suit
        return rankString+suitString

#Class deck, assigns number values to the cards
class Deck:
    #initialize
    def __init__(self):
        #list of suits
        suits = ["d","c","h","s"]
        #empty deck as an empty list
        self.deck = []
        #double for loop to assign suit and rank to cards
        for suit in suits:
            for rank in range(1,14):
                #puts new value card into the deck
                card = PlayingCard(rank,suit)
                self.deck.append(card)

    #shuffles the deck of cards
    def shuffle(self):
        shuffle(self.deck)

    #deals a card
    def dealCard(self):
        return self.deck.pop()

    #returns to list of cards remaining
    def cardsLeft(self):
        remain = len(self.deck)
        return remain

#testing things dont mind this
def main():
    deck = Deck()
    deck.shuffle()
    for card in deck.deck:
        print(card)
    print(deck.dealCard())
    print(deck.dealCard())
    print(deck.dealCard())
    print(deck.cardsLeft())
if __name__ == "__main__":
    
    main()
