import random

def main(n: int) -> None:
    """
    n: 规模，表示生成的数字的位数
    程序逻辑基于原始代码：
    - a: 由随机数字组成的长度为 n 的列表
    - b: 由随机数字组成的长度为 n 的列表
    """

    # 生成测试数据：位数为 n 的两个“数字”（用数字列表表示）
    # 为避免前导 0 导致位数变短，首位保证非 0
    if n <= 0:
        return

    def gen_digits(length: int):
        if length == 1:
            return [random.randint(0, 9)]
        first = random.randint(1, 9)
        rest = [random.randint(0, 9) for _ in range(length - 1)]
        return [first] + rest

    a = sorted(gen_digits(n))
    b = gen_digits(n)
    bn = int(''.join(map(str, b)))
    res = int(''.join(map(str, sorted(a))))

    if len(b) != len(a):
        print(''.join(map(str, sorted(a, reverse=True))))
    else:
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i] < a[j] < b[i]:
                    a[i], a[j] = a[j], a[i]
            tmp = int(''.join(map(str, a[:i + 1] + sorted(a[i + 1:], reverse=True))))
            res = max(res, tmp) if tmp <= bn else res
            for j in range(i + 1, len(a)):
                if a[j] == b[i]:
                    a[i], a[j] = a[j], a[i]
        print(res)


if __name__ == "__main__":
    # 示例：调用 main(5) 进行一次运行
    main(5)