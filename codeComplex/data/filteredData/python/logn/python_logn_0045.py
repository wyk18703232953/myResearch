MOD = 10**9 + 7

def solve(l, r):
    if l == r:
        return 0
    a = list(format(l, '064b'))
    b = list(format(r, '064b'))
    i = 0
    ll = l
    rr = r
    while i < 64 and a[i] == b[i]:
        i += 1
    for j in range(i, 64):
        bit_val = 1 << (63 - j)
        if a[j] == '0' and b[j] == '0':
            k = l ^ bit_val
            if k <= rr:
                l = k
                a[j] = '1'
        elif a[j] == '1' and b[j] == '1':
            k = r - bit_val
            if k >= ll:
                r = k
                b[j] = '0'
    return l ^ r

def main(n: int):
    # 根据规模 n 生成测试数据：
    # 生成 l, r，使得 0 <= l <= r < 2^n（n 不超过 60 时较安全）
    if n <= 0:
        l, r = 0, 0
    else:
        # 控制 n 防止移位过大
        m = min(n, 60)
        # 简单构造：l 是前 m 位的一半，r 是前 m 位全 1
        l = (1 << (m - 1)) if m >= 1 else 0
        r = (1 << m) - 1
    ans = solve(l, r)
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main，规模设为 10，可按需修改
    main(10)