import random
# visar hur man använder funktioner för att samla och använda kod 

# skapa array med tuple
frukter = ("Apelsin", "Banan", "Melon", "Kiwi", "Citron")
looping = True

# Definerar funktion
def print_fruit(userinput):
    fnr = int(userinput)
    print("\n" + frukter[fnr-1] + " Kommer Här!\n")


# Huvudprogram
print("\n-:FruktMaskin:_\n")


while looping:

    i = 1 
    for frukt in frukter:
        print(str(i) + ": " + frukt)
        i += 1 


    fruktnr = input("\nMata in nummer på frukt du vill ha: ")
    print_fruit(fruktnr)
    go = input("\nVill du ha en frukt till? ")

    if (go == "n"):
        break


print("---------------------------------------------------------------")

print("\nFöresten, du får en frukt för du är snäll\n")
slumpfrukt = random.randint(1, 5)
print_fruit(slumpfrukt)