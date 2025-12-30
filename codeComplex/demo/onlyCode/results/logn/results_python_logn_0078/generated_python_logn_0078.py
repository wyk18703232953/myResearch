import random

def main(n: int):
    # 生成测试数据：根据规模 n 生成 l, r
    # 这里让 l, r 落在 [0, 2^n - 1] 范围内
    if n <= 0:
        l = r = 0
    else:
        max_val = (1 << n) - 1
        l = random.randint(0, max_val)
        r = random.randint(0, max_val)
        if l > r:
            l, r = r, l

    # 原逻辑开始
    n1 = bin(l)[2:]
    n2 = bin(r)[2:]
    if l == r:
        ans = 0
    elif len(n1) < len(n2):
        ans = int(len(n2) * '1', 2)
    else:
        index = 0
        for i in range(len(n1)):
            if n1[i] != n2[i]:
                index = i
                break
        ans = int((len(n1) - index) * '1', 2)

    print(ans)

if __name__ == "__main__":
    # 示例：可根据需要修改 n
    main(5)