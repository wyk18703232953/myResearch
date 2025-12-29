from math import log
from collections import deque
import random

def main(n):
    # 生成测试数据：规模为 n 的数组 s，以及一个正整数 k
    # 这里示例：元素在 [1, 10^9]，k 在 [1, 10^9]
    random.seed(0)
    k = random.randint(1, 10**9)
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
                key = (y * z) % k
                d[key] -= 1
                x = (k - y % k)
                if y % k == 0:
                    x = 0
                if x in d:
                    ans += d[x]
                d[key] += 1
                aux += 1
            else:
                break

        for _ in range(aux):
            s1.popleft()

    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(10)