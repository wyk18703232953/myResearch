def main(n):
    # 将 n 映射为一对正整数 (a, b)，保持规模与 n 同阶
    # 这里选择 a = n + 1, b = n + 2，保证 b > 0 且两者随 n 线性增长
    a = n + 1
    b = n + 2

    s = 0
    while b:
        s += a // b
        a, b = b, a % b
    return s


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 以进行规模实验
    for n in range(1, 11):
        # print(n, main(n))
        pass