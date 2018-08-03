#PT Prigoda and David Ableson
#Programming Assignment 5
#Due Date 11/11/15
#This program is a code to run the game BlackJack, allowing the player to hit,
#stand, and also play again if the player wins or loses, and finally allows
#the player to quit at any time. This has

from blackJack import *
from graphics import *
from button import *

#BlackJack class
class BlackJack:
    def __init__(self):
        self.deck = Deck()
        #shuffle the cards
        self.deck.shuffle()
        #empy list for dealers hand
        self.dealerHand = []
        #empty list of players hand
        self.playerHand = []
        self.images = []

    #initializing class
    def initialDeal(self):
        #gives player a starting card
        card = self.deck.dealCard()
        self.playerHand.append(card)
        #gives dealer a starting card
        card = self.deck.dealCard()
        self.dealerHand.append(card)
        #gives player a starting card
        card = self.deck.dealCard()
        self.playerHand.append(card)
        #gives dealer a starting card
        card = self.deck.dealCard()
        self.dealerHand.append(card)

    #gets the rank and suits of the cards while displaying on GUI
    def displayHands(self,win,dealerX,dealerY,playerX,playerY):
        #for loop to know the suit and rank of dealer card
        for card in self.dealerHand:
            #gets rank and suit of cards
            rank = card.getRank()
            suit = card.getSuit()
            #displays card on GUI
            im = Image(Point(dealerX,dealerY),"playingcards/" + suit + str(rank) + ".gif")
            im.draw(win)
            self.images.append(im)
            dealerX += 7
        #dealer starts with one card face down
        self.im = Image(Point(dealerX - 7,dealerY),"playingcards/b2fv.gif")
        self.im.draw(win)
        #for loops for rank and suit in players hand
        for card in self.playerHand:
            #gets rank and suit of cards
            rank = card.getRank()
            suit = card.getSuit()
            #displays cards in an order on GUI
            im = Image(Point(playerX,playerY),"playingcards/" + suit + str(rank) + ".gif")
            im.draw(win)
            self.images.append(im)
            playerX += 7
        self.dealerX = dealerX
        self.dealerY = dealerY
        self.playerX = playerX
        self.playerY = playerY

    #gives player another card if under 21
    def hit(self,win):
        #gets card
        card = self.deck.dealCard()
        #gets suit and rank
        rank = card.getRank()
        suit = card.getSuit()
        #places card in hand
        self.playerHand.append(card)
        #puts image of card in GUI
        im = Image(Point(self.playerX,self.playerY),"playingcards/" + suit + str(rank) + ".gif")
        im.draw(win)
        #adds to the total of the hand
        self.images.append(im)
        self.playerX += 7

    #evaluates if the ace should be 1 or 11
    def evaluateHand(self,hand):
        haveAce = False
        #accumulator variable
        total = 0
        #for loop to loop through cards in hand
        for card in hand:
            #accumulator var
            total = total + card.blackjackValue()
            #if the card value is 1, there is an ace in the hand
            if card.getRank() == 1:
                haveAce = True
            if haveAce and 17 <= total + 10 <=21:
                total += 10
        #reuturns total amount in hand        
        return total

    #tells the dealer when to stop hitting and stand
    def dealerPlays(self,win):
        #accumulator varibale
        total = self.evaluateHand(self.dealerHand)
        self.im.undraw()
        #while loop to keep hitting if dealer hand under 17
        while self.evaluateHand(self.dealerHand) < 17:
            #deals a card
            card = self.deck.dealCard()
            #gets the cards rank and suit
            rank = card.getRank()
            suit = card.getSuit()
            #put the card in the dealers hand
            self.dealerHand.append(card)
            #displays the card in the GUI
            im = Image(Point(self.dealerX,self.dealerY),"playingcards/" + suit + str(rank) + ".gif")
            im.draw(win)
            self.images.append(im)
            self.dealerX += 7
            #accumulator var
            total = total + card.blackjackValue()
        return total

    #undraw when play clicks play again to start a new game
    def unDraw(self):
        for card in self.images:
            card.undraw()

    def getHands(self):
        return self.dealerHand,self.playerHand
            

