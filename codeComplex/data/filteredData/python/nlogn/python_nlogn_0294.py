def main(n):
    # n: number of passengers / size of input array
    if n <= 0:
        return

    # Deterministic generation of input array `arr`
    # Example pattern: arr[i] = (i * 2 + 3) % (2*n + 1)
    arr = [((i * 2 + 3) % (2 * n + 1)) for i in range(n)]

    # Deterministic generation of passenger string of length 2*n
    # Example pattern: alternating '0' and '1', with a simple variation
    passenger = []
    for i in range(2 * n):
        if i % 4 < 2:
            passenger.append('0')
        else:
            passenger.append('1')
    passenger = ''.join(passenger)

    # Core algorithm (unchanged logic, no input())
    new_arr = [(val, idx + 1) for idx, val in enumerate(arr)]
    new_arr = sorted(new_arr)

    from collections import deque
    que = deque()
    ans = [0] * (2 * n)

    left = 0
    right = n - 1
    le = 0

    for i in range(2 * n):
        if passenger[i] == '0':
            ans[i] = new_arr[left][1]
            que.append(new_arr[left][1])
            left += 1
            le += 1
        else:
            if le >= 1:
                ans[i] = que[-1]
                que.pop()
                le -= 1
            else:
                ans[i] = new_arr[right][1]
                que.append(new_arr[right][1])
                right -= 1
                le += 1

    print(*ans)


if __name__ == "__main__":
    main(5)