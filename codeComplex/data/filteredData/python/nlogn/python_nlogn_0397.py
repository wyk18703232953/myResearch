import random
import math

def my_cmp(x):
    if x[0] == 0:
        return float('inf')
    return x[1] / x[0]

def dis(a, b):
    return a * a + b * b

def main(n):
    # 生成规模为 n 的测试数据：n 个点 (x, y)
    # 这里示例生成范围在 [-10^3, 10^3] 的随机整数坐标
    random.seed(0)
    v = []
    for i in range(n):
        x = random.randint(-1000, 1000)
        y = random.randint(-1000, 1000)
        v.append((x, y, i))

    v.sort(key=my_cmp)

    x, y = 0, 0
    ans = [0] * n
    for i in range(n):
        if dis(x + v[i][0], y + v[i][1]) < dis(x - v[i][0], y - v[i][1]):
            ans[v[i][2]] = 1
        else:
            ans[v[i][2]] = -1
        x += v[i][0] * ans[v[i][2]]
        y += v[i][1] * ans[v[i][2]]

    for val in ans:
        print(val, end=' ')

# 示例调用
if __name__ == "__main__":
    main(10)