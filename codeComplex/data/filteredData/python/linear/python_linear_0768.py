import math

def main(n):
    # Map n to original n and q
    # Let original n = n, q = n for scalability
    orig_n = max(2, n)
    q = orig_n

    # Deterministic construction of arr of length orig_n
    # Example: strictly increasing then wrap by a modulus
    arr = [(i * 3 + 1) % (2 * orig_n + 1) for i in range(orig_n)]
    # Ensure not all equal
    if len(set(arr)) == 1:
        arr[0] += 1

    # Core logic from original program
    for i in range(orig_n):
        arr.append(0)
    ind = arr.index(max(arr[:orig_n]))
    ans = []
    ptr1 = 0
    ptr2 = orig_n
    for _ in range(ind):
        ans.append([arr[ptr1], arr[ptr1 + 1]])
        if arr[ptr1] > arr[ptr1 + 1]:
            arr[ptr2] = arr[ptr1 + 1]
            arr[ptr1 + 1] = arr[ptr1]

        else:
            arr[ptr2] = arr[ptr1]
        ptr1 += 1
        ptr2 += 1

    # Deterministic queries: m from 1 to q
    outputs = []
    for i in range(1, q + 1):
        m = i
        if m <= ind:
            outputs.append((ans[m - 1][0], ans[m - 1][1]))

        else:
            m -= ind
            m = m % (orig_n - 1)
            if m == 0:
                m += orig_n - 1
            outputs.append((arr[ind], arr[ind + m]))

    # Print outputs to keep I/O behavior
    for a, b in outputs:
        # print(a, b)
        pass
if __name__ == "__main__":
    main(10)