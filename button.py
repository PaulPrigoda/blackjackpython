# button.py
# for lab 8 on writing classes
from graphics import *
from random import randrange

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 
        w,h = width/2.0, height/2.0 #w and h are the width and the height 
        x,y = center.getX(), center.getY() #x and y are the coordinates
        self.xmax, self.xmin = x+w, x-w  #creates top left point of rect
        self.ymax, self.ymin = y+h, y-h  #creates top right point of rect
        p1 = Point(self.xmin, self.ymin)#stores first point
        p2 = Point(self.xmax, self.ymax) #stores second point
        self.rect = Rectangle(p1,p2) #creates rect
        self.rect.setFill('lightgray') #color of rect
        self.rect.draw(win) #draws rect
        self.label = Text(center, label) #puts text in button center
        self.label.draw(win) #draws text
        self.activate() #this line was not there in class today

    def getLabel(self):
        """Returns the label string of this button."""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black') #color the text "black"
        self.rect.setWidth(2)       #set the outline to look bolder
        self.active = True          #set the boolean variable that tracks "active"-ness to True

    def deactivate(self):
        """Sets this button to 'inactive'."""
        ##color the text "darkgray"
        self.label.setFill("darkgray")
        ##set the outline to look finer/thinner
        self.rect.setWidth(1)
        ##set the boolean variable that tracks "active"-ness to False
        self.active = False

    def isClicked(self,p):
        """Returns true if button active and Point p is inside"""
        x,y = p.getX(),p.getY()
        if self.xmin < x and x < self.xmax and self.ymin < y and y < self.ymax and self.active == True:
            return True
        return False
    
if __name__ == "__main__": 
    main()
