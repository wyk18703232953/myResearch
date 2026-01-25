def main(n):
    # Generate a deterministic digit string s of length n
    if n <= 0:
        print("NO")
        return
    s = ''.join(str((i * 7 + 3) % 10) for i in range(n))

    total_sum = sum(int(ch) for ch in s)
    for target in range(9 * n + 1):
        cnt = 0
        cursum = 0
        for ch in s:
            cursum += int(ch)
            if cursum == target:
                cnt += 1
                cursum = 0

        if cursum == 0 and cnt > 1:
            print("YES")
            return

    print("NO")


if __name__ == "__main__":
    main(10)