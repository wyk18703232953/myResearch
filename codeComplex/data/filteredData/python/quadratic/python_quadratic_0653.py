import random

def main(n: int):
    # 生成测试数据：n 个 1~100 之间的随机正整数
    a = [random.randint(1, 100) for _ in range(n)]

    a.sort()
    k = 0
    for i in range(n):
        if a[i]:
            k += 1
            for j in range(i + 1, n):
                if a[j] and a[j] % a[i] == 0:
                    a[j] = 0
    print(k)