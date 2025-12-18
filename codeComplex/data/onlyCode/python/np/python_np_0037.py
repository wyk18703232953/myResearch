s1 = input()
s2 = input()

objetivo = s1.count("+") - s1.count("-")
inicio = s2.count("+") - s2.count("-")
incognitos = s2.count("?")
distancia = objetivo - inicio

def factorial(n):
    total = 1
    for i in range(int(n)):
        total *= (i + 1)
    return total

if abs(distancia) > incognitos or distancia % 2 != incognitos % 2:
    print(0)
else:
    mas = (distancia + incognitos) / 2
    menos = (incognitos - distancia) / 2
    print((factorial(incognitos)/(factorial(mas)*factorial(menos)))/2**incognitos)
