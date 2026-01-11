def main(n):
    # Interpret n as the size N
    N = max(1, n)

    # Deterministic generation of arr of length N
    # Example: non-negative, increasing-ish sequence with some duplicates possible
    arr = [(i // 2) for i in range(N)]

    if sum(arr) == 0:
        # print('cslnb')
        pass
        return

    arr.sort()
    zeros = 0
    freq = {}
    dup = 0
    res = 0

    for i in range(N):
        num = arr[i]
        if num == 0:
            zeros += 1
            if zeros == 2:
                # print('cslnb')
                pass
                return

        if num not in freq:
            freq[num] = 1

        else:
            dup += 1
            freq[num] += 1

        if dup == 2:
            # print('cslnb')
            pass
            return

    for i in range(N):
        num = arr[i]
        if freq[num] == 2:
            if (num - 1) not in freq:
                freq[num - 1] = 1
                freq[num] = 1
                arr[i] = arr[i] - 1
                res += 1
                break

            else:
                # print('cslnb')
                pass
                return

    minus = [0] * N

    level = 0
    for i in range(N):
        minus[i] = min(arr[i], level)
        if arr[i] >= level:
            level += 1

    for i in range(N):
        res += arr[i] - minus[i]

    if res % 2 == 0:
        # print('cslnb')
        pass

    else:
        # print('sjfnb')
        pass
if __name__ == "__main__":
    main(10)