def get_num(g):
    s = [str(i) for i in g]
    num = int("".join(s))
    return num

def solve(a: str, b: str) -> int:
    bb = int(b)
    mark = [0 for _ in range(len(a))]
    f = []
    g = []

    for i in range(len(a)):
        g.append(a[i])

    g.sort()
    g.reverse()
    num = get_num(g)

    if num <= bb:
        return num

    index = []

    for i in range(0, min(len(a), len(b))):
        mx = '-1'
        idx = 0
        for j in range(len(a)):
            if mark[j] == 0 and a[j] <= b[i]:
                if a[j] > mx:
                    mx = a[j]
                    idx = j

        if mx == '-1':
            rem = []

            while len(f) > 0:
                ma = '-1'
                idd = 0
                for j in range(len(a)):
                    if mark[j] == 0 and a[j] < f[-1]:
                        if a[j] > ma:
                            ma = a[j]
                            idd = j

                if ma == '-1':
                    mark[index.pop()] = 0
                    f.pop()
                    continue
                else:
                    mark[index.pop()] = 0
                    f.pop()
                    f.append(ma)
                    mark[idd] = 1
                    break

            for j in range(len(a)):
                if mark[j] == 0:
                    rem.append(a[j])

            rem.sort()
            rem.reverse()

            for j in rem:
                f.append(j)

            return get_num(f)

        f.append(mx)
        mark[idx] = 1
        index.append(idx)

        if mx < b[i] and mx != '-1':
            break

    rem = []

    for i in range(len(a)):
        if mark[i] == 0:
            rem.append(a[i])

    rem.sort()
    rem.reverse()
    for i in rem:
        f.append(i)

    return get_num(f)


def main(n: int):
    """
    规模 n 用来生成测试数据：
    - a 为长度 n 的数字串，从 1 开始循环到 9，例如 n=12 -> '123456789123'
    - b 为长度 n 的数字串，全部为 '9'
    """
    if n <= 0:
        return

    digits = '123456789'
    a = ''.join(digits[i % len(digits)] for i in range(n))
    b = '9' * n

    ans = solve(a, b)
    print(ans)


if __name__ == "__main__":
    # 示例：可根据需要修改 n
    main(5)