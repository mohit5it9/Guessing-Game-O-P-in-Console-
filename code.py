#Runs in www.codeskulptor.org only


import simplegui
import math
import random

tri=0
lucky=0
rang=0

def range100():
    global rang,tri,lucky
    print "New game.Range is 0 to 100"
    rang=100
    tri=int(math.ceil(math.log(rang,2)))
    lucky= random.randrange(0, 100)
    print "Number of remaining tries is",tri

def range1000():
    global rang,tri,lucky
    print "New game.Range is 0 to 1000"
    rang=1000
    tri=math.ceil(math.log(rang,2))
    lucky=random.randrange(0, 1000)
    print "Number of remaining tries is",tri

def input_guess(guess):
    global rang,tri,lucky
    guss=int(guess)
    print "Guess is",guss
    tri-=1
    print "Number of remaining guesses are",tri
    if guss>lucky and tri>0:
        print "Lower"
    if guss<lucky and tri>0:
        print "Higer"
    if guss==lucky and tri>0:
        print "Correct"
    if tri<0 :
        print "loser"
        print "Try a new game"
        
frame=simplegui.create_frame("Maru",200,300)
frame.add_button("Range is 0 to 100",range100,100)
frame.add_button("Range is 0 to 1000",range1000,100)
frame.add_input("Enter guess",input_guess,100)
frame.start()
    
