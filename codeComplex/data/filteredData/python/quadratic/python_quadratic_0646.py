#!/usr/bin/python3

def main(n):
    # 生成确定性输入：长度为 n 的整数列表
    # 使用简单的算术构造，避免非常大的数
    a = [(i * 2 + 3) % (n + 5) + 1 for i in range(n)]
    a = list(set(a))
    n = len(a)

    cnt = 0
    for i in range(n):
        f = True
        for j in range(n):
            if i == j:
                continue
            if a[i] % a[j] == 0:
                f = False
        if f:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main(10)