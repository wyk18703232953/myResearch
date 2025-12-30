import random

def Sort(x):
    if len(x) == 1:
        return x

    mid = len(x) // 2
    a = Sort(x[:mid])
    b = Sort(x[mid:])

    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c = c + b[j:]
    c = c + a[i:]

    return c

def main(n):
    # 生成规模为 n 的测试数据，这里生成 0~999 之间的随机整数
    m = [random.randint(0, 999) for _ in range(n)]

    newm = Sort(m)
    count = 0
    for i in range(len(m)):
        if newm[i] != m[i]:
            count += 1

    if count / 2 <= 1:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    # 示例：运行 main(10)
    main(10)