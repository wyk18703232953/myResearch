import random

def main(n: int):
    # 生成测试数据：1..n 的一个随机排列
    L = list(range(1, n + 1))
    random.shuffle(L)

    ans = [''] * n
    revL = [0] * n
    ans[-1] = 'B'

    for i in range(n):
        revL[L[i] - 1] = i + 1

    for i in range(n - 2, -1, -1):
        t = revL[i] - 1
        counter = 'B'
        for j in range(t, -1, -i - 1):
            if j == t:
                continue
            if ans[L[j] - 1] == 'B':
                counter = 'A'
                break
        if counter != 'A':
            for k in range(t, n, i + 1):
                if k == t:
                    continue
                if ans[L[k] - 1] == 'B':
                    counter = 'A'
                    break
        ans[i] = counter

    for i in range(n):
        print(ans[L[i] - 1], sep='', end='')


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)