# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 21:04:33 2021

@author: helen
"""

def init():
    print('This is a calculator for simple operations. First you should select the operation and then write down the numbers.\n')

def commands():
    print('\nP - plus, M - minus, U - multiplication, D - division, E - Exit')

def wrong_command():
    print('\nWrong command.\nPlease, enter the command again.')
    
def enter_first_number():
    print('\nPlease enter first number:')
    
def enter_second_number():
    print('\nPlease enter second number')
    
def print_expression(num1, num2, operation, result):
    print(num1, operation, num2, '=', result)