# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 21:04:35 2021

@author: helen
"""

import Model
import View

def numbers():
    View.enter_first_number()
    num1 = float(input())
    View.enter_second_number()
    num2 = float(input())
    return num1, num2

if __name__ == "__main__":
    view = View.init()
    
    while(1):
        View.commands()
        command = input()
        
        if command == 'E' or command == 'e' :
            break
        elif command == 'P' or command == 'p':
            num1, num2 = numbers()
            result = Model.plus(num1, num2)
            View.print_expression(num1, num2, '+', result)
        elif command == 'M' or command == 'm':
            num1, num2 = numbers()
            result = Model.minus(num1, num2)
            View.print_expression(num1, num2, '-', result)
        elif command == 'U' or command == 'u':
            num1, num2 = numbers()
            result = Model.multiplication(num1, num2)
            View.print_expression(num1, num2, '*', result)
        elif command == 'D' or command == 'd':
            num1, num2 = numbers()
            result = Model.division(num1, num2)
            View.print_expression(num1, num2, '/', result)
        else:
            View.wrong_command()
