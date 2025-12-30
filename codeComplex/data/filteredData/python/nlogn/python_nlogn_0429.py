from collections import Counter
import random

def main(n):
    # 生成测试数据：在 1 到 1e9 范围内生成 n 个随机整数
    a = [random.randint(1, 10**9) for _ in range(n)]

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

# 示例调用
if __name__ == "__main__":
    main(10)