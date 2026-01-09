import sys

keta = 29

def judge(x, y, A, B):
    if A == B:
        return 0
    if x >= A or y >= B:
        return -1
    return 1

def simulate_interactive(A, B):
    queries = []

    def ask(x, y):
        queries.append(("?", x, y))
        return judge(x, y, A, B)

    # Simulate original logic, but instead of printing '?' and reading input,
    # we call ask() and get deterministic responses from (A,B)
    A00 = ask(0, 0)

    if A00 == 0:
        ANS = 0
        for k in range(keta, -1, -1):
            res = ask(2 ** k, 0)
            if res == -1:
                ANS += 2 ** k
        # Final result in this branch is (ANS, ANS)
        return ANS, ANS, queries

    a = 0
    b = 0
    for k in range(keta, -1, -1):
        lst = []
        lst.append(ask(2 ** k + a, b))
        lst.append(ask(a, 2 ** k + b))

        if lst[0] != lst[1]:
            if lst[0] == -1:
                a += 2 ** k
                b += 2 ** k

        else:
            if A00 == 1:
                a += 2 ** k

            else:
                b += 2 ** k
            A00 = lst[0]

    return a, b, queries

def main(n):
    # Deterministically choose hidden A,B from n
    # Scale them so they fit within 2^keta
    max_val = (1 << keta) - 1
    if n <= 0:
        A = 0
        B = 0

    else:
        A = (n * 1234567) % (max_val + 1)
        B = (n * 7654321) % (max_val + 1)

    A_ans, B_ans, _ = simulate_interactive(A, B)
    # print(A_ans, B_ans)
    pass
if __name__ == "__main__":
    # Example deterministic call; change 10 to other n for different scales
    main(10)