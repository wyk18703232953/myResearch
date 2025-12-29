import random

def main(n: int):
    # 随机生成一个长度为 n 的数字串（可能包含前导 0）
    digits = [str(random.randint(0, 9)) for _ in range(n)]
    a = sorted(digits)

    # 生成一个随机上界 b（这里让 b 的位数在 [1, n+1] 之间）
    # 以保证有较大概率存在可行解
    max_len_b = n + 1
    len_b = random.randint(1, max_len_b)
    # 第一位不为 0，其他位任意
    first_digit = random.randint(1, 9)
    other_digits = [str(random.randint(0, 9)) for _ in range(len_b - 1)]
    b_str = str(first_digit) + "".join(other_digits)
    b = int(b_str)

    # 原逻辑（去掉 input() 后直接使用生成的 a 和 b）
    a = a[::-1]  # reverse a
    p = ''
    cnt = [0] * 10  # 原代码中未使用，但保留结构

    while a:
        for i, d in enumerate(a):
            # 构造当前选择 d 后，剩余数字按升序排列的最小可能数 n_str
            n_str = p + d + "".join(sorted(a[:i] + a[i + 1:]))
            if int(n_str) <= b:
                p += d
                a.pop(i)
                break

    print("generated_digits:", "".join(digits))
    print("b:", b)
    print("result:", p)


if __name__ == "__main__":
    # 示例：n=5，可自行调整
    main(5)