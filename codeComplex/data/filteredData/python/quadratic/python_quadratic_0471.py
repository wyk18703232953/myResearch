import random

def qwe(s, j):
    l, r = 0, 0
    for i in range(len(s)):
        if i < j and s[i] > s[j]:
            l += 1
        elif i > j and s[i] > s[j]:
            r += 1
    return l, r

def generate_valid_data(n):
    # 生成一个随机的排列 s[0..n-1]
    s = list(range(1, n + 1))
    random.shuffle(s)

    a = [0] * n
    b = [0] * n

    # 根据原逻辑，从 s 推出 a, b
    for i in range(n):
        l, r = qwe(s, i)
        a[i] = l
        b[i] = r

    return a, b

def main(n):
    # 1. 生成测试数据 a, b
    a, b = generate_valid_data(n)

    # 2. 以下是原逻辑（去掉 input 部分）
    s = [0] * n
    ans = True

    for i in range(n):
        ans = ans and a[i] <= i and b[i] <= (n - i - 1)
        s[i] = n - a[i] - b[i]

    if ans:
        for i in range(n):
            l, r = qwe(s, i)
            ans = ans and (a[i] == l and b[i] == r)

    if ans:
        print('YES')
        for i in range(n):
            print(n - a[i] - b[i], end=' ')
        print()
    else:
        print('NO')

if __name__ == "__main__":
    # 示例：运行 main(5)
    main(5)