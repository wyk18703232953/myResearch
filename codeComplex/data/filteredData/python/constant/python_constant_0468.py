import random

def main(n: int):
    # n 表示要生成的测试组数
    for _ in range(n):
        # 生成测试数据范围可按需调整，这里取 [-10^9, 10^9]
        bx = random.randint(-10**9, 10**9)
        by = random.randint(-10**9, 10**9)
        ax = random.randint(-10**9, 10**9)
        ay = random.randint(-10**9, 10**9)
        cx = random.randint(-10**9, 10**9)
        cy = random.randint(-10**9, 10**9)

        num1 = ax > bx
        num3 = cx > bx
        num2 = ay > by
        num4 = cy > by

        if num1 == num3 and num2 == num4:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    # 示例：运行 5 组随机测试
    main(5)