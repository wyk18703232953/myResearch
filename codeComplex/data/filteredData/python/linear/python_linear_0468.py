def main(n):
    if n <= 0:
        # print(0)
        pass
        return
    # Deterministic generation of string a of length n over 'b' and 'w'
    # Pattern: alternates in blocks of increasing size: 1,2,3,4,...
    chars = ['b', 'w']
    a_list = []
    block_size = 1
    idx = 0
    char_idx = 0
    while idx < n:
        take = block_size
        for _ in range(take):
            if idx >= n:
                break
            a_list.append(chars[char_idx])
            idx += 1
        block_size += 1
        char_idx ^= 1
    a = "".join(a_list)

    n_len = len(a)
    b = []
    c = 0
    d = 0
    for i in range(1, n_len):
        if a[i] == a[i - 1]:
            b.append(['bw'.find(a[c]), i - c])
            d = max(d, i - c)
            c = i
    b.append(['bw'.find(a[c]), n_len - c])
    d = max(d, n_len - c)
    if d < n_len and b[0][0] == (b[-1][0] + b[-1][1]) % 2:
        d = max(d, b[-1][1] + b[0][1])
    # print(d)
    pass
if __name__ == "__main__":
    main(10)