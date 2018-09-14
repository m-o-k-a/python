#Mantisse decompouse - Eddy Ikhlef
result = [] #create list to show all the elements
result_value = .0 #create a float
index_value = -1 #start index to -1
m = input("Ecrivez votre mantisse: ") #get a binary string

for n in list(str(m)): #look over the binary string
    index_value += 1 #increment index value, to match with the position of the number n
    if int(n)%2 != 0: #if n is 1
        cache_result = "1/2**"+str(index_value) #result as an element of list
        result_value += 1/(2**int(index_value)) #increment value of the mantisse
        result.append(cache_result) #add the result as an element of list in result list
print(result, "=", result_value) #print results