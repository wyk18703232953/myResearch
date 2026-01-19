def factorial(n):
    total = 1
    for i in range(int(n)):
        total *= (i + 1)
    return total

def solve(s1, s2):
    objetivo = s1.count("+") - s1.count("-")
    inicio = s2.count("+") - s2.count("-")
    incognitos = s2.count("?")
    distancia = objetivo - inicio

    if abs(distancia) > incognitos or distancia % 2 != incognitos % 2:
        return 0
    else:
        mas = (distancia + incognitos) / 2
        menos = (incognitos - distancia) / 2
        return (factorial(incognitos) / (factorial(mas) * factorial(menos))) / 2 ** incognitos

def main(n):
    if n < 1:
        n = 1
    # s1: first n characters, deterministic pattern of '+' and '-'
    s1 = "".join("+" if i % 2 == 0 else "-" for i in range(n))
    # s2: same length, pattern using '+', '-', '?' deterministically
    s2 = "".join("+" if i % 3 == 0 else "-" if i % 3 == 1 else "?" for i in range(n))
    result = solve(s1, s2)
    print(result)

if __name__ == "__main__":
    main(10)