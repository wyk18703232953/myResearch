import random

def main(n):
    # 1. 生成测试数据
    # 生成一个长度为 n 的数字串（允许前导 0）
    digits = [str(random.randint(0, 9)) for _ in range(n)]
    s = ''.join(digits)
    # 生成 b：在所有数字最大排列和最小排列之间随机取值
    a_sorted_desc = ''.join(sorted(s, reverse=True))
    a_sorted_asc = ''.join(sorted(s))
    max_val = int(a_sorted_desc)
    min_val = int(a_sorted_asc)
    b = random.randint(min_val, max_val)

    # 2. 原逻辑（去掉 input，使用生成的 s 和 b）
    a = sorted(s, reverse=True)
    k = ""
    while len(a) > 0:
        for i in range(len(a)):
            num = k + a[i] + "".join(sorted(a[:i] + a[i + 1:]))
            if int(num) <= b:
                k += a[i]
                a = a[:i] + a[i + 1:]
                break

    print(k)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(5)