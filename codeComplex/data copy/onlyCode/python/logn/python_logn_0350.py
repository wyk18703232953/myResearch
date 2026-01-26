def main():
    x, k = list(map(int, input().split()))
    if x == 0:
        print(0)
        return 0
    def helper(n):
        if n == 0:
            return 1
        p = 1
        ret = 2
        while n >= 2 * p:
            p *= 2
            ret = (ret ** 2) % 1000000007
        return ret * helper(n - p)
    x = x % 1000000007
    k = k % 1000000006
    a = helper(k)
    print((2 * a * x - a + 1) % 1000000007)
    return 0
main()
