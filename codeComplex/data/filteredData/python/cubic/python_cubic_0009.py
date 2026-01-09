def main(n):
    # Deterministically generate a string of length n over a small alphabet
    # Pattern: repeating 'abcde' so that longer repeated substrings exist
    base = "abcde"
    cadena = "".join(base[i % len(base)] for i in range(n))

    n_len = len(cadena)
    rpta = 0

    for i in range(n_len - 1):
        tamanho_cadena = n_len - i - 1
        for j in range(n_len - tamanho_cadena):
            subcadena = cadena[j:j + tamanho_cadena]
            contador = 1
            for k in range(n_len - tamanho_cadena - j):
                if subcadena == cadena[j + k + 1:j + k + 1 + tamanho_cadena]:
                    contador = contador + 1
            if contador >= 2 and rpta == 0:
                rpta = tamanho_cadena
        if rpta != 0:
            break

    # print(rpta)
    pass
if __name__ == "__main__":
    main(100)