import random

def main(n):
    # 生成测试数据：
    # n: 数组长度
    # k: 范围参数，设为与数值范围相关
    # a: 长度为 n 的整数数组
    if n <= 0:
        return 0

    # 可以根据需要调整随机范围
    max_val = max(10, n * 2)
    k = random.randint(0, max_val // 4)  # 示例：k 在一个较小范围内
    a = [random.randint(0, max_val) for _ in range(n)]

    # 保持原逻辑
    a.sort()
    slow, fast = 0, 0
    while fast < n:
        if a[slow] == a[fast]:
            fast += 1
        elif abs(a[slow] - a[fast]) <= k:
            a[slow] = 0
            slow += 1
        else:
            slow += 1

    ans = 0
    for i in a:
        if i != 0:
            ans += 1

    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)