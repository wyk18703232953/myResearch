import math

def generate_params(n):
    # 保证 n 至少为 2，避免无意义规模
    if n < 2:
        n = 2
    # 生成 (n, a, b)
    # 让 a, b 在 1~3 之间变化，并且依赖 n，保证确定性
    a = 1 + (n % 3)
    b = 1 + ((n // 2) % 3)
    return n, a, b

def main(n):
    n, a, b = generate_params(n)
    if a > 1 and b > 1:
        print('NO')
    elif a == 1 and b == 1 and (n == 2 or n == 3):
        print('NO')
    else:
        c = max(a, b)
        m = [[0] * n for _ in range(n)]
        for i in range(n - c):
            m[i][i + 1] = 1
            m[i + 1][i] = 1
        if b > 1:
            for i in range(n):
                for j in range(n):
                    if i != j:
                        m[i][j] = 1 - m[i][j]
        print('YES')
        for i in range(n):
            print(''.join(map(str, m[i])))

if __name__ == "__main__":
    # 示例：使用 n = 10 作为规模
    main(10)