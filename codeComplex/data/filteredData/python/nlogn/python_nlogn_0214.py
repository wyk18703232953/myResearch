import random

def main(n):
    # 参数与测试数据生成
    u = random.randint(1, 10**6)
    # 生成严格递增的数组 e，模拟原题中常见的有序坐标/时间戳等
    e = []
    cur = 0
    for _ in range(n):
        cur += random.randint(1, 10)  # 保证递增
        e.append(cur)

    ans = -1.0
    k = 2
    for i in range(n - 2):
        while k < n - 1 and e[k + 1] - e[i] <= u:
            k += 1
        if i < k - 1 and e[k] - e[i] <= u:
            ans = max(ans, (e[k] - e[i + 1]) / (e[k] - e[i]))
    print(ans)

# 示例调用
if __name__ == "__main__":
    main(10)