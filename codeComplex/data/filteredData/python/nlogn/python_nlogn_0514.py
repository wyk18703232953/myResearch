import sys
from collections import Counter

def main(n):
    # n 表示数组 A 的长度规模
    if n <= 0:
        return

    # 确定性生成长度为 n 的数组 A
    # 构造一些重复元素以保证计数逻辑有意义
    A = [i % (max(2, n // 3)) + 1 for i in range(n)]

    t = 1  # 单组测试，用规模 n 控制数据大小

    outputs = []
    for _ in range(t):
        C = Counter(A)
        B = []
        for k, v in C.items():
            if v >= 4:
                B.append(k)
                B.append(k)
            elif v >= 2:
                B.append(k)
        B.sort()
        l = len(B)
        m = 10**18
        ans = [-1, -1, -1, -1]
        for i in range(l - 1):
            x, y = B[i], B[i + 1]
            temp = (4 * (x + y) ** 2) / (x * y)
            if temp < m:
                m = temp
                ans = [x, x, y, y]
        outputs.append(" ".join(map(str, ans)))

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    # 示例调用：可修改 n 以改变规模
    main(10000)