def crear_intervalo(x, a):
    lim_inf = x - a / 2
    lim_sup = x + a / 2
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


def main(n):
    # 生成测试数据：
    # 固定 t，也可按需改为函数参数
    t = 2

    # 简单生成 n 个“房子”：中心间隔为 (a + t)
    # 使得有些间隔刚好够，有些大于，有些小于
    intervalos = []
    for i in range(n):
        # a 固定为 2，中心位置按 3*i 递增
        x = 3 * i
        a = 2
        intervalo = crear_intervalo(x, a)
        intervalos.append(intervalo)

    intervalos.sort()
    posibilidades = 2  # 两端各一个

    for i in range(n - 1):
        posibilidades += calcular_posibles_posiciones(intervalos[i], intervalos[i + 1], t)

    print(posibilidades)


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)