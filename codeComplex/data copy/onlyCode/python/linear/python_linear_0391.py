from sys import stdin, stdout


def main():
    p = 998244353  # Constante brindada por el problema
    n = int(stdin.readline())
    a = list(readline())
    answer = a[-1]
    pow_ = 1  # Potencia de 2
    for i in range(n - 1, 0, -1):  # Se analizan todas las dificultades
        answer = (answer + a[i - 1] * (2 + n - i) * pow_ % p) % p  # Se calcula la expresion
        pow_ = pow_ * 2 % p  # Se aumenta la potencia de 2
    return answer


def readline():  # Metodo para leer una linea completa, dividirla en elementos y convertirlos en numeros enteros
    return map(int, stdin.readline().strip().split())


if __name__ == '__main__':
    stdout.write(str(main()) + '\n')
