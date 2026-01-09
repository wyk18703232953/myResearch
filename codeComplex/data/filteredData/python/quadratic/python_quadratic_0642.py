def nospace(l):
    ans = ''.join(str(i) for i in l)
    return ans

def main(n):
    # n is the size of the array
    if n <= 0:
        # print(0)
        pass
        return

    # Deterministic generation of array 'a' of length n
    # Use a mix of values to exercise divisibility logic
    a = [(i % 7) + 1 for i in range(1, n + 1)]

    a.sort()

    i = 0
    ans = 0
    while i < len(a):
        if a[i]:
            ans += 1
            j = i + 1
            while j < n:
                if a[j] % a[i] == 0:
                    a[j] = 0
                j += 1
        i += 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)