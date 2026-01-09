def main(n):
    # Deterministically generate two numeric strings a, b based on n
    # Ensure they are non-empty
    length_a = max(1, n)
    length_b = max(1, (n * 2) // 3 + 1)

    # Generate a: digits cycling 1..9, avoiding leading zero
    a_digits = []
    for i in range(length_a):
        d = (i % 9) + 1  # 1..9
        a_digits.append(str(d))
    a = "".join(a_digits)

    # Generate b: digits cycling 1..9 but scaled, keep it comparable in magnitude
    b_digits = []
    for i in range(length_b):
        d = ((i * 2) % 9) + 1
        b_digits.append(str(d))
    b = "".join(b_digits)

    na = len(a)
    nb = len(b)

    def fs(idx, arr):
        try:
            # Try to find a smaller digit after position idx
            for i in range(idx + 1, len(arr)):
                if arr[idx] > arr[i]:
                    ans = arr[i]
                    k = arr.copy()
                    k.pop(i)
                    ans += "".join(k)
                    return ans
            return False
        except Exception:
            return False

    if na < nb:
        # print("".join(sorted(list(a), reverse=True)))
        pass

    else:
        if a == b:
            # print(a)
            pass

        else:
            l = sorted(list(a), reverse=True)
            ans1 = ""
            flag = 0
            ans = []
            for ch in b:
                for j in range(len(l)):
                    if ch == l[j]:
                        k = fs(j, l)
                        if k is not False:
                            ans.append(ans1 + fs(j, l))
                        ans1 += l[j]
                        l.pop(j)
                        break
                    if ch > l[j]:
                        ans1 += l[j]
                        l.pop(j)
                        flag = 1
                        break
                if flag == 1:
                    break
            ans1 += "".join(l)
            if int(ans1) <= int(b):
                # print(ans1)
                pass

            else:
                for v in sorted([int(x) for x in ans], reverse=True):
                    if v <= int(b):
                        # print(v)
                        pass
                        break


if __name__ == "__main__":
    main(10)