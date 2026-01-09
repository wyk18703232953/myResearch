def main(n):
    # Generate deterministic input based on n
    # n is the length of the digit string s, digits cycle from 0 to 9
    s = ''.join(str(i % 10) for i in range(n))

    for target_sum in range(9 * n + 1):
        cnt = 0
        cursum = 0
        for ch in s:
            cursum += ord(ch) - 48  # int(ch) but faster and deterministic
            if cursum == target_sum:
                cnt += 1
                cursum = 0

        if cursum == 0 and cnt > 1:
            # print("YES")
            pass
            return

    # print("NO")
    pass
if __name__ == "__main__":
    main(10)