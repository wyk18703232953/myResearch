import math

P = [2, 3, 5, 7, 11, 13, 17, 19]

def ya(x):
    xr = math.ceil(math.sqrt(x))
    LIST = []
    for i in range(1, xr + 1):
        if x % i == 0:
            LIST.append(i)
            LIST.append(x // i)
    return LIST

def run_algorithm(A):
    n = len(A)
    m = len(A[0]) if n > 0 else 0

    SET = set()
    for a in A:
        SET |= set(a)

    compression_dict = {a: ind for ind, a in enumerate(sorted(SET))}

    for i in range(n):
        A[i] = [compression_dict[a] for a in A[i]]

    OK = 0
    NG = len(compression_dict)
    ANS = [1, 1]
    B = [set()] * n

    Q = 1
    for j in range(m):
        Q *= P[j]

    while NG > OK + 1:
        mid = (OK + NG) // 2
        SET = set()

        for i in range(n):
            NOW = 1
            for j in range(m):
                if A[i][j] >= mid:
                    NOW *= P[j]
            B[i] = NOW
            SET.add(NOW)

        flag = 0

        for s in SET:
            for l in ya(s):
                if Q // l in SET:
                    flag = 1
                    OK = mid
                    break
            if flag:
                break
        else:
            NG = mid

    SET = set()
    for i in range(n):
        NOW = 1
        for j in range(m):
            if A[i][j] >= OK:
                NOW *= P[j]
        B[i] = NOW
        SET.add(NOW)

    flag = 0
    ANS1 = 0
    for i in range(n):
        for l in ya(B[i]):
            if Q // l in SET:
                ANS1 = i
                flag = 1
                break
        if flag:
            break

    LIST = ya(B[ANS1])
    SET = set(LIST)

    ANS2 = 0
    for i in range(n):
        if Q // B[i] in SET:
            ANS2 = i

    return ANS1 + 1, ANS2 + 1

def generate_data(n):
    if n <= 0:
        n = 1
    max_m = min(8, n)
    m = max_m if max_m > 0 else 1
    rows = n

    A = []
    for i in range(rows):
        row = [((i + 1) * (j + 1)) % (n + 3) for j in range(m)]
        A.append(row)
    return A

def main(n):
    A = generate_data(n)
    ans1, ans2 = run_algorithm(A)
    print(ans1, ans2)

if __name__ == "__main__":
    main(10)