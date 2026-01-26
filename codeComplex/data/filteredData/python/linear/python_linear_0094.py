import math

prime = [True for _ in range(1000001)]

def solve(n, e, h, a, b, c):
    ans = 1e9
    for i in range(1, 1000001):
        su = 0
        ntmp = n
        tmp1 = e
        tmp2 = h
        tmp1 -= i
        tmp2 -= i
        if tmp1 < 0 or tmp2 < 0 or i > ntmp:
            break
        ntmp -= i
        su += c * i
        if ntmp == 0:
            ans = min(ans, su)
            continue
        if a <= b:
            if (tmp1 // 2) >= ntmp:
                su += a * ntmp
                ntmp -= ntmp

            else:
                su += a * (tmp1 // 2)
                ntmp -= (tmp1 // 2)
                if ntmp <= (tmp2 // 3):
                    su += b * ntmp
                    ntmp -= ntmp

                else:
                    su += b * (tmp2 // 3)
                    ntmp -= (tmp2 // 3)

        else:
            if (tmp2 // 3) >= ntmp:
                su += b * ntmp
                ntmp -= ntmp

            else:
                su += b * (tmp2 // 3)
                ntmp -= (tmp2 // 3)
                if ntmp <= (tmp1 // 2):
                    su += a * ntmp
                    ntmp -= ntmp

                else:
                    su += a * (tmp1 // 2)
                    ntmp -= (tmp1 // 2)
        if ntmp == 0:
            ans = min(ans, su)
    if ans == 1e9:
        return -1

    else:
        return int(ans)

def core_main(n, s):
    m = {}
    have = {}
    cc = 0
    for c in s:
        if c not in m:
            m[c] = 1

        else:
            m[c] += 1
    ct = len(m)
    l = 0
    ans = 1e9
    for i in range(0, n):
        if s[i] not in have:
            have[s[i]] = 0
            cc += 1
        have[s[i]] += 1
        while l <= i and have[s[l]] > 1:
            have[s[l]] -= 1
            l += 1
        if cc == ct:
            ans = min(ans, i - l + 1)
    return ans

def generate_string(n):
    if n <= 0:
        return ""
    base_chars = [chr(ord('a') + i) for i in range(26)]
    s_chars = []
    for i in range(n):
        ch = base_chars[i % 26]
        s_chars.append(ch)
    return "".join(s_chars)

def generate_params(n):
    if n <= 0:
        n_val = 1

    else:
        n_val = n
    e = 2 * n_val + 3
    h = 3 * n_val + 5
    a = (n_val % 5) + 1
    b = (n_val % 7) + 2
    c = (n_val % 11) + 3
    return n_val, e, h, a, b, c

def main(n):
    n_val, e, h, a, b, c = generate_params(n)
    cost_result = solve(n_val, e, h, a, b, c)
    s = generate_string(n_val)
    sub_result = core_main(len(s), s)
    # print(cost_result)
    pass
    # print(sub_result)
    pass
if __name__ == "__main__":
    main(10)