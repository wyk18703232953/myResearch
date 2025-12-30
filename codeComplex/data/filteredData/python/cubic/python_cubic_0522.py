import random

def permuteDigits(a, b):
    n = len(a)
    if len(a) < len(b):
        return a

    i = 0
    c = 0
    t = a[0]
    flag = 0
    lastind = []
    while i < len(a) and i < len(b) and a[i] >= b[i]:
        if c == n:
            i = i - 1
            t = a[i]
            a = a[:i] + a[i+1:]
            a.insert(lastind.pop(), t)
            flag = 1
            c = i
        elif (flag == 0 and a[c] == b[i]) or a[c] < b[i]:
            lastind.append(c)
            t = a[c]
            a = a[:c] + a[c+1:]
            a.insert(i, t)
        else:
            c = c + 1

        if a[i] < b[i]:
            break
        elif flag == 0 and a[i] == b[i]:
            i = i + 1
            c = i
    return a


def main(n):
    # 1. 根据规模 n 生成测试数据
    # 生成一个长度为 n 的随机数字串 aa（不以 0 开头）
    if n <= 0:
        return

    first_digit = random.randint(1, 9)
    other_digits = [random.randint(0, 9) for _ in range(n - 1)]
    aa_digits = [first_digit] + other_digits
    aa = "".join(str(d) for d in aa_digits)

    # 生成一个不大于 aa 的随机数字串 bb（长度 <= n）
    # 这里简单生成同长度的随机数字串，再截断到不超过 aa 的排序上界
    bb_len = random.randint(1, n)
    first_digit_b = random.randint(1, 9)
    other_digits_b = [random.randint(0, 9) for _ in range(bb_len - 1)]
    bb_digits = [first_digit_b] + other_digits_b
    bb = "".join(str(d) for d in bb_digits)

    # 2. 按原逻辑处理
    a = [int(ch) for ch in aa]
    b = [int(ch) for ch in bb]

    a.sort(reverse=True)

    ans = permuteDigits(a, b)
    s = "".join(str(x) for x in ans)
    print(int(s))


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(8)