import random

def main(n):
    # 生成测试数据：根据规模 n 生成区间 [l, r]
    # 这里选择让 r 在 [0, 2^n - 1] 内，且 l <= r
    if n <= 0:
        return 0

    max_val = (1 << n) - 1
    r_num = random.randint(0, max_val)
    l_num = random.randint(0, r_num)

    l = bin(l_num)[2:]
    r = bin(r_num)[2:]

    r = r[::-1]
    l = l[::-1]

    if l == r:
        result = 0
    else:
        l += '0' * (len(r) - len(l))
        p = -1
        for i in range(len(r)):
            if r[i] != l[i]:
                p = i

        a = '1' * p + '0'
        b = '0' * p + '1'

        result = int(a, 2) ^ int(b, 2)

    print(result)
    return result

if __name__ == "__main__":
    # 示例：调用 main，规模 n 自行设定
    main(10)