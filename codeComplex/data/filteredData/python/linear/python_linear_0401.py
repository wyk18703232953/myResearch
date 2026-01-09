def main(n):
    EPS = 1e-6

    # Scale n to get a reasonable problem size
    # Use n as the number of segments
    if n <= 0:
        return

    m = n * 10  # total weight parameter, deterministic from n

    # Generate deterministic a and b based on n
    # Ensure no zero values and keep them reasonably bounded
    a = [(i % 7) + 2 for i in range(1, n + 1)]
    b = [(i % 9) + 2 for i in range(1, n + 1)]
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
        while abs(left - right) >= EPS:
            mid = (left + right) / 2
            if check(mid):
                right = mid

            else:
                left = mid
        return (left + right) / 2

    res = binary_search(0, 1e9 + 1)
    if res - 1e9 > EPS:
        # print(-1)
        pass

    else:
        # print("%.10f" % res)
        pass
if __name__ == "__main__":
    main(1000)