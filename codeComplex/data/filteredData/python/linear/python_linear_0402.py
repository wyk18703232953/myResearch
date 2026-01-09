def main(n):
    EPS = 1e-6

    # Scale definition:
    # n is the number of segments
    # m is fixed deterministically as n
    # a and b are deterministic arrays of length n
    m = n

    # Generate deterministic coefficients a and b, avoid zeros
    a = [2 + (i % 5) for i in range(n)]
    b = [3 + (i % 7) for i in range(n)]
    b.append(b[0])

    def check(f):
        fuel_left = f
        total_weight = float(m + fuel_left)
        for i in range(n):
            cost = total_weight / a[i]
            fuel_left = fuel_left - cost
            total_weight = total_weight - cost

            cost = total_weight / b[i + 1]
            fuel_left = fuel_left - cost
            total_weight = total_weight - cost
            if fuel_left < 0:
                return False
        return True

    def binary_search(left, right):
        mid = (left + right) / 2
        if abs(left - right) < EPS:
            return mid
        if check(mid):
            return binary_search(left, mid)

        else:
            return binary_search(mid, right)

    res = binary_search(0, 1e9 + 1)
    if res - 1e9 > EPS:
        # print(-1)
        pass

    else:
        # print("%.10f" % res)
        pass
if __name__ == "__main__":
    main(1000)