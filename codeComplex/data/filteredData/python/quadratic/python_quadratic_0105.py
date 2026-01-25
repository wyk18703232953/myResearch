def check(x, y):
    return ''.join([''.join(s) for s in x]) == ''.join([''.join(s) for s in y])

def generate_matrix_a(n):
    # Deterministically generate matrix a with characters based on indices
    return [[chr(ord('a') + (i + j) % 3) for j in range(n)] for i in range(n)]

def generate_matrix_b(n):
    # Deterministically generate matrix b with a different pattern
    return [[chr(ord('a') + (i * 2 + j) % 3) for j in range(n)] for i in range(n)]

def main(n):
    a = generate_matrix_a(n)
    b = generate_matrix_b(n)

    for _ in range(4):
        for _ in range(2):
            if check(a, b):
                print('Yes')
                return
            b = b[::-1]
        for _ in range(2):
            if check(a, b):
                print('Yes')
                return
            b = [row[::-1] for row in b]
        c = [['' for _ in range(n)] for _ in range(n)]
        for t in range(n):
            for u in range(n):
                c[t][u] = b[u][n - t - 1]
        b = c[:]
        if check(a, b):
            print('Yes')
            return
    print('No')

if __name__ == "__main__":
    main(5)