# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:42:12 2021

@author: helen
"""


import Model
import View_Gui
from tkinter import Tk


def clicked_plus(num1, num2):
    return Model.plus(float(num1), float(num2))

def clicked_minus(num1, num2):
    return Model.minus(float(num1), float(num2))

def clicked_multiplication(num1, num2):
    return Model.multiplication(float(num1), float(num2))
    
def clicked_division(num1, num2):
    return Model.division(float(num1), float(num2))

if __name__ == "__main__":
    
    window = Tk()
    window1 = View_Gui.View(window)
    window.mainloop()

    
        