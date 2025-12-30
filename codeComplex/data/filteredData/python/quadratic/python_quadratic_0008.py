import math
import random

def main(n):
    # 生成测试数据：半径 r 和 n 个点的位置 x[i]
    # 这里示例：r 固定为 10，x 为 0~1000 内递增随机数
    r = 10
    x = []
    cur = 0
    for _ in range(n):
        cur += random.randint(0, 20)
        x.append(cur)

    ans = []
    for i in range(n):
        t = r
        for j in range(i):
            a = abs(x[i] - x[j])
            if a <= 2 * r:
                t2 = (2 * r) ** 2
                t2 -= a ** 2
                t2 = math.sqrt(t2) + ans[j]
                t = max(t, t2)
        ans.append(t)

    for k in ans:
        print(k)

if __name__ == "__main__":
    # 可根据需要调整规模
    main(5)