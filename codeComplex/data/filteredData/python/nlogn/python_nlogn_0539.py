from math import log
import random

def main(n):
    # 生成测试数据：随机选择 k，生成 n 个随机正整数
    # 可根据需要调整范围
    k = random.randint(1, 10**9)
    s = [random.randint(1, 10**9) for _ in range(n)]

    ans = 0
    for j in range(11):
        d = dict()
        z = 10 ** j
        # 预处理：统计 (i * z) % k 的频次
        for i in s:
            y = i * z
            u = y % k
            if u in d:
                d[u] += 1
            else:
                d[u] = 1
        # 枚举每个 i 作为右侧数
        for i in s:
            y = i
            lg = int(log(i, 10)) + 1
            lg = 10 ** lg
            if lg == z:
                key = (y * z) % k
                d[key] -= 1
                x = (k - y % k) % k
                if x in d:
                    ans += d[x]
                d[key] += 1
    print(ans)

if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)