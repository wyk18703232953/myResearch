import math


def main(n: int):
    # 生成测试数据：这里假设 m = n，可按需求修改生成策略
    m = n

    result = []

    half_m = math.ceil(m / 2)
    half_n = math.ceil(n / 2)

    for column in range(1, half_m + 1):
        row_range = range(1, n + 1)
        # 如果是中间列且列数为奇数，则行也只到中间行
        if column == half_m and m % 2 == 1:
            row_range = range(1, half_n + 1)

        for row in row_range:
            result.append(f"{column} {row}")
            # 中心点只输出一次
            if (
                row == half_n
                and n % 2 == 1
                and column == half_m
                and m % 2 == 1
            ):
                continue
            result.append(f"{m + 1 - column} {n + 1 - row}")

    print("\n".join(result))


if __name__ == "__main__":
    # 示例：规模为 5，可按需要修改或在外部调用 main
    main(5)