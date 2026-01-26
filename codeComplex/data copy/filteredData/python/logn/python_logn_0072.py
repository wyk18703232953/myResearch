def main(n):
    # Deterministically generate two integers a and b based on n
    # Ensure a != b for most n, but keep it deterministic
    a = n
    b = 2 * n + 1

    if a == b:
        # print(0)
        pass
        return

    string_1 = ""
    string_2 = ""

    temp_a = a
    temp_b = b

    from math import floor

    while temp_a:
        if temp_a % 2 == 0:
            string_1 = string_1 + "0"

        else:
            string_1 = string_1 + "1"
        temp_a = floor(temp_a / 2)

    while temp_b:
        if temp_b % 2 == 0:
            string_2 = string_2 + "0"

        else:
            string_2 = string_2 + "1"
        temp_b = floor(temp_b / 2)

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
        resposta = pow(2, potencia) - 1

    # print(resposta)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)