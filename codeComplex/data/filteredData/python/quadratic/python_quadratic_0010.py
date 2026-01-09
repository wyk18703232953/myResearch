from math import sqrt

def main(n):
    # n: number of points
    if n <= 0:
        return

    # Deterministically generate r and x array
    r = 10
    # Spread points with some variation but deterministic
    x = [i * 3 + (i % 5) for i in range(n)]

    arr = []
    for i in range(n):
        arr.append(r)
        for j in range(i):
            if abs(x[j] - x[i]) <= (r * 2):
                diff = x[j] - x[i]
                val = (r * r * 4) - (diff * diff)
                if val >= 0:
                    arr[i] = max(arr[i], arr[j] + sqrt(val))

    arr1 = [str(v) for v in arr]
    # print(" ".join(arr1))
    pass
if __name__ == "__main__":
    main(10)