from math import floor

CONST = 9

def solve(k):
    i = 0
    while k > CONST * (10 ** i) * (i + 1):
        k -= floor(CONST * (10 ** i)) * (i + 1)
        i += 1
    num_digits = i + 1
    num = floor((k - 1) / num_digits)
    num += floor(10 ** i)
    # print(('{}'.format(num))[(k - 1) % num_digits])
    pass

def main(n):
    # 生成 n 个查询，第 i 个为 (i+1)*n，保证随 n 线性放大
    for i in range(1, n + 1):
        k = i * n
        solve(k)

if __name__ == "__main__":
    main(10)