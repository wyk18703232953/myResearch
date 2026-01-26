import sys
from math import floor

if __name__ == '__main__':

    entrada = input()
    entrada_str = list(entrada.split(" "))
    entrada_int = list(map(int, entrada_str))

    a = entrada_int[0]
    b = entrada_int[1]

    if a == b:
        print(0)
        sys.exit()

    string_1 = ""
    string_2 = ""
    while a:
        if a%2 == 0:
            string_1 = string_1 + "0"
        else:
            string_1 = string_1 + "1"
        a = floor(a/2)

    while b:
        if b%2 == 0:
            string_2 = string_2 + "0"
        else:
            string_2 = string_2 + "1"
        b = floor(b/2)

    lista_1 = list(string_1)
    lista_1.reverse()
    contrario_1 = "".join(lista_1)

    lista_2 = list(string_2)
    lista_2.reverse()
    contrario_2 = "".join(lista_2)

    if len(string_1) != len(string_2):
        resposta = pow(2, len(string_2)) - 1
    else:
        potencia = 0
        for i in range(len(string_1)):
            if contrario_1[i] != contrario_2[i]:
                break
            potencia += 1

        potencia = len(string_1) - potencia
        resposta = pow(2, potencia)-1

    print(resposta)



		    		 			  				 	 	   		 		