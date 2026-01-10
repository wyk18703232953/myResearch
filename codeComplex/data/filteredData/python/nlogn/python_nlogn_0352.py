from collections import defaultdict, Counter
from bisect import bisect, bisect_left
from math import sqrt, gcd

def main(n):
    ans_ = []

    t_p = [2**i for i in range(31)]

    # Deterministically generate array of size n
    # Example pattern: arr[i] = i % 50
    base_arr = [i % 50 for i in range(n)]
    arr = Counter(base_arr)

    d = defaultdict(int)
    # Initialize m and ans_lis similar to original logic
    keys_list = list(arr.keys())
    if not keys_list:
        m = 0
        ans_lis = []
    else:
        m = 1
        ans_lis = [[keys_list[0], 1]]

    for i in arr:
        for j in t_p:
            a, b, c = i, i + j, i + 2 * j
            s = arr[a] + arr[b] + arr[c]
            if s > m:
                m = s
                ans_lis = [[x, arr[x]] for x in [a, b, c]]

    ans_.append(m)
    t = ""
    for i in ans_lis:
        t += (str(i[0]) + " ") * i[1]
    ans_.append(t)

    for i in ans_:
        print(i)


if __name__ == "__main__":
    main(10)