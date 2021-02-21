import keyboard
import sys

x=0
print("Start typing \n")
def keyboard1 (x):
    keyboard.send("delete")
    keyboard.send("delete")
    keyboard.write(x)

def keyboardcapital (y):
    keyboard.send("delete")
    keyboard.send("delete")
    keyboard.send("delete")
    keyboard.write(y)

def keyboardsingle (z):
    keyboard.send("delete")
    keyboard.write(z)

def keyboardsinglecap (j):
    keyboard.send("delete")
    keyboard.send("delete")
    keyboard.write(j)

def keyboardspecialsend (t):
    keyboard.send("delete")
    keyboard.send(t)

def keyboardtripleCAP (r):
    keyboard.send("delete")
    keyboard.send("delete")
    keyboard.send("delete")
    keyboard.send("delete")
    keyboard.write(r)

def keyboardtriple (e):
    keyboard.send("delete")
    keyboard.send("delete")
    keyboard.send("delete")
    keyboard.write(e)

def setup():

        #lowercase
    keyboard.add_hotkey("f+j", lambda: keyboard1("a"))
    keyboard.add_hotkey("f+k", lambda: keyboard1("b"))
    keyboard.add_hotkey("f+l", lambda: keyboard1("c"))
    keyboard.add_hotkey("f+;", lambda: keyboard1("d"))
    keyboard.add_hotkey("d+j", lambda: keyboard1("e"))
    keyboard.add_hotkey("d+k", lambda: keyboard1("f"))
    keyboard.add_hotkey("d+l", lambda: keyboard1("g"))
    keyboard.add_hotkey("d+;", lambda: keyboard1("h"))
    keyboard.add_hotkey("s+j", lambda: keyboard1("i"))
    keyboard.add_hotkey("s+k", lambda: keyboard1("j"))
    keyboard.add_hotkey("s+l", lambda: keyboard1("k"))
    keyboard.add_hotkey("s+;", lambda: keyboard1("l"))
    keyboard.add_hotkey("a+j", lambda: keyboard1("m"))
    keyboard.add_hotkey("a+k", lambda: keyboard1("n"))
    keyboard.add_hotkey("a+l", lambda: keyboard1("o"))
    keyboard.add_hotkey("a+;", lambda: keyboard1("p"))
    keyboard.add_hotkey("j+k", lambda: keyboard1("q"))
    keyboard.add_hotkey("j+l", lambda: keyboard1("r"))
    keyboard.add_hotkey("j+;", lambda: keyboard1("s"))
    keyboard.add_hotkey("k+l", lambda: keyboard1("t"))
    keyboard.add_hotkey("k+;", lambda: keyboard1("u"))
    keyboard.add_hotkey("l+;", lambda: keyboard1("v"))
    keyboard.add_hotkey("d+s", lambda: keyboard1("w"))
    keyboard.add_hotkey("d+a", lambda: keyboard1("x"))
    keyboard.add_hotkey("s+a", lambda: keyboard1("y"))
    keyboard.add_hotkey("f+k+l", lambda: keyboardsingle("z"))


    #uppercase

    keyboard.add_hotkey("f+j+ space", lambda: keyboardcapital("A"))
    keyboard.add_hotkey("f+k+ space", lambda: keyboardcapital("B"))
    keyboard.add_hotkey("f+l+ space", lambda: keyboardcapital("C"))
    keyboard.add_hotkey("f+;+ space", lambda: keyboardcapital("D"))
    keyboard.add_hotkey("d+j+ space", lambda: keyboardcapital("E"))
    keyboard.add_hotkey("d+k+ space", lambda: keyboardcapital("F"))
    keyboard.add_hotkey("d+l+ space", lambda: keyboardcapital("G"))
    keyboard.add_hotkey("d+;+ space", lambda: keyboardcapital("H"))
    keyboard.add_hotkey("s+j+ space", lambda: keyboardcapital("I"))
    keyboard.add_hotkey("s+k+ space", lambda: keyboardcapital("J"))
    keyboard.add_hotkey("s+l+ space", lambda: keyboardcapital("K"))
    keyboard.add_hotkey("s+;+ space", lambda: keyboardcapital("L"))
    keyboard.add_hotkey("a+j+ space", lambda: keyboardcapital("M"))
    keyboard.add_hotkey("a+k+space", lambda: keyboardcapital("N"))
    keyboard.add_hotkey("a+l+space", lambda: keyboardcapital("O"))
    keyboard.add_hotkey("a+;+space", lambda: keyboardcapital("P"))
    keyboard.add_hotkey("j+k+space", lambda: keyboardcapital("Q"))
    keyboard.add_hotkey("j+l+space", lambda: keyboardcapital("R"))
    keyboard.add_hotkey("j+;+space", lambda: keyboardcapital("S"))
    keyboard.add_hotkey("k+l+ space", lambda: keyboardcapital("T"))
    keyboard.add_hotkey("k+;+ space", lambda: keyboardcapital("U"))
    keyboard.add_hotkey("l+;+ space", lambda: keyboardcapital("V"))
    keyboard.add_hotkey("d+s+ space", lambda: keyboardcapital("W"))
    keyboard.add_hotkey("d+a+ space", lambda: keyboardcapital("X"))
    keyboard.add_hotkey("s+a+ space", lambda: keyboardcapital("Y"))
    keyboard.add_hotkey("f+k+l+ space", lambda: keyboardsinglecap("Z"))

    #special characters

    keyboard.add_hotkey(";", lambda: keyboardspecialsend("delete"))
    keyboard.add_hotkey(";+space", lambda: keyboardspecialsend("tab"))        

    print("hi")
    keyboard.wait()
