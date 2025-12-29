import random

def main(n: int):
    # 生成规模为 n 的测试数据，这里生成区间 [-10, 10] 的随机整数
    # 你可根据需要修改生成规则
    a = [random.randint(-10, 10) for _ in range(n)]

    b = [abs(x) for x in a]
    if n == 1:
        ans = a[0]
    elif all(x > 0 for x in a) or all(x < 0 for x in a):
        b.sort()
        ans = sum(b) - 2 * b[0]
    else:
        ans = sum(b)

    print(ans)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)