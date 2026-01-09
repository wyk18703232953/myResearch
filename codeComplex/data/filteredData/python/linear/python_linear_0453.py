def main(n):
    # Map n to problem parameters:
    # Let string length = n, and k = 2 * (n // 4) so that k is even and <= n
    length = n
    if length <= 0:
        # print("")
        pass
        return
    k = 2 * (length // 4)
    if k > length:
        k = length if length % 2 == 0 else length - 1

    # Deterministically generate a parenthesis string of length `length`
    # Pattern: first half '(', second half ')', truncated/extended to length
    half = length // 2
    arr = ['('] * half + [')'] * (length - half)
    # If length is odd, arr is already of size length

    st = []
    ans = []
    for i in range(length):
        if k <= 0:
            break

        else:
            if arr[i] == '(':
                st.append((arr[i], i))

            else:
                if st and st[-1][0] == '(':
                    k -= 2
                    ans.append(st.pop())
                    ans.append((arr[i], i))

                else:
                    st.append((arr[i], i))

    ans.sort(key=lambda x: x[1])
    res = []
    for i in ans:
        res.append(i[0])
    # print(''.join(res))
    pass
if __name__ == "__main__":
    # Example call for experimental purposes
    main(20)