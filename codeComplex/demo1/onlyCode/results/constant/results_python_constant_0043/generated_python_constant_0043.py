def main(n: int):
    # 根据 n 生成测试数据：这里直接使用原题给定的“幸运数”列表
    details = [4, 7, 44, 77, 444, 777, 47, 74, 447, 774, 474, 747, 477]

    f = 0
    for i in details:
        if n % i == 0:
            f = 1
            break

    if f:
        print("YES")
    else:
        print("NO")


# 示例：需要时可自行调用，例如：
# main(28)