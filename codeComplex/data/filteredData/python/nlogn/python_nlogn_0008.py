import random

def main(n: int) -> int:
    # 生成测试数据：
    # n: 区间个数
    # t: 间隔阈值，随机生成一个正整数
    t = random.randint(1, 10)

    # 生成 n 组 (a, b)，保证 b>0 以便有意义的区间长度
    # a 取在 [-50, 50]，b 取在 (0, 20]
    arr = []
    for _ in range(n):
        a = random.randint(-50, 50)
        b = random.randint(1, 20)
        arr.append((a - (b / 2), a + (b / 2)))

    # 按原始逻辑处理
    arr.sort()
    ans = 0
    for i in range(1, n):
        diff = abs(arr[i][0] - arr[i - 1][1])
        if diff == t:
            ans += 1
        elif diff > t:
            ans += 2

    result = ans + 2
    print(result)
    return result

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)