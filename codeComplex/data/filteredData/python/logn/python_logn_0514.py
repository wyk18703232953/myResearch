def main(n):
    # 生成规模为 n 的测试数据：这里理解为要查询的位置 n
    # 若需要，可在此根据 n 构造更复杂的测试数据
    pos = n - 1  # 与原程序中 n = int(input()) - 1 对应

    c = 0
    for i in range(11):
        c += 9 * (i + 1) * (10 ** i)
        if c > pos:
            pos -= (c - 9 * (i + 1) * (10 ** i))
            v = pos // (i + 1)
            ch = str(10 ** i + v)[pos % (i + 1)]
            print(ch)
            return

# 示例调用
if __name__ == "__main__":
    # 例如：查询第 15 位（从 1 开始计），传入 n=15
    main(15)