import random

def main(n):
    # 1. 生成长度为 n 的数字串（不以 0 开头）
    #    为了保证有意义的上界 b，这里生成的 b 至少 >= 生成的数字本身
    digits = [str(random.randint(0, 9)) for _ in range(n)]
    if digits[0] == '0':
        digits[0] = str(random.randint(1, 9))
    mass = digits[:]  # 拷贝一份作为原算法的输入字符串
    num_str = ''.join(mass)
    b = int(num_str) + random.randint(0, 10 ** max(1, n // 2))

    # 原始逻辑开始
    mass = list(mass)
    mass.sort()
    mass = mass[::-1]
    p = ''
    while len(mass) > 0:
        for i in range(len(mass)):
            n_str = p + mass[i] + ''.join(sorted(mass[:i] + mass[i + 1:]))
            if int(n_str) <= b:
                p += mass[i]
                mass = mass[:i] + mass[i + 1:]
                break

    print(p)


if __name__ == "__main__":
    # 示例：运行规模 n=5
    main(5)