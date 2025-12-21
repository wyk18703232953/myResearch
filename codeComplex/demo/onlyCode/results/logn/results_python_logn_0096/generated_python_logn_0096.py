def max_xor_naive(l, r):
    max_xor = 0
    xor = 0
    for a in range(l, r + 1):
        for b in range(a + 1, r + 1):
            xor = a ^ b
            if xor > max_xor:
                max_xor = xor
    return max_xor

def max_xor_efficient(l, r):
    s1 = bin(l)[2:]
    s2 = bin(r)[2:]
    l1 = len(s1)
    l2 = len(s2)
    if l1 < l2:
        return pow(2, l2) - 1
    for i in range(0, l1):
        if s1[i] != s2[i]:
            return pow(2, l1 - i) - 1
    return 0

def main(n):
    l = 1
    r = n
    ans2 = max_xor_efficient(l, r)
    print(ans2)
    return ans2

if __name__ == "__main__":
    main(10)