def main(n):
    l = 0
    r = (1 << n) - 1
    ans = 0
    for i in range(63, -1, -1):
        if r & (1 << i) > 0 and l & (1 << i) == 0:
            ans = (1 << (i + 1)) - 1
            break
    return ans

if __name__ == "__main__":
    print(main(10))