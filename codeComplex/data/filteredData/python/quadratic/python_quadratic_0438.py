def main(n):
    # Interpret n as the length of the array
    if n <= 0:
        return

    # Deterministic generation of arr: digits 0-9 repeating
    # but ensure it's a list of integers as in the original (from string digits)
    base_digits = [i % 10 for i in range(n)]
    arr = base_digits

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
        s = sum(arr[:l])
        i = l
        v = [s]
        curr = 0
        while i < n:
            curr += arr[i]
            if i == n - 1:
                if curr > s:
                    curr -= arr[i]
                    v.append(curr)
                    curr = arr[i]
                v.append(curr)
            elif curr > s:
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
    # Example call for scalability/experiments
    main(10)