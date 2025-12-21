def fn(n):
    return (n * (n + 1)) / 2

def search(x, n):
    left, right = 0, n
    while left <= right:
        middle = left + (right - left) // 2
        if fn(middle) - (n - middle) == x:
            return n - middle
        elif fn(middle) - (n - middle) > x:
            right = middle - 1
        else:
            left = middle + 1
    return -1

def main(n):
    k = n // 2
    return search(k, n)

if __name__ == '__main__':
    print(main(10))