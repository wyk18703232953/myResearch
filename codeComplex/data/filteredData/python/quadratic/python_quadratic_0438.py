def main(n):
    # Generate a deterministic binary string of length n
    # Example pattern: digits are (i % 2)
    s = ''.join(str(i % 2) for i in range(n))
    arr = [int(z) for z in s]

    ans = 0

    if n == 2:
        if arr[0] == arr[1]:
            # print("YES")
            pass

        else:
            # print("NO")
            pass
        return

    for l in range(1, n - 1):
        s_val = sum(arr[:l])
        i = l
        v = [s_val]
        curr = 0
        while i < n:
            curr += arr[i]
            if i == n - 1:
                if curr > s_val:
                    curr -= arr[i]
                    v.append(curr)
                    curr = arr[i]
                v.append(curr)
            elif curr > s_val:
                curr -= arr[i]
                v.append(curr)
                curr = arr[i]
            i += 1

        if len(set(v)) == 1:
            # print("YES")
            pass
            ans = 1
            return

    if not ans:
        # print("NO")
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)