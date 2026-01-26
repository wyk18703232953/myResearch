import math

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
    if n <= 0:
        # print("")
        pass
        return

    # 确定性生成 a, b 的十进制字符串
    # 保证都有 n 位，且不会以 0 开头
    digits_a = [(i * 7 + 3) % 10 for i in range(n)]
    digits_b = [(i * 9 + 4) % 10 for i in range(n)]

    # 避免前导零
    if digits_a[0] == 0:
        digits_a[0] = 1
    if digits_b[0] == 0:
        digits_b[0] = 1

    e1 = "".join(str(d) for d in digits_a)
    e2 = "".join(str(d) for d in digits_b)

    a = int(e1)
    b = int(e2)

    l1 = [int(ch) for ch in str(a)]
    l2 = [int(ch) for ch in str(b)]

    if len(l1) < len(l2):
        l1.sort(reverse=True)
        o = [str(i) for i in l1]
        # print("".join(o))
        pass

    else:
        n2 = len(l2)
        ans = rec(0, n2, l1, l2)
        w = [str(i) for i in ans]
        # print("".join(w))
        pass
if __name__ == "__main__":
    main(10)