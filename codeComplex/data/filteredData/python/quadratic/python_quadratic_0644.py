import random

def main(n: int) -> int:
    # 生成测试数据：n 个 [1, 10*n] 之间的随机整数
    l = [random.randint(1, 10 * n) for _ in range(n)]

    l.sort()
    v = [False for _ in range(n)]
    ans = 0
    i = 0
    while i < n:
        if not v[i]:
            ans += 1
            for j in range(i + 1, n):
                if l[j] % l[i] == 0:
                    v[j] = True
        i += 1
    print(ans)
    return ans