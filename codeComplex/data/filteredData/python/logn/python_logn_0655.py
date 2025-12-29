# ------------------------- converted code --------------------------- #

def main(n):
    """
    n: problem scale parameter
    This main will generate a test (n, k) and run the original logic.
    """
    # 1. Generate test data (n, k)
    #    Original constraints are unknown; we create a reasonable k.
    #    The logic requires 0 <= k <= n*(n+1)//2, so we set k accordingly.
    k = (n * (n + 1)) // 4  # for example, quarter of the max sum

    # 2. Core logic from the original code, with n, k taken from variables

    def possible(x):
        days = n - x
        tot = days * (days + 1) // 2
        return tot - x <= k

    low = 0
    high = n

    while low <= high:
        mid = (low + high) // 2
        if possible(mid):
            high = mid - 1
        else:
            low = mid + 1

    # 3. Return the result instead of printing
    return low


# Example usage (can be removed when importing as a module):
if __name__ == "__main__":
    # You can change the argument below to test different scales
    result = main(10)
    print(result)