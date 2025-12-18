if __name__ == '__main__':
    cin = input
    n = int(cin())
    s, t = [*cin()], cin()
    i, r = 0, list()

    if sorted(s) != sorted(t):
        print(-1)
    else:
        while i < n:
            j = i
            while j < n and s[j] != t[i]:
                j += 1
            s[i:j + 1] = s[j:j + 1] + s[i:j]
            r.extend(range(j, i, -1))
            i += 1
        print(len(r))
        print(*r)