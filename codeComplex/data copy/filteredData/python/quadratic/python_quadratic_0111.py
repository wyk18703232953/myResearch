def main(n):
    import copy

    # 使用 n 作为矩阵规模 a
    a = max(1, int(n))

    # 生成确定性的 a x a 矩阵 lista（字符）
    # 元素为 'A' + ((i * a + j) % 26)
    lista = []
    for i in range(a):
        row = []
        for j in range(a):
            val = chr(ord('A') + ((i * a + j) % 26))
            row.append(val)
        lista.append(row)

    # 生成 listb：根据 n 的奇偶确定生成方式，保证可重复
    # n 为偶数：listb = lista（应输出 "yes"）
    # n 为奇数：listb 为 90° 旋转后的矩阵（同样应输出 "yes"）
    # 这样既有非平凡变换，又保持与原逻辑一致
    listb = []
    if a % 2 == 0:
        for i in range(a):
            listb.append(lista[i][:])

    else:
        # 生成 90° 旋转后的矩阵作为目标
        listb = [[None] * a for _ in range(a)]
        for i in range(a):
            for j in range(a):
                listb[a - 1 - j][i] = lista[i][j]

    flag = 0
    mark = 0

    listacpy = copy.deepcopy(lista)

    # 一来就比
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
    main(5)