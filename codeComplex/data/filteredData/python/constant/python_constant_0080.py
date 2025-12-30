def main(n: int):
    # 原逻辑计算函数
    def calc(x: int) -> int:
        if x < 3:
            return x
        else:
            if x % 2 != 0:
                return x * (x - 1) * (x - 2)
            else:
                if x == 6:
                    return 60
                elif x % 3 == 0:
                    return (x - 1) * (x - 2) * (x - 3)
                else:
                    return x * (x - 1) * (x - 3)

    # 根据 n 生成测试数据：这里生成 1 到 n 的整数作为测试规模
    for i in range(1, n + 1):
        print(calc(i))


if __name__ == "__main__":
    # 示例：可按需修改 n 的规模
    main(10)