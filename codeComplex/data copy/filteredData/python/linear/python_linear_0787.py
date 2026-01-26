from collections import Counter


def check(A):
    CA = Counter(A)
    if CA[0] >= 2:
        return False
    cnt = 0
    for k, v in CA.items():
        if v > 2:
            return False
        if v == 2 and CA[k - 1] >= 1:
            return False
        if v >= 2:
            cnt += 1
    if cnt >= 2:
        return False
    L = len(A)
    if (sum(A) - L * (L - 1) // 2) % 2 == 0:
        return False
    return True


def main(n):
    if n <= 0:
        A = []

    else:
        # Deterministic construction: non-decreasing sequence with some duplicates
        # A[i] = i // 2 ensures sorted order and controlled multiplicities
        A = [i // 2 for i in range(n)]
    if check(A):
        # print('sjfnb')
        pass

    else:
        # print('cslnb')
        pass
if __name__ == "__main__":
    main(10)