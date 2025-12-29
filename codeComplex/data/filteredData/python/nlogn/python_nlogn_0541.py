from math import log
from collections import deque
import random

def main(n):
    # 生成测试数据：规模为 n
    # 这里假设 k 为适当范围内的正整数，并生成 n 个正整数
    # 可根据需要调整生成策略
    k = random.randint(1, 10**9)
    # 为避免全部为 0，生成 1~1e9 之间的整数
    s = [random.randint(1, 10**9) for _ in range(n)]

    ans = 0
    s.sort()
    s1 = deque(s)
    for j in range(11):
        d = dict()
        z = 10 ** j
        for i in s:
            y = i * z
            u = y % k
            if u in d:
                d[u] += 1
            else:
                d[u] = 1
        aux = 0
        for i in s1:
            y = i
            lg = int(log(i, 10)) + 1
            lg = 10 ** lg
            if lg == z:
                aux1 = (y * z) % k
                aux2 = y % k
                d[aux1] -= 1
                x = (k - aux2)
                if aux2 == 0:
                    x = 0
                if x in d:
                    ans += d[x]
                d[aux1] += 1
                aux += 1
            else:
                break
        for _ in range(aux):
            s1.popleft()
    print(ans)

# 示例调用
if __name__ == "__main__":
    main(10)