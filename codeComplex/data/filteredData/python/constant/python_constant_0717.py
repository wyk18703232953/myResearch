import math

def main(n):
    # Precompute arrays a and b as in the original program
    a = [9]
    for i in range(2, 20):
        a.append(10 ** i - 10 ** (i - 1))
    b = [0]
    for i in range(1, 20):
        b.append(b[-1] + i * a[i - 1])

    # Core logic using the given n as input size
    for i in range(20):
        if n <= b[i]:
            break
    p = b[i - 1]
    k = n - p
    ans = 10 ** (i - 1) - 1 + math.ceil(k / i)

    if k % i == 0:
        # print(('0' + str(ans))[i])
        pass

    else:
        # print(('0' + str(ans))[k % i])
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for different scales
    main(1000000)