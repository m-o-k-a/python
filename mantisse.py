#Mantisse decompouse - Eddy Ikhlef
result = []
result_value = .0
index_value = -1
m = input("Ecrivez votre mantisse: ")
m = str(m)
print(m)

for n in list(str(m)):
    index_value += 1
    if int(n)%2 != 0:
        cache_result = "1/2**"+str(index_value)
        result_value += 1/(2**int(index_value))
        result.append(cache_result)
print(result, "=", result_value)
