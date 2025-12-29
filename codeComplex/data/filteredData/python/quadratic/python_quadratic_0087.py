from collections import deque, defaultdict, Counter
from itertools import product, groupby, permutations, combinations
from math import gcd, floor, inf, log2, sqrt, log10
from bisect import bisect_right, bisect_left
from statistics import mode
from string import ascii_uppercase
import random


def transpose(matrix):
    return [list(x) for x in zip(*matrix)]


def reverse_row(matrix):
    return matrix[::-1]


def reverse_column(matrix):
    return [x[::-1] for x in matrix]


def rotate_90(matrix):
    """counterclockwise 90° (same as clockwise 270°)"""
    return reverse_row(transpose(matrix))


def rotate_180(matrix):
    """same for both clockwise and counterclockwise"""
    return reverse_row(reverse_column(matrix))


def rotate_270(matrix):
    """counterclockwise 270° (same as clockwise 90°)"""
    return reverse_column(transpose(matrix))


def main(n):
    """
    n: matrix size (n x n).

    生成两张 n x n 的字符矩阵 matrix1, matrix2，
    然后用和原程序相同的逻辑判断 matrix2 经过若干操作
    是否能与 matrix1 相同，并打印 "Yes"/"No"。
    """
    # 生成测试数据：随机从大写字母中选取
    matrix1 = [
        [random.choice(ascii_uppercase) for _ in range(n)]
        for _ in range(n)
    ]

    matrix2 = [
        [random.choice(ascii_uppercase) for _ in range(n)]
        for _ in range(n)
    ]

    # 原逻辑封装为一个函数
    def check(matrix1, matrix2):
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

    check(matrix1, matrix2)


if __name__ == "__main__":
    # 示例：规模 n = 4
    main(4)