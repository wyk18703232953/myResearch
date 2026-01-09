def main(n):
    # Interpret n as the length of the parentheses string
    # Generate a deterministic input: balanced parentheses of length n (if n is odd, last char is ')')
    s = []
    for i in range(n):
        if i < n // 2:
            s.append('(')

        else:
            s.append(')')
    line = ''.join(s)

    # Define k deterministically as the largest even number <= n
    k = n if n % 2 == 0 else n - 1

    if n == k:
        # print(line)
        pass

    else:
        ans = []
        arr = []
        for ch in line:
            arr.append(ch)

        for i in range(n):
            if len(ans) == k // 2:
                break
            if arr[i] == '(':
                ans.append(i)

        for i in range(n - 1, -1, -1):
            if len(ans) == k:
                break
            if arr[i] == ')':
                ans.append(i)

        ans.sort()
        for i in ans:
            # print(arr[i], end="")
            pass
        # print()
        pass
if __name__ == "__main__":
    main(10)