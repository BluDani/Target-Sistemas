num = int(input("Digite um número: "))

ant = 1
pos = 1

while True:

    auxiliar = pos
    pos += ant
    ant = auxiliar

    #Se o a sequência ultrapassar o número, ele não pertence a sequência
    if(pos > num):
        print(f"\033[031m\nO número {num} não pertence a sequência de Fibonacci\033[0m")
        break

    elif(num == pos):
        print(f"\033[032m\nO número {num} pertence a sequência de Fibonacci\033[0m")
        break