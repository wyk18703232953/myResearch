import math

def bi(n, k):
    MIN = 0
    MAX = n
    while MAX > MIN + 1:
        bn = (MIN + MAX) // 2
        if math.log2(k + 2 + bn) < bn + 1:
            MAX = bn
        elif math.log2(k + 2 + bn) == bn + 1:
            return bn

        else:
            MIN = bn
    if MAX + 1 <= math.log2(k + 2 + MAX):
        return MAX
    return MIN

def main(n):
    # 输入结构：testcase 组 (n, k)
    # 将 n 解释为 testcase 数量
    testcase = n
    T = []
    for i in range(testcase):
        ni = i + 1
        ki = (i * i + 3 * i + 5)  # 确定性生成 k
        T.append([ni, ki])

    outputs = []
    for n, k in T:
        if n == 1:
            if k == 1:
                outputs.append(("YES", 0))

            else:
                outputs.append(("NO",))
            continue

        if n == 2:
            if 1 <= k <= 2:
                outputs.append(("YES", 1))
            elif k == 3:
                outputs.append(("NO",))
            elif 4 <= k <= 5:
                outputs.append(("YES", 0))

            else:
                outputs.append(("NO",))
            continue

        if n <= 30 and k > (pow(4, n) - 1) // 3:
            outputs.append(("NO",))
            continue

        ANS = bi(n, k)
        outputs.append(("YES", n - ANS))

    # 模拟原程序的打印行为
    for out in outputs:
        if len(out) == 2:
            # print(out[0], out[1])
            pass

        else:
            # print(out[0])
            pass
if __name__ == "__main__":
    main(10)