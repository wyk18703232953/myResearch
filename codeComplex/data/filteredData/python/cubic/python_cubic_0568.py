import random

def main(n: int):
    # 生成测试数据：长度为 n 的数字串 s 和 s1
    # 使得 s1 的长度在 1..n 之间，且只包含 0..9
    s = "".join(str(random.randint(0, 9)) for _ in range(n))
    m = random.randint(1, n)
    s1 = "".join(str(random.randint(0, 9)) for _ in range(m))

    l = []
    l1 = []
    for x in s:
        l.append(int(x))
    for x in s1:
        l1.append(int(x))
    d = {}
    for x in l:
        d[x] = d.get(x, 0) + 1
    f = False
    if len(s1) > len(s):
        l = sorted(l)
        l = l[::-1]
        print("".join(map(str, l)))
        return

    ans = [0] * len(s)

    ki = 0
    i = 0
    while i < len(l1):
        f = True
        for j in range(max(l1[i], ki), -1, -1):
            if d.get(j, -1) > 0:
                ans[i] = j
                d[j] -= 1
                f = False
                if j != l1[i]:
                    ki = 9
                break

        if f:
            for i1 in range(i - 1, -1, -1):
                f1 = False
                for j in range(max(l1[i1], ki) - 1, -1, -1):
                    if d.get(j, -1) > 0:
                        d[ans[i1]] += 1
                        ans[i1] = j
                        d[j] -= 1
                        f1 = True
                        i = i1
                        ki = 9
                        break
                if f1:
                    break
                else:
                    d[ans[i1]] += 1
                    ans[i1] = 0
        i += 1

    print("".join(map(str, ans)))


if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数
    main(10)