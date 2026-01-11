def main(n):
    # Generate deterministic input of size n
    # arr: n integers, e.g., arr[i] = (i * 2) % (n + 3)
    arr = [(i * 2) % (n + 3) for i in range(n)]
    # lst: string of length n over '0' and '1', deterministic pattern
    lst = ''.join('0' if i % 2 == 0 else '1' for i in range(n))

    new_arr = sorted([(val, idx) for idx, val in enumerate(arr)])

    stack = []
    ans = []

    size = 0
    left = 0
    right = n - 1

    for ch in lst:
        if ch == '0':
            ans.append(new_arr[left][1] + 1)
            stack.append(new_arr[left][1] + 1)
            size += 1
            left += 1

        if ch == '1':
            if size == 0:
                ans.append(new_arr[right][1] + 1)
                stack.append(new_arr[right][1] + 1)
                right -= 1
            elif size > 0:
                ans.append(stack[-1])
                stack.pop()
                size -= 1

    # print(*ans)
    pass
if __name__ == "__main__":
    # example call for time-complexity experiments
    main(10)