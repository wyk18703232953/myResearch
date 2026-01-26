def main(n):
    # Interpret n as both number of boys and girls; m is also set to n
    m = n

    # Deterministically generate boys_out and girls_in based on n
    # boys_out: n integers in decreasing order
    boys_out = [n * 2 - i for i in range(n)]
    boys_out.sort(reverse=True)

    # girls_in: n integers in increasing order, all >= max(boys_out)
    max_boy = boys_out[0] if boys_out else 0
    girls_in = [max_boy + (i // 2) for i in range(n)]
    girls_in.sort()

    max_boy = max(boys_out) if boys_out else 0
    ans = 0
    for boy in boys_out:
        ans += boy * m

    count = 0
    i = 0
    for girl in girls_in:
        if girl < max_boy:
            # print(-1)
            pass
            return

        if girl > max_boy:
            if count == m - 1:
                count = 0
                i += 1
            if i >= n:
                # print(-1)
                pass
                return
            ans += girl - boys_out[i]
            count += 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)