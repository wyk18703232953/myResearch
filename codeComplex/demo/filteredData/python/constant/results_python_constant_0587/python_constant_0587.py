def main(n):
    # 确定性生成 x, y
    x = n // 3 + 1
    y = n - x
    a = 1 + 1
    b = n + n
    c = x + y
    distance_w = c - a
    distance_b = b - c
    if distance_w == distance_b:
        return 'White'
    if distance_w < distance_b:
        return 'White'
    return 'Black'


if __name__ == "__main__":
    # 示例调用
    result = main(10)
    # print(result)
    pass