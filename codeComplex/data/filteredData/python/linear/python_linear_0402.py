def main(n):
    # n controls the size of the arrays a and b
    if n <= 0:
        return

    EPS = 1e-6

    # Deterministic generation of m, a, b based on n
    m = 1000 + n  # total non-fuel weight

    # Generate a and b with values >= 2 to avoid division by 0 or 1
    # Pattern is fully deterministic and depends only on n
    a = [2 + (i % 9) for i in range(n)]
    b = [3 + (i % 9) for i in range(n)]
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
    # Example deterministic call; adjust n to run different scales
    main(5)