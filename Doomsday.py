#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 22:22:23 2022

@author: ryanvossoughi
"""

import numpy as np

day_of_week=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]    #Result strings
day_doom=[3,28,14,4,9,6,11,8,5,10,7,12] #Doomsdays in non leap years from January-December
day_doom_leap = list(day_doom)
day_doom_leap[:2]=[4,29] #Doomsdays in leap years from January-December



#Function that guarantees a valid number is entered
def inputNumber(prompt): 
    while True:
        try:
            System = float(input(prompt))
            break
        except ValueError:
            pass
            print("Please select valid number")
    return System


#Function that displays a menu of options as a string for the user to select
#and returns the chosen selection as an integer
def displayMenu(options):

    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("Please choose a menu item: ")
    return choice

#Define menu items for the user to choose from
MenuItems=np.array(["Enter date","Quit"])
while True:
    choice=displayMenu(MenuItems)
    if choice == 1: 
        while True:
            item=input("Please enter date like so dd/mm/åååå: ")
            split_item=list(map(int,item.split("/"))) #Splits input date into 3 differennt outputs
            day=split_item[0]           #Input day is defined
            month=split_item[1]         #Input month is defined
            year=split_item[2]          #Input year is defined
            a=(9 - ((year // 100) % 4) * 2) % 7 # Formula for century code
            b=(year%100)//12                    # Last 2 digites of the year divided by 12
            c=(year%100)%12                     # Determines the remainder
            d=c//4                              # The remainder divided by 4                
            e=a+b+c+d                           # Sum of a,b,c and d gives the doomsday
            if (year % 400 == 0): #Checks for leap year
                dooms_day=day_doom_leap
            elif (year % 100 != 0):
                dooms_day=day_doom
            doom=(day-dooms_day[month-1]+e)%7 #Determines the doomsday from input month and day and turns into a week
            print("")
            print('The day of the week was a: '+day_of_week[doom]) #Prints DotW
            print("")
            break
    
    elif choice == 2:   
        print("Goodbye")                #To quit
        break


