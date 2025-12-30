import random
from collections import Counter

def main(n):
    # 1. 生成测试数据：长度为 n 的数组 a，元素为 1..1e9 之间的随机整数
    a = [random.randint(1, 10**9) for _ in range(n)]

    # 2. 将原逻辑应用到生成的测试数据上
    C = Counter(a)
    unique_vals = set(a)

    ans = 0
    for x in unique_vals:
        ok = True
        for i in range(65):
            need = (1 << i) - x
            if need == x and C[need] > 1:
                ok = False
                break
            if need != x and C[need] > 0:
                ok = False
                break
        ans += C[x] * ok

    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：运行规模 n=10
    main(10)