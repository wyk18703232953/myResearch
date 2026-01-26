def main(n):
    # 原程序的含义：
    # 输入为两个整数 n, v
    # 这里将实验规模参数 n 映射为原程序中的 n
    # v 则设为一个确定性的函数，例如 v = n // 2 + 1
    if n < 1:
        return 0

    total_dist = n
    v = n // 2 + 1

    remaining_dist = total_dist - 1
    adding = min(remaining_dist, v)
    cost = adding

    remaining_dist -= adding

    i = 2
    while remaining_dist > 0:
        cost += i
        i += 1
        remaining_dist -= 1

    return cost


if __name__ == "__main__":
    # 示例：用若干不同规模调用 main
    for size in [1, 5, 10, 20]:
        # print(size, main(size))
        pass