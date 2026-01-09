def main(n):
    # 根据 n 确定性生成 a 和 b
    a = n
    b = n // 2 + 1

    c = 1
    result = a ^ b
    while c <= result:
        c *= 2
    c -= 1

    return c

if __name__ == "__main__":
    # 示例调用
    # print(main(10))
    pass