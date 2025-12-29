import random

def solve(n, pos, l, r):
    if (r - l + 1 == n):
        return 0
    if (pos > l and pos < r):
        if (n > r and l > 1):
            x = pos - l + 1 + r - l + 1
            y = r - pos + 1 + r - l + 1
            ans = min(x, y)
        else:
            if (n == r):
                ans = pos - l + 1
            elif (l == 1):
                ans = r - pos + 1
    elif (pos >= r):
        if (n > r):
            ans = pos - r + 1
        else:
            ans = 0
        if (l > 1):
            ans += r - l + 1
    elif (pos <= l):
        if (l > 1):
            ans = l - pos + 1
        else:
            ans = 0
        if (n > r):
            ans += r - l + 1
    return ans

def generate_test_data(n):
    # n is the size of the range [1..n]
    pos = random.randint(1, n)
    # Generate l and r such that 1 <= l <= r <= n
    l = random.randint(1, n)
    r = random.randint(l, n)
    return pos, l, r

def main(n):
    pos, l, r = generate_test_data(n)
    ans = solve(n, pos, l, r)
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改 n
    main(10)