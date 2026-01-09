def main(n):
    # Map n to problem parameters deterministically
    # n controls both m (number of special elements) and k (divider)
    if n < 1:
        n = 1
    m = n
    k = max(1, n // 3)

    # Generate special array deterministically: strictly increasing positive integers
    # Example: arithmetic progression with step = (k % 5) + 1
    step = (k % 5) + 1
    special = [step * (i + 1) for i in range(m)]

    numOn = 0
    numOps = 0
    while numOn < m:
        numOps += 1
        op = ((special[numOn] - numOn - 1) // k) * k + k + numOn + 1
        while numOn < m and special[numOn] < op:
            numOn += 1
    # print(numOps)
    pass
if __name__ == "__main__":
    main(10)