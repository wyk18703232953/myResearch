def main(n):
    # Generate a deterministic string s of length n
    # Pattern: '+' if i % 3 != 0 else '-'
    s = ''.join('+' if i % 3 != 0 else '-' for i in range(n))
    ans = 0
    for ch in s:
        if ch == '+':
            ans += 1

        else:
            ans -= 1
        if ans < 0:
            ans = 0
    return ans

if __name__ == "__main__":
    result = main(10)
    # print(result)
    pass