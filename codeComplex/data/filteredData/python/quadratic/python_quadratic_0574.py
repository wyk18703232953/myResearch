import sys

def countR(ip):
    c = 0
    for i in ip:
        if i == 'R':
            c += 1
    return c

def countB(ip):
    c = 0
    for i in ip:
        if i == 'B':
            c += 1
    return c

def countG(ip):
    c = 0
    for i in ip:
        if i == 'G':
            c += 1
    return c

def run_single_case(n, k, a):
    x = 'RGB' * 680
    y = 'GBR' * 680
    z = 'BRG' * 680
    xk = x[:k]
    yk = y[:k]
    zk = z[:k]
    op = 2001
    for j in range(n - k + 1):
        b = a[j:j + k]
        xd = 0
        yd = 0
        zd = 0
        for jj in range(len(b)):
            if b[jj] != xk[jj]:
                xd += 1
            if b[jj] != yk[jj]:
                yd += 1
            if b[jj] != zk[jj]:
                zd += 1
        op = min(op, xd, yd, zd)
    return op

def main(n):
    # n controls both number of test cases and the scale of each case
    t = n
    results = []
    for case_id in range(t):
        # Deterministic generation of n_case and k
        n_case = max(1, case_id + 2)  # lengths: 2,3,4,... for variety
        max_k = min(2000, n_case)
        k = max(1, (case_id * 3) % max_k + 1)
        if k > n_case:
            k = n_case

        # Deterministic generation of string a of length n_case
        # Pattern cycles over 'R', 'G', 'B' based on index and case_id
        chars = ['R', 'G', 'B']
        a = ''.join(chars[(i + case_id) % 3] for i in range(n_case))

        op = run_single_case(n_case, k, a)
        results.append(op)

    # Output results to keep behavior similar to original program
    for val in results:
        # print(val)
        pass
if __name__ == "__main__":
    main(5)