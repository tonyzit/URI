import string

def cifrador(caracteres, cifra):
    abc = list(string.ascii_uppercase)
    criptografia = []
    cont=0
    for i in caracteres:
        cont=cont+1
        if i == abc[cont]:
            print(abc[cont])
            criptografia.append(abc[cont+cifra])  
    return criptografia

def main():
    vezes = int(input())
    cont=0
    #while(cont!=vezes):
    palavra = list(input())
    casas = int(input())
    print(str(cifrador(palavra,casas)).strip('[]').replace(', ',''))
    vezes = vezes+1
main()