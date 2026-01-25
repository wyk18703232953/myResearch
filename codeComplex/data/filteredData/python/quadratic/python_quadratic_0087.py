from collections import deque, defaultdict, Counter
from itertools import product, groupby, permutations, combinations
from math import gcd, floor, inf, log2, sqrt, log10
from bisect import bisect_right, bisect_left
from statistics import mode
from string import ascii_uppercase


def transpose(matrix):
    return [list(x) for x in zip(*matrix)]


def reverse_row(matrix):
    return matrix[::-1]


def reverse_column(matrix):
    return [x[::-1] for x in matrix]


def rotate_90(matrix):
    return reverse_row(transpose(matrix))


def rotate_180(matrix):
    return reverse_row(reverse_column(matrix))


def rotate_270(matrix):
    return reverse_column(transpose(matrix))


def main(n):
    if n <= 0:
        return

    cases = n

    # deterministic generation of matrix1 and matrix2, each cases x cases
    # use letters from ascii_uppercase in a repeating pattern
    chars = ascii_uppercase
    m = len(chars)

    matrix1 = []
    for i in range(cases):
        row = [chars[(i * cases + j) % m] for j in range(cases)]
        matrix1.append(row)

    # generate matrix2 by applying a fixed sequence of transformations
    # so structure is similar but not necessarily identical
    matrix2 = []
    for i in range(cases):
        row = [chars[(i * cases + (cases - 1 - j)) % m] for j in range(cases)]
        matrix2.append(row)

    # original decision logic
    if (
        matrix1 == matrix2
        or matrix1 == reverse_row(matrix2)
        or matrix1 == reverse_column(matrix2)
        or matrix1 == rotate_90(matrix2)
        or matrix1 == rotate_180(matrix2)
        or matrix1 == rotate_270(matrix2)
    ):
        print("Yes")
        return

    matrix2 = reverse_row(matrix2)
    if (
        matrix1 == matrix2
        or matrix1 == reverse_row(matrix2)
        or matrix1 == reverse_column(matrix2)
        or matrix1 == rotate_90(matrix2)
        or matrix1 == rotate_180(matrix2)
        or matrix1 == rotate_270(matrix2)
    ):
        print("Yes")
        return

    matrix2 = reverse_column(matrix2)
    if (
        matrix1 == matrix2
        or matrix1 == reverse_row(matrix2)
        or matrix1 == reverse_column(matrix2)
        or matrix1 == rotate_90(matrix2)
        or matrix1 == rotate_180(matrix2)
        or matrix1 == rotate_270(matrix2)
    ):
        print("Yes")
        return

    matrix2 = transpose(matrix2)
    if (
        matrix1 == matrix2
        or matrix1 == reverse_row(matrix2)
        or matrix1 == reverse_column(matrix2)
        or matrix1 == rotate_90(matrix2)
        or matrix1 == rotate_180(matrix2)
        or matrix1 == rotate_270(matrix2)
    ):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main(5)