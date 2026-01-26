def prime2(n):
    cont = 0
    flag = True
    while flag:
        if n % 2 == 0:
            cont += 1
            n = n // 2

        else:
            flag = False
    if n % 4 == 1:
        return [cont, "L"]

    else:
        return [cont, "R"]


def arrivo(n, start, char):
    for i in char:
        if (i == "L" or i == "R") and start % 2 == 1:
            pass
        elif (i == "U") and 2 * start == n + 1:
            pass

        else:
            [power, direc] = prime2(start)
            if i == "L":
                start -= 2 ** (power - 1)
            elif i == "R":
                start += 2 ** (power - 1)
            else:  # 'U'
                if direc == "L":
                    start += 2 ** power

                else:
                    start -= 2 ** power
    return start


def main(n):
    # 生成测试数据：q组查询
    # 按规模 n 线性生成 q，至少 1 组
    q = max(1, n)  # 可以根据需要调整为其他函数，例如 q = min(n, 10)
    results = []

    for i in range(q):
        # 生成 start：在 [1, n] 范围循环
        start = (i % n) + 1

        # 生成指令串 char：长度随 n 变化
        # 这里选用长度 = min(20, n)，由字符 'L', 'R', 'U' 组成的简单规律序列
        length = min(20, n)
        base = "LRU"
        char = "".join(base[j % 3] for j in range(i, i + length))

        res = arrivo(n, start, char)
        results.append(res)

    # 输出结果
    for r in results:
        # print(r)
        pass
if __name__ == '__main__':
    # 示例：调用 main，n 可按需求修改
    main(10)