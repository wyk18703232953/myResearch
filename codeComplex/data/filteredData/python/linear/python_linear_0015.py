import math
import random

def main(n):
    # 生成测试数据：k 取 [1, n] 之间的随机整数（含 1，不含 n 时处理）
    if n < 3:
        print("NO")
        return

    k = random.randint(1, max(1, n - 1))

    l = []
    c = 0
    for j in range(2, n):
        p = 0
        for i in range(2, int(math.isqrt(j)) + 1):
            if j % i == 0:
                p = 1
                break
        if p == 0:
            l.append(j)

    l.append(n)

    for i in range(len(l) - 1):
        if (l[i] + l[i + 1] + 1) in l:
            c += 1

    if c >= k:
        print("YES")
    else:
        print("NO")


# 示例调用
if __name__ == "__main__":
    # 可根据需要调整 n 的规模
    main(50)