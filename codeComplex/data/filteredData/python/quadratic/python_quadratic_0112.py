import random
import string

def h(d, n):
    c = []
    for i in range(n):
        c.append(d[n - i - 1])
    return c

def r(d, n):
    c = []
    for i in range(n):
        temp = ""
        for j in range(n):
            temp += d[j][n - i - 1]
        c.append(temp)
    return c

def generate_test_data(n):
    # 生成一个 n×n 的随机矩阵，由 '.' 和 '#' 组成
    chars = ".#"
    a = []
    for _ in range(n):
        row = "".join(random.choice(chars) for _ in range(n))
        a.append(row)

    # 随机选择一种变换方式生成 b
    # 0: 不变
    # 1: 0~3 次旋转
    # 2: 水平翻转 + 0~3 次旋转
    # 3: 完全随机(大概率 NO)
    mode = random.randint(0, 3)

    b = [row[:] for row in a]

    if mode == 1:
        k = random.randint(0, 3)
        for _ in range(k):
            b = r(b, n)
    elif mode == 2:
        b = h(b, n)
        k = random.randint(0, 3)
        for _ in range(k):
            b = r(b, n)
    elif mode == 3:
        # 完全随机生成另一个矩阵
        b = []
        for _ in range(n):
            row = "".join(random.choice(chars) for _ in range(n))
            b.append(row)

    return a, b

def main(n):
    a, b = generate_test_data(n)

    yes = 0
    tmp_a = a[:]  # 避免修改原始 a，便于调试时打印
    for _ in range(4):
        if tmp_a == b:
            print('YES')
            yes = 1
            break
        tmp_a = r(tmp_a, n)
    if yes == 0:
        tmp_a = h(a, n)
        for _ in range(4):
            if tmp_a == b:
                print('YES')
                yes = 1
                break
            tmp_a = r(tmp_a, n)
    if yes == 0:
        print('NO')

if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)