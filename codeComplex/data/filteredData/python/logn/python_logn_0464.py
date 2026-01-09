import sys

keta = 29

def simulate_query(x, y, A, B):
    # Determine the sign of (A xor x) - (B xor y)
    v1 = A ^ x
    v2 = B ^ y
    if v1 > v2:
        return 1
    elif v1 < v2:
        return -1

    else:
        return 0

def main(n):
    # Map n to bit length (bounded by keta)
    K = min(n, keta + 1)
    # Deterministically construct hidden A and B using first K bits
    A = 0
    B = 0
    for k in range(K):
        if k % 2 == 0:
            A |= (1 << k)

        else:
            B |= (1 << k)

    # Start of original logic, with queries simulated
    keta_local = keta
    A00 = simulate_query(0, 0, A, B)

    if A00 == 0:
        ANS = 0
        for k in range(keta_local, -1, -1):
            res = simulate_query(2**k, 0, A, B)
            if res == -1:
                ANS += 2**k
        # In the interactive problem this would print "! ANS ANS"
        # For experiment we just return the result
        return ANS, ANS

    A_ans = 0
    B_ans = 0
    for k in range(keta_local, -1, -1):
        LIST = []
        res1 = simulate_query(2**k + A_ans, B_ans, A, B)
        LIST.append(res1)
        res2 = simulate_query(A_ans, 2**k + B_ans, A, B)
        LIST.append(res2)

        if LIST[0] != LIST[1]:
            if LIST[0] == -1:
                A_ans += 2**k
                B_ans += 2**k

        else:
            if A00 == 1:
                A_ans += 2**k

            else:
                B_ans += 2**k
            A00 = LIST[0]

    return A_ans, B_ans

if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    result = main(30)
    # print(result)
    pass