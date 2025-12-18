# python3

def readline(): return map(int, input().split())


def main():
    n, a, b = readline()
    if a > 1 and b > 1:
        print('NO')
        return

    if n in [2, 3] and a == 1 and b == 1:
        print('NO')
        return
    
    matrix = [[i in [j + 1, j -1] for i in range(n)] for j in range(n)]

    a, b = n + 1 - a, n + 1 - b
    if a != n:
        matrix = [[False for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                if i < a and j < a and i != j:
                    matrix[i][j] = True
    elif b != n:
        matrix = [[False for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                if i >= b or j >= b:
                    matrix[i][j] = True
                if i == j:
                    matrix[i][j] = False

    print('YES')
    for row in matrix:
        print("".join(map(lambda x: '1' if x else '0', row)), flush=False)

if __name__ == '__main__':
    main()
