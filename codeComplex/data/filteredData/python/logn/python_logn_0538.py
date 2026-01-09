def main(n):
    k = n
    digit = 1
    low = 1
    high = 9
    totalDigit = 9
    lastTotalDigit = 0
    while totalDigit < k:
        low *= 10
        high = 10 * low - 1
        digit += 1
        lastTotalDigit = totalDigit
        totalDigit += (high + 1 - low) * digit
    k -= lastTotalDigit
    cur = str(low + (k - 1) // digit)
    # print(cur[(k - 1) % digit])
    pass
if __name__ == "__main__":
    main(1000)