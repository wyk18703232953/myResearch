from math import gcd

def t_prime(n):
    if n == 1:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        if p < n and pow(p, n - 1, n) != 1:
            return False
    return True

def main(n):
    # 映射：n 为数组长度，k 也从 n 派生（保证可扩展且确定性）
    if n <= 0:
        return

    # 预处理 primes 与 pset（与原逻辑保持一致）
    primes = [i for i in range(2, 10 ** 5) if t_prime(i)]
    pset = set(primes)

    # 构造确定性输入：
    # n: 数组长度
    # k: 选择上限，设为 min(n, max(1, n//2)) 保证规模合理且可变化
    k = min(n, max(1, n // 2))

    # l: 确定性整数数组，使用简单算术构造
    # 既有重复因子又有不同素因子，避免退化情况
    l = [(i + 2) * (i % 5 + 2) for i in range(n)]

    # 下面为原始逻辑，去掉所有 input / exit 相关交互，改为函数内局部执行
    if k == 1:
        print(0)
        return

    for i in range(n):
        for j in range(i):
            u, v = l[i], l[j]
            poss = gcd(u, v)
            poss2 = max(u, v) // poss
            smol = min(poss, poss2)
            if t_prime(smol) and smol not in pset:
                primes.append(smol)
                pset.add(smol)

    powers = set()
    count = 0
    outLs = []
    pgood = []
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
        print(0)
        return

    if order[-1][0] == 2 and k % 2 and count > k:
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
            print(0)
            return
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
        ret = out + other[: (k - 2 * need - 1)]
        assert len(ret) == k
        print(" ".join(map(str, ret)))
        return

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
                need -= len(lis) - 1
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
        print(" ".join(map(str, out)))
        return
    else:
        print(0)
        return

if __name__ == "__main__":
    # 示例：可根据需要调整 n 以做时间复杂度实验
    main(200)