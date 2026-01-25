import sys
import string


def main(n):
    # n is the length of the array
    if n <= 0:
        return

    # Deterministically generate array of length n
    # Mix of negative, zero, and positive values
    ar = [((i * 2) % 11) - 5 for i in range(n)]

    if n == 1:
        print(ar[0])
        return

    onlyNegs = True
    onlyPos = True

    if max(ar) >= 0:
        onlyNegs = False
    if min(ar) <= 0:
        onlyPos = False

    if onlyNegs:
        print(abs(sum(ar)) + max(ar) * 2)
        return

    if onlyPos:
        print(abs(sum(ar)) - min(ar) * 2)
        return

    print(sum(abs(i) for i in ar))


if __name__ == "__main__":
    main(10)