MAX = 10**9  # O((n*m + (2**m)**2) * log(MAX))
import random

def main(n):
    # 自行设定 m 的规模，这里设为与 n 同阶，可根据需要调整
    m = max(1, min(10, n))  # 防止 2^m 过大，这里限制 m <= 10

    # 生成测试数据：n 行，每行 m 个整数，范围 [0, MAX]
    arrs = [[random.randint(0, MAX) for _ in range(m)] for _ in range(n)]

    def convertToBinary(arr, minB):
        b = 0
        for i in range(m):
            if arr[i] >= minB:
                b |= (1 << i)
        return b

    def checkPossible(minB):
        binRepresentations = set()
        for arr in arrs:
            binRepresentations.add(convertToBinary(arr, minB))
        binList = list(binRepresentations)
        ii = jj = -1
        bn = len(binList)
        for i in range(bn):
            for j in range(i, bn):
                if binList[i] | binList[j] == (1 << m) - 1:
                    ii = binList[i]
                    jj = binList[j]
        if ii != -1:
            ansi = ansj = -1
            for i in range(len(arrs)):
                b = convertToBinary(arrs[i], minB)
                if b == ii:
                    ansi = i
                if b == jj:
                    ansj = i
            return (ansi, ansj)
        else:
            return None

    minB = -1
    i = j = -1
    b = MAX
    while b > 0:
        temp = checkPossible(minB + b)
        if temp is None:
            b //= 2
        else:
            minB += b
            i, j = temp
    i += 1
    j += 1
    print(f"{i} {j}")