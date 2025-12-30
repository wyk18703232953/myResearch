import random

def main(n):
    """
    n: 控制测试数据规模，这里用于控制 a,b 的最大值范围
    生成 1 <= a < b <= max(3, n) 的一组数据并执行原逻辑
    """
    upper = max(3, n)

    a = random.randint(1, upper - 1)
    b = random.randint(a + 1, upper)

    if max(a, b) - min(a, b) + 1 <= 2:
        print(-1)
    elif max(a, b) - min(a, b) + 1 == 3:
        if a % 2 == 1 and b % 2 == 1:
            print(-1)
        else:
            print(min(a, b), min(a, b) + 1, min(a, b) + 2)
    else:
        ans = 0
        for i in range(a, b + 1):
            if i % 2 == 0:
                ans = i
                break
        print(ans, ans + 1, ans + 2)


if __name__ == "__main__":
    # 示例：使用 n = 10 运行
    main(10)