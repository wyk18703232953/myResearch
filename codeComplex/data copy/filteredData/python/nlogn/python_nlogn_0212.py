def max_eligible(a, x):
    import bisect
    ind = bisect.bisect_right(a, x)
    if ind <= len(a):
        return a[ind - 1]

    else:
        return -1

def main(n):
    if n < 3:
        # print(-1)
        pass
        return

    U = n
    a = [i for i in range(1, n + 1)]

    max_val = -1
    for i in range(n - 2):
        x = a[i] + U
        val1 = max_eligible(a, x)

        if val1 != -1 and val1 != a[i + 1] and val1 != a[i]:
            val = (val1 - a[i + 1]) / (val1 - a[i])
            if val > max_val:
                max_val = val

    # print(max_val)
    pass
if __name__ == "__main__":
    main(10)