def main():
    #graphical window
    win = GraphWin("PT and David's BlackJack",600,600)
    win.setCoords(-1,-1,100,100)
    #makes background green
    win.setBackground("green4")

    #welcome text
    welcome = Text(Point(50,95),"Welcome to PT and David's BlackJack!")
    welcome.setSize(20)
    welcome.draw(win)

    #player amount text
    player = Text(Point(20,25),"Player:")
    player.setSize(25)
    player.draw(win)

    #dealer amount text
    dealer = Text(Point(80,75),"Dealer: ")
    dealer.setSize(25)
    dealer.draw(win)

    #displays hit button, activated
    hit = Button(win,Point(13,50),20,10,"Hit")
    hit.activate()

    #displays stand button, activated
    stand = Button(win,Point(38,50),20,10,"Stand")
    stand.activate()

    #displays play again button, deactivated
    playAgain = Button(win,Point(62,50),20,10,"Play Again")
    playAgain.deactivate()

    #displays quit button, activated so user can quit any time
    quitGame = Button(win,Point(87,50),20,10,"Quit")
    quitGame.activate()

    #starts game of blackjack
    bj = BlackJack()

    #deals initial cards to player and dealer
    bj.initialDeal()

    #places where the images of cards are displayed in GUI
    bj.displayHands(win,25,75,45,25)

    #total of player and dealer hands
    dhand,phand = bj.getHands()
    ptotal = bj.evaluateHand(phand)
    dtotal = bj.evaluateHand(dhand)
    player.setText("Player: "+str(ptotal))

    #wating for a user click
    pt = win.getMouse()

    #you win/lose text
    output = Text(Point(50,60),"")
    output.setSize(30)
    output.draw(win)

    #while loop while the quit button isnt clicked
    while not quitGame.isClicked(pt):
        #if hit is clicked, gives player another card
        if hit.isClicked(pt) == True:
            bj.hit(win)
            dhand,phand = bj.getHands()
            ptotal = bj.evaluateHand(phand)
            player.setText("Player: "+str(ptotal))
            #if player total is over 21, they busted and lose
            if ptotal > 21:
                output.setText("You Busted, You Lose!!!")
                #deactivates hit and stand buttons, activates play again button
                hit.deactivate()
                stand.deactivate()
                playAgain.activate()
        #otherwise, if stand is clicked, dealer goes
        elif stand.isClicked(pt) == True:
            dtotal = bj.dealerPlays(win)
            dealer.setText("Dealer: "+str(dtotal))
            hit.deactivate()
            stand.deactivate()
            #if dealer total is over 21, player wins
            if dtotal > 21:
                output.setText("Dealer Busts, You Win!!!")
            #if dealer total is greater than player total, dealer wins
            elif dtotal > ptotal:
                output.setText("You Lose!!!")
            #if it is a tie, player wins (rule of blackjack)
            elif dtotal == ptotal:
                output.setText("It's a Tie, You Win!!!")
            #anything else, player will have higher amount and they will win
            else:
                output.setText("Higher Amount, You Win!!!")
            playAgain.activate()
        #otherwise, if play again is clicked, reset game
        elif playAgain.isClicked(pt):
            #undraws everything
            bj.unDraw()
            #initializes new game
            bj = BlackJack()
            #deals new cards
            bj.initialDeal()
            #cards in same spot
            bj.displayHands(win,25,75,45,25)
            #gets self.dealerHand and self.playerHand
            dhand,phand = bj.getHands()
            #evaluates boths hands
            ptotal = bj.evaluateHand(phand)
            dtotal = bj.evaluateHand(dhand)
            #resets the total amount for player
            player.setText("Player: "+str(ptotal))
            #activates hit and stand, deactivates play again
            hit.activate()
            stand.activate()
            playAgain.deactivate()
            #resets amount for dealer
            output.setText("")
            dealer.setText("Dealer: ")
        #waits for click from user
        pt = win.getMouse()
    #if quit is clicked, quits game
    win.close()
    quitGame.activate()

if __name__ == "__main__":
    main()
        
        
