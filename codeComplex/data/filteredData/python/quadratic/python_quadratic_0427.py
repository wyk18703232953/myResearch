def main(n):
    # Deterministically generate input:
    # Original input: n, then a string of digits of length n
    # Here we create a list of 0/1 digits of length n in a fixed pattern.
    arr = [i % 2 for i in range(n)]

    if len(set(arr)) == 1:
        result = 'YES'

    else:
        val = sum(arr)
        factor = set()
        for i in range(1, int(val ** 0.5) + 1):
            if val % i == 0:
                factor.add(i)
                factor.add(val // i)
        can = False
        for i in factor:
            each = val // i
            if 1 < i <= n:
                idx = 0
                temp = 0
                cnt = 0
                while idx < n:
                    if temp + arr[idx] < each:
                        temp += arr[idx]
                    elif temp + arr[idx] > each:
                        temp = 0

                    else:
                        temp = 0
                        cnt += 1
                    idx += 1
                if cnt == i:
                    can = True
        result = 'YES' if can else 'NO'
    # print(result)
    pass
if __name__ == "__main__":
    main(1000)