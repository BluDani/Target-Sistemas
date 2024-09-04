def inverterString(str):

    if len(str) == 0:
        return str
    
    else:
        return inverterString(str[1:]) + str[0]

palavra = input("Escreva uma palavra: ")
print(inverterString(palavra))