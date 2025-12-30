#   Author: yumtam (modified)
#   Converted to parameterized main(n) without input()

import random

def is_square(x: int) -> bool:
    sq = int(x**0.5)
    return sq * sq == x

def main(n: int):
    """
    n: number of test cases to generate and run.
    For each test case, we randomly generate an integer value for n (problem's n),
    and apply the original logic, printing YES/NO.
    """
    # You can adjust range of generated test data as needed
    MIN_VAL, MAX_VAL = 1, 10**9

    for _ in range(n):
        # generate test data for original "n"
        val = random.randint(MIN_VAL, MAX_VAL)

        if ((val % 2 == 0 and is_square(val // 2))
                or (val % 4 == 0 and is_square(val // 4))):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    # Example: run with 5 generated test cases
    main(5)