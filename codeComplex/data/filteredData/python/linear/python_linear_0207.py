def main(n):
    from collections import *
    ceil1 = lambda a, b: (a + b - 1) // b

    # Generate deterministic s and schedule a based on n
    # n is the number of existing time points
    s = (n % 60) + 1  # gap requirement between 1 and 60
    a = []
    for i in range(n):
        # Spread times deterministically over the day
        h = (i * 7) % 24
        m = (i * 13) % 60
        a.append([h, m])

    ans = -1
    for i in range(26):
        for j in range(60):
            tem = i * 60 + j
            ans = (i, j)
            for h, m in a:
                tem2 = h * 60 + m
                if tem <= tem2:
                    if tem2 - (tem + 1) < s:
                        ans = -1
                        break

                else:
                    if tem - (tem2 + 1) < s:
                        ans = -1
                        break

            if ans != -1:
                # print('%d %d' % (ans[0], ans[1]))
                pass
                return
    # If no valid time found, print a sentinel
    # print('-1 -1')
    pass
if __name__ == "__main__":
    main(5)