# -*- coding: utf-8 -*-
"""
Converted version:
- No input()
- main(n) as entry, where n is the scale (controls test data generation)
- Generates test pairs (l, r) based on n and processes them
"""

import math
import random

def process_pair(l: int, r: int) -> int:
    """
    Original logic encapsulated into a function:
    Given l and r, compute:
        x = l ^ r
        if x == 0: return 0
        else:
            k = floor(log2(x))
            return (1 << (k + 1)) - 1
    """
    x = l ^ r
    if x:
        k = int(math.log(x, 2))
        return (1 << (k + 1)) - 1
    else:
        return 0

def main(n: int):
    """
    n controls how many test cases to generate.
    For each i in [0, n-1], generate a pair (l, r) and print result.
    Test data strategy (simple and deterministic for reproducibility):
      l = i
      r = (2 * i + 1)
    You can change the generation strategy as needed.
    """
    results = []
    for i in range(n):
        l = i
        r = 2 * i + 1
        res = process_pair(l, r)
        results.append(res)
    # Output results, one per line
    for val in results:
        print(val)

if __name__ == "__main__":
    # Example: run main with a chosen scale
    main(10)