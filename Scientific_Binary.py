# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 21:40:55 2018
@author: Eddy
"""
#Scientific Binary Notation
#Starting Fuctions
my_continue = True
def mantisse(): #Significand Function (from my previous programm Mantisse.py
    result = []  # create list to show all the elements
    result_value = .0  # create a float
    index_value = 0  # start index to 0 (incremen# tation at the beginning of the for loop to match the identification of the list)
    m = my_binary[8:]  # get a binary string
    print(m)
    for n in list(str(m))[1:]:  # look over the binary string; [1:] to don't count the first digit (always one in the significand)
        index_value += 1  # increment index value, to match with the position of the number n
        if int(n) == 1:  # when digit is one, do:
            result_value += 1 / (2 ** int(index_value))  # increment value of the significand
    return result_value  # print results

def signe(): #Signe Function
    if my_binary[0] == "0":  #Because our input is a string, we need to ask if the index 0 is equal to a string and not a number.
        return "+"
    else:
        return "-"

def entier(): #Integer Function Converter, lazy version
    return int(my_binary[1:9], 2)-127

#Starting Main Loop
while my_continue:
    print("tout nombre Réel x peut s'écrire en base 10 de la forme sm*2^k sur 32 Bits")
    print("s = le signe du nombre")
    print("m = la mantisse de 23 bits")
    print("k = la puissance du type e + 127, e codé sur 8 bits et e ϵ Z")
    my_binary = input("Ecrivez votre nombre binaire:\n")
    # verifie que c'est du 32 bit
    while len(my_binary) != 32:
        my_binary = my_binary + "0"
    print("Conversion en 32 Bits ->", my_binary, my_binary[10:])
    #s = signe()
    #e = entier()
    #m = mantisse()
    #affichage du nombre en binaire
    print("votre nombre est : " + str(signe()) + str(mantisse()) + "*" + "2" + "^"+ str(entier()) + "\nConvertir une nouvelle fois? (Y/N)") #print("votre nombre est : " + str(s) + str(m) + "*" + "2" + "^"+ str(e))
    while True: #to get a correct output
        test = input("(Y/N) ? >> ")
        if test == "N" or test == "n":
            my_continue = False
            break
        elif test == "Y" or test == "y":
            break
        else:
            print("Error: Must Write Y or N as OUTPUT")
