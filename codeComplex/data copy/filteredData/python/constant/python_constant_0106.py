def main(n):
    # Interpret n as the number of test cases
    numCases = max(1, n)

    results = []
    for i in range(numCases):
        # Deterministically generate a and b based on i
        # Ensure they are positive and non-zero
        a = i + 2
        b = 2 * i + 3

        total = 0
        largerNum = max(a, b)
        smallerNum = min(a, b)
        while True:
            div = largerNum // smallerNum
            total += div
            rem = largerNum % (smallerNum * div)
            if rem == 0:
                break

            else:
                largerNum = smallerNum
                smallerNum = rem
        results.append(total)

    for val in results:
        # print(val)
        pass
if __name__ == "__main__":
    main(10)