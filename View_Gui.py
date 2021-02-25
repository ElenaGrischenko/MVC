# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 11:39:45 2021

@author: helen
"""



from tkinter import *
import Controller_Gui

class View:
    
    def __init__(self, window):
        window.title("Simple calculator")
        window.geometry('800x400')
        
        self.command_plus = Label(window, text='Plus:')
        self.command_plus.grid(column=1, row=0)
        self.pnum1 = Entry(window, width=10)
        self.pnum1.grid(column=2, row=0)
        self.plus = Label(window, text='+')
        self.plus.grid(column=3, row=0)
        self.pnum2 = Entry(window, width=10)
        self.pnum2.grid(column=4, row=0)
        self.plus_equal = Button(window, text='=', command=self.clicked_plus)
        self.plus_equal.grid(column=5, row=0)
        self.result_plus = Label(window, text='')
        self.result_plus.grid(column=6, row=0)
        
        self.command_minus = Label(window, text='Minus:')
        self.command_minus.grid(column=1, row=1)
        self.mnum1 = Entry(window, width=10)
        self.mnum1.grid(column=2, row=1)
        self.minus = Label(window, text='-')
        self.minus.grid(column=3, row=1)
        self.mnum2 = Entry(window, width=10)
        self.mnum2.grid(column=4, row=1)
        self.minus_equal = Button(window, text='=', command=self.clicked_minus)
        self.minus_equal.grid(column=5, row=1)
        self.result_minus = Label(window, text='')
        self.result_minus.grid(column=6, row=1)
    
        self.command_mult = Label(window, text='Multiplication:')
        self.command_mult.grid(column=1, row=2)
        self.munum1 = Entry(window, width=10)
        self.munum1.grid(column=2, row=2)
        self.mul = Label(window, text='*')
        self.mul.grid(column=3, row=2)
        self.munum2 = Entry(window, width=10)
        self.munum2.grid(column=4, row=2)
        self.mul_equal = Button(window, text='=', command=self.clicked_multiplication)
        self.mul_equal.grid(column=5, row=2)
        self.result_mul = Label(window, text='')
        self.result_mul.grid(column=6, row=2)
        
        self.command_division = Label(window, text='Division:')
        self.command_division.grid(column=1, row=3)
        self.dnum1 = Entry(window, width=10)
        self.dnum1.grid(column=2, row=3)
        self.division = Label(window, text='/')
        self.division.grid(column=3, row=3)
        self.dnum2 = Entry(window, width=10)
        self.dnum2.grid(column=4, row=3)
        self.div_equal = Button(window, text='=', command=self.clicked_division)
        self.div_equal.grid(column=5, row=3)
        self.result_div = Label(window, text='')
        self.result_div.grid(column=6, row=3)
        
    
    def clicked_plus(self):
        self.result_plus['text'] = Controller_Gui.clicked_plus(self.pnum1.get(), self.pnum2.get())
        
    def clicked_minus(self):
        self.result_minus['text'] = Controller_Gui.clicked_minus(self.mnum1.get(), self.mnum2.get())

    def clicked_multiplication(self):
        self.result_mul['text'] = Controller_Gui.clicked_multiplication(self.munum1.get(), self.munum2.get())

    def clicked_division(self):
        self.result_div['text'] = Controller_Gui.clicked_division(self.dnum1.get(), self.dnum2.get())
    


