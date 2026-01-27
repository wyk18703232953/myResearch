def d(a, b):
    return a + b

def main(n):
    # 确定性生成 x, y，使其与 n 相关联
    # 映射规则：
    # x 在 [1, n] 之间循环，y 在 [1, n] 之间循环，但相对错位
    if n <= 0:
        return

    x = (n % n) + 1  # 恒为 1
    y = ((n // 2) % n) + 1

    if d(x - 1, y - 1) <= d(n - x, n - y):
        # print("White")
        pass

    else:
        # print("Black")
        pass
if __name__ == "__main__":
    main(10)