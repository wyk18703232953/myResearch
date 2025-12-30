import random

def rec(i, n, l, l2):
    if i == n:
        return []
    else:
        x = l2[i]
        flag = 0
        o = []
        p = []
        mi = -1
        for j in l:
            if j < x:
                if j > mi:
                    if i == 0 and j == 0:
                        o.append(j)
                        p.append(j)
                        continue
                    mi = j

            if x == j:
                flag = 1

            o.append(j)
            p.append(j)

        if flag:
            o.remove(x)

        if mi == -1 and flag == 0:
            return []

        ans1 = []
        if flag:
            ans1 = [x] + rec(i + 1, n, o, l2)

        if mi != -1:
            p.remove(mi)

        p.sort(reverse=True)
        ans2 = [mi] + p
        if len(ans1) == n - i:
            return ans1
        else:
            return ans2


def main(n):
    """
    自动生成规模为 n 的测试数据并执行原逻辑。
    n: 控制第二个数 b 的位数（保证 n >= 1）
    """
    if n < 1:
        raise ValueError("n must be >= 1")

    # 生成 b：恰好 n 位，最高位不为 0
    first_digit_b = random.randint(1, 9)
    other_digits_b = [random.randint(0, 9) for _ in range(n - 1)]
    l2 = [first_digit_b] + other_digits_b
    b = int("".join(str(d) for d in l2))

    # 生成 a：位数在 [1, n+1] 之间，最高位不为 0
    len_a = random.randint(1, n + 1)
    first_digit_a = random.randint(1, 9)
    other_digits_a = [random.randint(0, 9) for _ in range(len_a - 1)]
    l1 = [first_digit_a] + other_digits_a
    a = int("".join(str(d) for d in l1))

    # 保持与原程序逻辑一致
    e1 = str(a)
    e2 = str(b)
    l1 = [int(ch) for ch in e1]
    l2 = [int(ch) for ch in e2]

    if len(l1) < len(l2):
        l1.sort(reverse=True)
        o = [str(i) for i in l1]
        result = "".join(o)
    else:
        n_local = len(l2)
        ans = rec(0, n_local, l1, l2)
        w = [str(i) for i in ans]
        result = "".join(w)

    print(result)


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)