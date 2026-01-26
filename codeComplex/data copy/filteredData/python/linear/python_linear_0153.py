def main(n):
    # 映射：n 为数组长度，p 为 n 的下一个质数（确定性构造）
    if n <= 0:
        # print(0)
        pass
        return

    def next_prime(x):
        def is_prime(k):
            if k < 2:
                return False
            if k == 2:
                return True
            if k % 2 == 0:
                return False
            i = 3
            while i * i <= k:
                if k % i == 0:
                    return False
                i += 2
            return True

        if x <= 2:
            return 2
        p = x if x % 2 == 1 else x + 1
        while not is_prime(p):
            p += 2
        return p

    p = next_prime(n)

    # 确定性数组构造：arr[i] = (i * 2 + 3) % p + 1
    arr = [((i * 2 + 3) % p) + 1 for i in range(n)]

    su = 0
    for i in range(n):
        su += arr[i]

    maxi, f = 0, 0
    for i in range(n - 1):
        f += arr[i]
        maxi = max(maxi, f % p + (su - f) % p)

    # print(maxi)
    pass
if __name__ == "__main__":
    # 示例：可根据需要修改 n 的大小进行复杂度实验
    main(10)