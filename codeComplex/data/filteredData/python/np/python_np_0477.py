from math import gcd
import random

def t_prime(n):
    if n == 1:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        if p < n and pow(p, n - 1, n) != 1:
            return False
    return True


def solve(n, k, l):
    primes = [i for i in range(2, 10 ** 5) if t_prime(i)]
    pset = set(primes)

    if k == 1:
        return []

    # augment primes using gcds of pairs
    for i in range(n):
        for j in range(i):
            u, v = l[i], l[j]
            poss = gcd(u, v)
            if poss == 0:
                continue
            poss2 = max(u, v) // poss
            smol = min(poss, poss2)
            if smol > 1 and t_prime(smol) and smol not in pset:
                primes.append(smol)
                pset.add(smol)

    powers = set()
    count = 0
    outLs = []
    pgood = []

    # collect full powers of primes in list
    for p in primes:
        curr = []
        fp = [v for v in l if v % p == 0]
        for v in fp:
            v2 = v
            while v2 % p == 0:
                v2 //= p
            if v2 == 1:
                curr.append(v)
                powers.add(v)
        if len(curr) > 1:
            count += len(curr)
            outLs.append(curr)
            pgood.append(p)

    order = [(len(lis), lis) for lis in outLs]
    order.sort(key=lambda x: x[0])

    if len(order) == 0:
        return []

    if order[-1][0] == 2 and (k % 2 == 1) and count > k:
        extra = -1
        need = -1
        last = []
        for v in l:
            if v in powers:
                continue
            v2 = v
            primesn = []
            for p in pgood:
                add = 1
                while v2 % p == 0:
                    v2 //= p
                    if add:
                        primesn.append(p)
                    add = 0
            if v2 == 1 and (need == -1 or need > len(primesn)):
                extra = v
                last = primesn
                need = len(last)
                assert need >= 2

        if need == -1 or 2 * need + 1 > k:
            return []

        other = []
        out = [extra]
        for lis in outLs:
            works = False
            for p in last:
                if lis[0] % p == 0:
                    works = True
                    break
            if works:
                out.append(lis[0])
                out.append(lis[1])
            else:
                other.append(lis[0])
                other.append(lis[1])

        assert len(out) == 2 * need + 1
        assert (k - 2 * need - 1) % 2 == 0
        ret = out + other[:(k - 2 * need - 1)]
        assert len(ret) == k
        return ret

    out = []
    need = k

    for i in range(len(order)):
        assert need != 1
        lis = order[i][1]
        if len(lis) < need - 1 or len(lis) == need or (len(lis) == need - 1 and i == len(order) - 1):
            out += lis
            need -= len(lis)
        elif len(lis) == need - 1:
            if len(lis) > 2:
                out += lis[:-1]
                need -= (len(lis) - 1)
                assert need == 2
        else:
            out += lis[:need]
            need = 0

    assert need + len(out) == k
    assert need >= 0
    assert need == 0 or len(out) == count

    for v in l:
        if need == 0:
            break
        if v in powers:
            continue
        v2 = v
        for p in pgood:
            while v2 % p == 0:
                v2 //= p
        if v2 == 1:
            out.append(v)
            need -= 1

    if need == 0:
        return out
    else:
        return []


def main(n):
    # 生成测试数据：
    # n: 数组长度
    # k: 选择数量，设为不大于 n 且与 n 有一定关系
    if n <= 0:
        return []

    # 让 k 在 [1, n] 之间，偏向中等规模
    k = max(1, min(n, n // 2 + 1))

    # 生成数组 l：使用 2..10^5 范围内的随机数，偏向有因子结构
    l = []
    for _ in range(n):
        if random.random() < 0.6:
            # 生成带小质因数的数
            base = random.randint(2, 200)
            exp = random.randint(1, 5)
            val = base ** exp
            # 控制上界
            if val > 10 ** 9:
                val = base
            l.append(val)
        else:
            l.append(random.randint(2, 10 ** 9))

    ans = solve(n, k, l)
    if ans:
        print(' '.join(map(str, ans)))
    else:
        print(0)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可根据需要修改
    main(10)