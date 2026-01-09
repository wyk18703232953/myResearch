def iscomposite(value):
    for i in range(2, value):
        if value % i == 0:
            return '1'

    else:
        return '0'


def main(n):
    # 保持原逻辑：从 4 到 n-1 搜索 a,b 且 a+b=n，a,b 均为合数
    # 为了可规模化实验，仅执行逻辑，不依赖输入
    for i in range(4, n):
        a = i
        b = n - i
        if iscomposite(a) == '1' and iscomposite(b) == '1':
            # 输出一次找到的分解
            # print(a, b)
            pass
            break


if __name__ == "__main__":
    # 示例：使用 n=100 作为规模
    main(100)