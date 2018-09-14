# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 13:20:05 2018

@author: Eddy
"""
#Significand decompose - Eddy Ikhlef
result = [] #create list to show all the elements
result_value = .0 #create a float
index_value = 0 #start index to -1
m = input("Ecrivez votre mantisse: ") #get a binary string
for n in list(str(m))[1:]: #look over the binary string; [1:] to don't count the first digit (always one in the Significand)
    index_value += 1 #increment index value, to match with the position of the number n
    if int(n) == 1: #when digit is one, do:
        cache_result = "1/2**"+str(index_value) #result as an element of list
        result_value += 1/(2**int(index_value)) #increment value of the mantisse
        result.append(cache_result) #add the result as an element of list in result list
print("décomposition de la mantisse:", result, "=", result_value) #print results
