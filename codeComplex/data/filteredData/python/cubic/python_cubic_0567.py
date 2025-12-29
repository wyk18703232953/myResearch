import random

def main(n: int):
    # 1. 生成测试数据
    # 生成一个长度为 n 的数字串 a，由字符 '0'-'9' 随机组成
    # 生成一个整数 b，范围为 [0, 10^n - 1]
    digits = [str(random.randint(0, 9)) for _ in range(n)]
    a = digits[:]  # 列表形式
    # 构造 b：随机一个 n 位以内的整数
    if n <= 18:  # 避免太大的数，int 也可以承受更大，但这里做个保险
        b = random.randint(0, 10**n - 1)
    else:
        # 对于非常大的 n，用前 18 位限定范围
        b = random.randint(0, 10**18 - 1)

    # 2. 原始逻辑
    a.sort()
    a = a[::-1]
    prefix = ""
    while len(a) > 0:
        for i in range(len(a)):
            num = prefix + a[i] + "".join(sorted(a[:i] + a[i+1:]))
            if int(num) <= b:
                prefix += a[i]
                a = a[:i] + a[i+1:]
                break

    # 输出结果
    print(prefix)


if __name__ == "__main__":
    # 示例调用：n 为生成的数字串长度
    main(5)