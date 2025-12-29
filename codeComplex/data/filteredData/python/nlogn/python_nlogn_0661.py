import random

MOD = 998244353

def I(J):
    if len(J) <= 1:
        return J, 0
    else:
        a = J[:len(J) // 2]
        b = J[len(J) // 2:]
        a, ai = I(a)
        b, bi = I(b)
        c = []
        i = 0
        j = 0
        inversions = ai + bi
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
                inversions += (len(a) - i)
        c += a[i:]
        c += b[j:]
        return c, inversions


def main(n):
    # 生成测试数据 L，长度为 n，元素可以为正数或 -1
    # 规则示例：随机在 1..n 中选一些位置放正数，其余为 -1
    L = [-1] * n
    values = list(range(1, n + 1))
    random.shuffle(values)
    # 至少放一个正数，至多放 n 个
    k = random.randint(1, n)
    positions = random.sample(range(n), k)
    for pos, val in zip(positions, values[:k]):
        L[pos] = val

    D = {}
    J = []
    S = []
    T = [0] * (n + 1)

    for i in range(n):
        if L[i] > 0:
            D[L[i]] = i
            J.append(L[i])
            T[i + 1] = T[i]
        else:
            T[i + 1] = T[i] + 1

    for i in range(1, n + 1):
        if i not in D:
            S.append(i)

    total = len(S)
    num = 1
    denom = 1
    if total > 0:
        themostimportantsum = 0
        for i in J:
            low = 0
            high = total - 1
            while high - low > 1:
                guess = (high + low) // 2
                if S[guess] > i:
                    high = guess
                else:
                    low = guess
            if S[low] > i:
                smaller = low
            elif S[high] > i:
                smaller = high
            else:
                smaller = high + 1
            themostimportantsum += T[D[i]] * (total - smaller) + (total - T[D[i]]) * (smaller)
            num = themostimportantsum + total
            denom = total

    num = (denom * (((total) * (total - 1)) // 2) + 2 * num) % MOD
    denom *= 2

    if num == denom:
        inv_cnt = I(J)[1]
        if inv_cnt == 0:
            print(0)
        else:
            print(inv_cnt % MOD)
    else:
        inv_cnt = I(J)[1]
        num += denom * inv_cnt
        print(((num - denom) * pow(denom % MOD, MOD - 2, MOD)) % MOD)


if __name__ == "__main__":
    # 示例：运行规模为 5 的测试
    main(5)