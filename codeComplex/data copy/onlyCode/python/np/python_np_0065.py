import math


def c(k, n):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def main():
    sent = input()
    received = input()
    difference = abs((sent.count('+') - sent.count('-')) - (received.count('+') - received.count('-')))
    unrecognized = received.count('?')
    if difference > unrecognized:
        print(0)
        return
    # 1)n = k + m
    # 2)m = k - diff
    # n = k + k - diff
    # k = (n + diff) // 2
    k = (unrecognized - difference) // 2
    answer = c(k, unrecognized) * 0.5**unrecognized
    print(answer)


if __name__ == '__main__':
    main()
