import string

def main(n):
    # Generate deterministic test data based on n
    if n <= 0:
        return
    # Create two strings a and b of length n using a simple cyclic pattern
    letters = string.ascii_lowercase
    a_str = ''.join(letters[i % 26] for i in range(n))
    b_str = ''.join(letters[(i * 2) % 26] for i in range(n))

    a = list(a_str)
    b = list(b_str)

    def swap(i, j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

    res_a = dict().fromkeys(list(string.ascii_lowercase), 0)
    res_b = dict().fromkeys(list(string.ascii_lowercase), 0)

    for ch in a:
        res_a[ch] += 1
    for ch in b:
        res_b[ch] += 1

    can = True
    for key in res_a:
        if res_a[key] != res_b[key]:
            can = False
            break

    if not can:
        print(-1)
    else:
        ans = []
        for i in range(n):
            if a[i] == b[i]:
                continue
            else:
                idx = -1
                for j in range(i + 1, n):
                    if a[j] == b[i]:
                        idx = j
                        break
                for j in range(idx, i, -1):
                    ans.append(j)
                    swap(j, j - 1)
        print(len(ans))
        if ans:
            print(' '.join(map(str, ans)))


if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(10)