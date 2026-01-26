def check(st, n):
    count = 1
    i = 1
    pre = st[0]
    indx = [0 for _ in range(n)]
    pre_indx = 0
    while i < n:
        if pre != st[i]:
            count += 1

        else:
            indx[pre_indx] = count
            count = 1
            pre_indx = i
        pre = st[i]
        i += 1
    indx[pre_indx] = count
    return indx

def generate_string(n):
    if n <= 0:
        return ""
    base = "abc"
    return "".join(base[i % len(base)] for i in range(n))

def main(n):
    st = generate_string(n)
    if n == 0:
        # print(0)
        pass
        return
    actual_indx = check(st, n)
    reverse_indx = check(st[::-1], n)
    if st[0] == st[-1]:
        # print(max(actual_indx))
        pass

    else:
        # print(min(n, max(max(actual_indx[1:]), actual_indx[0] + reverse_indx[0])))
        pass
if __name__ == "__main__":
    main(10)