def main(n: int):
    """
    规模 n 用于生成测试数据：
    - 这里令 x = n, y = 3n，保证 y > x 且间隔可变
    - 若需要其他模式，可根据需求调整生成规则
    """
    x = n
    y = 3 * n

    if y - x < 2:
        print(-1)
    elif x % 2 != 0 and y - x == 2:
        print(-1)
    elif x % 2 == 0:
        print(x, x + 1, x + 2)
    else:
        print(x + 1, x + 2, x + 3)


if __name__ == "__main__":
    # 示例：可以在此手动调整 n 做简单测试
    main(5)