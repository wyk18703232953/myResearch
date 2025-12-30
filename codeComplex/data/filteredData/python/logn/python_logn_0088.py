from math import ceil, sqrt, log
import random

def mod_expo(n, p, m):
    """find (n^p)%m"""
    result = 1
    while p != 0:
        if p % 2 == 1:
            result = (result * n) % m
        p //= 2
        n = (n * n) % m
    return result

def is_square(n):
    return int(sqrt(n)) * int(sqrt(n)) == n

def find_div(n):
    d = []
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            if i * i != n:
                d.append(i)
                d.append(n // i)
            else:
                d.append(i)
    return d

def find_x(n):
    d = find_div(2 * n)
    for div in d:
        x2 = div * (div + 2 * n)
        if is_square(x2):
            return sqrt(x2)
    return -1

def find_base_side(n):
    squares = [x * x for x in range(ceil(sqrt(n)))]
    for i in range(len(squares)):
        for j in range(len(squares)):
            if squares[i] + squares[j] == n * n:
                return squares[i]
    return -1

def str_add(n):
    n = list(n)
    for i in range(1, len(n) + 1):
        if n[-i] == '9':
            n[-i] = '0'
        else:
            n[-i] = int(int(n[-i]) + 1)
            break
    n = str(n)
    return n

def str_sub(n):
    n = list(n)
    for i in range(1, len(n) + 1):
        if n[-i] == '0':
            n[-i] = '9'
        else:
            n[-i] = int(int(n[-i]) - 1)
            break
    n = str(n)
    return n

def find_massive_x(n):
    if n % 2 == 0:
        n2 = str(int(pow(n / 2, 2)))
        x = str_sub(n2)
        y = str_add(n2)
    else:
        n2 = str(int(pow(n, 2) / 2))
        x = str_sub(n2)
        y = str_add(n2)
    x = str(x)
    y = str(y)
    print(x, y)

def find_triples(n):
    if n <= 2:
        print(-1)
        return
    else:
        find_massive_x(n)
    print(-1)

def find_max_xor(l, r):
    lxr = l ^ r
    msb_pos = 0
    while lxr > 0:
        msb_pos += 1
        lxr //= 2
    return pow(2, msb_pos) - 1

def main(n):
    """
    n 用作规模参数。
    这里根据 n 生成测试数据：
      - 生成 t = n 组测试
      - 对每组生成 0 <= l <= r <= 2*n 的随机区间
      - 对每组打印 find_max_xor(l, r) 的结果
    """
    t = n
    for _ in range(t):
        l = random.randint(0, max(0, 2 * n))
        r = random.randint(l, max(l, 2 * n))
        print(find_max_xor(l, r))

if __name__ == "__main__":
    # 示例：使用 n=5 作为规模
    main(5)