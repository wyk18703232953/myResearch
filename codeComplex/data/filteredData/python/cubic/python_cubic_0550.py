def main(n):
    # Deterministically generate two numeric strings s1, s2 based on n
    if n < 1:
        n = 1
    len1 = n
    len2 = n

    # Generate s1 as a non-decreasing sequence of digits derived from i % 10
    s1_digits = [(i * 7 + 3) % 10 for i in range(len1)]
    s1 = "".join(str(d) for d in s1_digits)

    # Generate s2 as another numeric string of length len2
    s2_digits = [(i * 5 + 1) % 10 for i in range(len2)]
    s2 = "".join(str(d) for d in s2_digits)

    arr = list(s1)
    arr.sort(reverse=True)
    if len(s2) > len(s1):
        t = ""
        for i in arr:
            t += i
        # print(t)
        pass

    else:
        t = ""
        l = len(s1)
        for i in range(l):
            index = -1
            ma = -1
            for j in range(len(arr)):
                temp = arr[j]
                tt = []
                for k in range(len(arr)):
                    if k != j:
                        tt.append(arr[k])
                tt.sort()
                for k in tt:
                    temp += k
                temp = t + temp
                if int(s2) >= int(temp):
                    if int(arr[j]) > ma:
                        ma = int(arr[j])
                        index = j
            t += arr[index]
            del arr[index]
        # print(t)
        pass
if __name__ == "__main__":
    main(5)