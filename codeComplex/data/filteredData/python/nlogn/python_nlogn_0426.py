from collections import Counter
import random

def main(n):
    # 生成测试数据：n 个范围在 [-1e9, 1e9] 的随机整数
    a = [random.randint(-10**9, 10**9) for _ in range(n)]

    d = Counter(a)
    ans = 0
    for i in range(n):
        for j in range(31):
            s = 1 << j
            s = s - a[i]
            if d.get(s) is not None and ((d[s] == 1 and s != a[i]) or d[s] >= 2):
                break
        else:
            ans += 1
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(10)