def main(n: int):
    """
    对规模 n 生成类似原始逻辑的测试数据并输出：
    第一行：字符 '4' 重复 n 次
    第二行：字符 '5' 重复 n 次再加一个 '6'
    """
    # 根据 n 构造输出
    line1 = '4' * n
    line2 = '5' * n + '6'
    print(line1)
    print(line2)


if __name__ == "__main__":
    # 示例：当 n=1131 时，与原程序行为等价
    main(1131)