#Declararea liste
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(my_list)

#Afiseaza lista ordonata ascendent
my_list.sort()
print(my_list)

#Afiseaza lista ordonata descendent
my_list.reverse()
print(my_list)

# Afiseaza numerele pare
numere_pare = my_list[0:9:2]
print(numere_pare)

# Afiseaza numerele impare
numere_impare = my_list[9:0:-2]
print(numere_impare)

# Afiseaza multipli ai lui 3
multipli_trei=my_list[1:9:3]
print(multipli_trei)
