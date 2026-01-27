def max1(a, b):
    if a >= b:
        return a, b

    else:
        return b, a

def minus(a, b):
    p = a // b
    cnt = p
    return b, (a - (b * cnt)), cnt

def main(n):
    # 解释规模映射（内部说明，不涉及外部输入）：
    # 使用 n 组测试数据，第 i 组为 (a, b) = (i + 1, 2 * i + 1)
    # 保持算法逻辑不变，仅由 n 决定数据规模且完全确定性。
    results = []
    for i in range(1, n + 1):
        a = i + 1
        b = 2 * i + 1
        cnt = 0
        while a > 0 and b > 0:
            a, b = max1(a, b)
            a, b, p = minus(a, b)
            cnt += p
        results.append(cnt)
    for value in results:
        # print(value)
        pass
if __name__ == "__main__":
    main(5)