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


def core_logic(matrix1, matrix2):
    if (
        matrix1 == matrix2
        or matrix1 == reverse_row(matrix2)
        or matrix1 == reverse_column(matrix2)
        or matrix1 == rotate_90(matrix2)
        or matrix1 == rotate_180(matrix2)
        or matrix1 == rotate_270(matrix2)
    ):
        return "Yes"

    matrix2 = reverse_row(matrix2)
    if (
        matrix1 == matrix2
        or matrix1 == reverse_row(matrix2)
        or matrix1 == reverse_column(matrix2)
        or matrix1 == rotate_90(matrix2)
        or matrix1 == rotate_180(matrix2)
        or matrix1 == rotate_270(matrix2)
    ):
        return "Yes"

    matrix2 = reverse_column(matrix2)
    if (
        matrix1 == matrix2
        or matrix1 == reverse_row(matrix2)
        or matrix1 == reverse_column(matrix2)
        or matrix1 == rotate_90(matrix2)
        or matrix1 == rotate_180(matrix2)
        or matrix1 == rotate_270(matrix2)
    ):
        return "Yes"

    matrix2 = transpose(matrix2)
    if (
        matrix1 == matrix2
        or matrix1 == reverse_row(matrix2)
        or matrix1 == reverse_column(matrix2)
        or matrix1 == rotate_90(matrix2)
        or matrix1 == rotate_180(matrix2)
        or matrix1 == rotate_270(matrix2)
    ):
        return "Yes"

    else:
        return "No"


def generate_matrices(cases):
    # Deterministically generate two square matrices of size cases x cases
    # elements are 'A'..'Z' repeated
    chars = ascii_uppercase
    L = len(chars)

    matrix1 = []
    matrix2 = []

    for i in range(cases):
        row1 = [chars[(i * cases + j) % L] for j in range(cases)]
        # matrix2 is a rotated/modified version for deterministic structure
        row2 = [chars[(j * cases + i) % L] for j in range(cases)]
        matrix1.append(row1)
        matrix2.append(row2)

    return matrix1, matrix2


def main(n):
    # Interpret n as matrix dimension (cases)
    if n <= 0:
        return
    cases = n

    matrix1, matrix2 = generate_matrices(cases)
    result = core_logic(matrix1, matrix2)
    # print(result)
    pass
if __name__ == "__main__":
    main(5)