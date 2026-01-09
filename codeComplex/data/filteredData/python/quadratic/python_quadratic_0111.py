import copy

def main(n):
    a = n

    # 生成确定性的矩阵 lista 和 listb，大小为 a x a
    # 元素为字符，通过简单算术构造
    lista = []
    listb = []
    for i in range(a):
        row_a = []
        row_b = []
        for j in range(a):
            # 构造字符：在 'a' 到 'z' 之间循环
            val_a = (i * a + j) % 26
            val_b = (j * a + i) % 26
            row_a.append(chr(ord('a') + val_a))
            row_b.append(chr(ord('a') + val_b))
        lista.append(row_a)
        listb.append(row_b)

    listacpy = copy.deepcopy(lista)
    flag = 0
    mark = 0

    # 直接比较
    for i in range(a):
        for j in range(a):
            if listacpy[i][j] != listb[i][j]:
                mark = 1
                break
        if mark == 1:
            break
    if mark == 0:
        flag = 1
    mark = 0

    # 转90°
    for i in range(a):
        for j in range(a):
            listacpy[a - 1 - j][i] = lista[i][j]

    for i in range(a):
        for j in range(a):
            if listacpy[i][j] != listb[i][j]:
                mark = 1
                break
        if mark == 1:
            break
    if mark == 0:
        flag = 1

    mark = 0

    # 转180°
    for i in range(a):
        for j in range(a):
            listacpy[a - 1 - i][a - 1 - j] = lista[i][j]

    for i in range(a):
        for j in range(a):
            if listacpy[i][j] != listb[i][j]:
                mark = 1
                break
        if mark == 1:
            break
    if mark == 0:
        flag = 1

    mark = 0

    # 转270°
    for i in range(a):
        for j in range(a):
            listacpy[j][a - 1 - i] = lista[i][j]

    for i in range(a):
        for j in range(a):
            if listacpy[i][j] != listb[i][j]:
                mark = 1
                break
        if mark == 1:
            break
    if mark == 0:
        flag = 1
    mark = 0

    # 翻面
    listtemp = copy.deepcopy(lista)
    for i in range(a):
        for j in range(a):
            lista[i][j] = listtemp[i][a - 1 - j]

    # 翻面后直接比
    listacpy = copy.deepcopy(lista)
    for i in range(a):
        for j in range(a):
            if listacpy[i][j] != listb[i][j]:
                mark = 1
                break
        if mark == 1:
            break
    if mark == 0:
        flag = 1
    mark = 0

    # 翻面后转90°
    for i in range(a):
        for j in range(a):
            listacpy[a - 1 - j][i] = lista[i][j]

    for i in range(a):
        for j in range(a):
            if listacpy[i][j] != listb[i][j]:
                mark = 1
                break
        if mark == 1:
            break
    if mark == 0:
        flag = 1
    mark = 0

    # 翻面后转180°
    for i in range(a):
        for j in range(a):
            listacpy[a - 1 - i][a - 1 - j] = lista[i][j]

    for i in range(a):
        for j in range(a):
            if listacpy[i][j] != listb[i][j]:
                mark = 1
                break
        if mark == 1:
            break
    if mark == 0:
        flag = 1

    mark = 0

    # 翻面后转270°
    for i in range(a):
        for j in range(a):
            listacpy[j][a - 1 - i] = lista[i][j]

    for i in range(a):
        for j in range(a):
            if listacpy[i][j] != listb[i][j]:
                mark = 1
                break
        if mark == 1:
            break
    if mark == 0:
        flag = 1

    if flag == 1:
        # print("yes")
        pass

    else:
        # print("no")
        pass
if __name__ == "__main__":
    main(10)