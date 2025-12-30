import random

def main(n: int):
    # 生成测试数据：n 个 1~10^9 之间的随机正整数
    a = [random.randint(1, 10**9) for _ in range(n)]

    a.sort()
    k = 0
    used = [0] * n
    for i in range(n):
        if used[i]:
            continue
        k += 1
        for j in range(i, n):
            if a[j] % a[i] == 0:
                used[j] = True
    print(k)