from collections import defaultdict, Counter
from bisect import bisect, bisect_left
from math import sqrt, gcd

def main(n):
    # Deterministically generate the input array of size n
    # Pattern: arr[i] = i // 2 to create some duplicates
    arr_input = [i // 2 for i in range(n)]
    arr = Counter(arr_input)

    ans_ = []

    t_p = [2**i for i in range(31)]
    d = defaultdict(int)
    # Handle case when arr is empty (n == 0)
    if arr:
        m = 1
        ans_lis = [list(arr.keys())[0]]

    else:
        m = 0
        ans_lis = []

    for i in arr:
        for j in t_p:
            a, b, c = i, i + j, i + 2 * j
            s = (arr[a] > 0) + (arr[b] > 0) + (arr[c] > 0)
            if s > m:
                m = s
                ans_lis = [x for x in [a, b, c] if arr[x]]

    ans_.append(m)
    t = ""
    for i in ans_lis:
        t += str(i) + " "
    ans_.append(t)

    for i in ans_:
        # print(i)
        pass
if __name__ == "__main__":
    # Example call with a chosen input size
    main(1000)