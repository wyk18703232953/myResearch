import random
import string

def main(n: int):
    # 1. 生成测试数据
    # 生成长度为 n 的字符串 s，由数字字符组成
    s = ''.join(random.choice(string.digits) for _ in range(n))
    # 生成一个规模相关的整数 b，使得 b 在 0 到 10^n - 1 之间
    # 为避免超大整数，可以在 n 过大时限制 b 的构造方式
    if n <= 18:
        max_val = 10 ** n - 1
        b = random.randint(0, max_val)
    else:
        # 对于特别大的 n，只使用前 18 位生成 b 的上界
        max_val = 10 ** 18 - 1
        b = random.randint(0, max_val)

    # 2. 将原始逻辑封装执行
    a = ''.join(reversed(sorted(s)))
    r = ''
    while len(a) > 0:
        for i in range(len(a)):
            candidate = r + a[i] + ''.join(sorted(a[:i] + a[i+1:]))
            if int(candidate) <= b:
                r += a[i]
                a = a[:i] + a[i+1:]
                break

    # 3. 输出结果（可根据需要调整打印内容）
    print("s =", s)
    print("b =", b)
    print("result =", r)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)