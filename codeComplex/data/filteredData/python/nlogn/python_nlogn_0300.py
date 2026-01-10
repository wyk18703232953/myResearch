def main(n):
    # Generate deterministic weights w of length n
    # Example: w[i] = (i * 2 + 3) % (n + 7) + 1
    w = [((i * 2 + 3) % (n + 7)) + 1 for i in range(n)]

    # Generate deterministic string s of length n
    # Pattern: first half '0', second half '1', remaining alternating '01'
    half = n // 2
    s_list = []
    for i in range(n):
        if i < half:
            s_list.append('0')
        elif i < 2 * half:
            s_list.append('1')
        else:
            s_list.append('0' if (i - 2 * half) % 2 == 0 else '1')
    s = ''.join(s_list)

    intro = [[v, i] for i, v in enumerate(w, 1)]
    intro.sort(key=lambda x: x[0])
    i = -1
    li = []
    ans = []
    for j in s:
        if j == "0":
            if i + 1 < len(intro):
                i += 1
                ans.append(intro[i][1])
                li.append(intro[i][1])
            else:
                # If more '0' than n, mimic stack push with a dummy stable value
                # to keep behavior defined; here reuse last index
                ans.append(intro[-1][1])
                li.append(intro[-1][1])
        else:
            if li:
                ans.append(li.pop(-1))
            else:
                # If more '1' than pushes, output 0 to keep deterministic behavior
                ans.append(0)

    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main(10)