import random
import string

def rotate(i, j, n):
    return j, n - 1 - i

def flip(i, j, n):
    return j, i

def main(n):
    # 生成两个 n x n 的随机字符矩阵
    chars = string.ascii_letters + string.digits
    ns = [''.join(random.choice(chars) for _ in range(n)) for _ in range(n)]
    ns2 = [''.join(random.choice(chars) for _ in range(n)) for _ in range(n)]

    same = True
    # 原位置比较
    for i in range(n):  # 0
        for j in range(n):
            if ns[i][j] != ns2[i][j]:
                same = False
                break
        if not same:
            break
    if same:
        return True

    same = True
    # 旋转 90°
    for i in range(n):  # 1
        for j in range(n):
            a, b = rotate(i, j, n)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if not same:
            break
    if same:
        return True

    same = True
    # 旋转 180°
    for i in range(n):  # 2
        for j in range(n):
            a, b = rotate(i, j, n)
            a, b = rotate(a, b, n)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if not same:
            break
    if same:
        return True

    same = True
    # 旋转 270°
    for i in range(n):
        for j in range(n):  # 3
            a, b = rotate(i, j, n)
            a, b = rotate(a, b, n)
            a, b = rotate(a, b, n)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if not same:
            break
    if same:
        return True

    same = True
    # 水平翻转
    for i in range(n):  # 0
        for j in range(n):
            a, b = flip(i, j, n)
            if ns[a][b] != ns2[i][j]:
                same = False
                break
        if not same:
            break
    if same:
        return True

    same = True
    # 翻转后再旋转 90°
    for i in range(n):  # 1
        for j in range(n):
            a, b = rotate(i, j, n)
            a, b = flip(a, b, n)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if not same:
            break
    if same:
        return True

    same = True
    # 翻转后再旋转 180°
    for i in range(n):  # 2
        for j in range(n):
            a, b = rotate(i, j, n)
            a, b = rotate(a, b, n)
            a, b = flip(a, b, n)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if not same:
            break
    if same:
        return True

    same = True
    # 翻转后再旋转 270°
    for i in range(n):
        for j in range(n):  # 3
            a, b = rotate(i, j, n)
            a, b = rotate(a, b, n)
            a, b = rotate(a, b, n)
            a, b = flip(a, b, n)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if not same:
            break
    if same:
        return True
    else:
        return False

if __name__ == "__main__":
    # 示例：调用 main(5)
    if main(5):
        print("Yes")
    else:
        print("No")