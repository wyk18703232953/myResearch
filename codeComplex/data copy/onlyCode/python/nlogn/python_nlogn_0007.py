
def crear_intervalo(x,a):
    lim_inf = x-a/2
    lim_sup = x+a/2
    intervalo = (lim_inf, lim_sup)
    return intervalo

def calcular_posibles_posiciones(i1, i2, t):
    espacio_disponible = i2[0] - i1[1]
    espacio_sobrante = espacio_disponible - t
    if espacio_sobrante > 0:
        return 2
    elif espacio_sobrante == 0:
        return 1
    else:
        return 0

intervalos = []
posibilidades = 2

datos = input().split()
n,t = int(datos[0]), int(datos[1])

for i in range(n):
    casas = input().split()
    x, a = int(casas[0]), int(casas[1])
    intervalo = crear_intervalo(x,a)
    intervalos.append(intervalo)
    
intervalos.sort()

for i in range(n-1):
    posibilidades = posibilidades + calcular_posibles_posiciones(intervalos[i], intervalos[i+1],t)

print(posibilidades)

 