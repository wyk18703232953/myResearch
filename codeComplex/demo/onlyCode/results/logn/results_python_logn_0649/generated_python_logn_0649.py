def main(n):
    k = n * (n + 1) // 4
    def check(mid):
        added = n - mid
        total = (added * (added + 1)) // 2
        return total - mid >= k
    low = 0
    high = n - 1
    while low < high:
        mid = (low + high + 1) // 2
        if check(mid):
            low = mid
        else:
            high = mid - 1
    return low

if __name__ == "__main__":
    print(main(10))