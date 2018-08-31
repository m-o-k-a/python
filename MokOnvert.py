# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 19:15:26 2018

@author: Eddy
"""
#MOKA ULTIMATE BINARY : Convert base 10 To Base 2 V 1.0
#Created By Eddy Ikhlef - Moka - mokastudy.tk
#special thanks to http://cs.furman.edu/digitaldomain/more/ch6/dec_frac_to_bin.html
import os

toEnd = "y" 
print("/!\ numbers will be converted to the more precise value")
while toEnd == "y": #main loop, to do many conversion
  number_str = input("Please enter a number >> ")
  #get int part and fractionnal part
  number_int = 0 #set to int
  number_float = float(number_str) #set to float
  if number_float >= 0: #check if the int is negative
      neg = False 
  else:
      neg = True
      number_float = abs(number_float)
  
  while number_float >= 1: #allow to get integer part of number_float and send it to number_int
    number_int += 1
    if number_float - number_int < 1:
      break
  number_float -= number_int #delete integer part
#---STEP I : INT CONVERTION--- consecutive euclidian equation method#
  result = ''
  while number_int > 0:
    if number_int %2 == 0:
      result = '0' + result
      number_int = int(number_int//2)
    else:
      result = '1' + result
      number_int = int(number_int//2) 
  number_int = result
#---STEP II : FLOAT CONVERTION--- check method in the website at the top of the programm#
  result_float = ''
  count = 0
  while number_float > 0:
    number_float = number_float*2
    number_cache = number_float
    if number_float >= 0 and number_float < 1:
      result_float = result_float + '0'
      count += 1
    else:
      result_float = result_float + '1'
      number_float -= 1
      count += 1
    if number_cache == int(number_cache):
       number_float = result_float
       break
 
  if neg == False: #0b
    print(str(number_str), "(base 10) correspond to 0b",str(number_int),".",str(number_float))
  else: #add the negative number if the int was negative, -0b
    print(str(number_str), "(base 10) correspond to -0b",str(number_int),".",str(number_float))

  toEnd = input("Convert another number? (Y/N)").lower() #ask to redo
  if toEnd == "n":
    print("See you next time on MokOnvert")
    os.system ("pause")
  elif toEnd != "y": #wrong value
    print("ERROR: NOT Y OR N, ABORT PROGRAMM")
    os.system ("pause")
#------------------------------END OF PROGRAMM-----------------------------#
