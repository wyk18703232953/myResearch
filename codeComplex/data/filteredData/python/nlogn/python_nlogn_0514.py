from collections import Counter
import random

def main(n: int):
    # 生成测试数据：t 组测试，每组长度为 n
    # 为了稳定产生有解的情况，让数组元素在较小范围内重复较多
    t = 1
    print(f"t = {t}, n = {n}")

    for _ in range(t):
        # 生成长度为 n 的数组 A，元素在 [1, max(4, n//5)] 范围内
        value_range = max(4, n // 5)
        A = [random.randint(1, value_range) for _ in range(n)]

        # 输出测试数据概览（可按需要保留/删除）
        print("Generated A (first 50 elements or less):", A[:50])

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

        print("Answer:", *ans)


if __name__ == "__main__":
    # 示例：调用 main(100)
    main(100)