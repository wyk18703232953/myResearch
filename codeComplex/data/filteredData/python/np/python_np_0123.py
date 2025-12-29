import random

def main(n: int):
    # 生成规模为 n 的测试数据：随机整数序列 a[0..n-1]
    # 可以根据需要修改数据范围
    a = [random.randint(0, 10**9) for _ in range(n)]

    b = []
    bb = []
    for i in range(n):
        x = a[i]
        idx = 0
        for j in range(len(b)):
            nxt = b[j] ^ x
            if nxt < x:
                x = nxt
                idx ^= bb[j]
        if x == 0:
            cnt = 0
            v = []
            for k in range(2000):
                if idx & (1 << k):
                    v.append(k)
            print(len(v), end=' ')
            for e in v:
                print(e, end=' ')
            print()
        else:
            print(0)
            idx ^= 1 << i
            b.append(x)
            bb.append(idx)


if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改
    main(5)