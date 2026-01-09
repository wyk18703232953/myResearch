import math

def main(n):
    # Deterministic generation of n, k based on input scale n
    # Ensure n_used >= 3 to avoid empty prime range
    n_used = max(3, n)
    # Let k scale roughly with n, but stay manageable
    k = max(1, n_used // 10)

    n = n_used

    l = []
    c = 0
    for j in range(2, n):
        p = 0
        for i in range(2, int(math.sqrt(j)) + 1):
            if j % i == 0:
                p = 1
                break

            else:
                pass
        if p == 0:
            l.append(j)

    l += [n]

    for i in range(len(l) - 1):
        if (l[i] + l[i + 1] + 1) in l:
            c += 1

    if c >= k:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # Example call for complexity experiments
    main(1000)