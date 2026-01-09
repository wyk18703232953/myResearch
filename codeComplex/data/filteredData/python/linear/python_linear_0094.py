import math

prime = [True for _ in range(1000001)]

def solve_single_case(n, e, h, a, b, c):
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

def core_string_algorithm(s):
    n = len(s)
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
    # Use first up to 26 lowercase letters deterministically
    chars = [chr(ord('a') + (i % 26)) for i in range(n)]
    return "".join(chars)

def main(n):
    # Use n as the primary size parameter.
    # 1) Run the original "solve" logic on deterministically generated numeric inputs.
    # Map n to parameters in a fixed way.
    # Ensure values stay reasonable but scale with n.
    e = 2 * n + 3
    h = 3 * n + 5
    a = (n % 7) + 1
    b = (n % 5) + 2
    c = (n % 3) + 3
    numeric_result = solve_single_case(n, e, h, a, b, c)

    # 2) Run the original "main" string logic on a generated string of length n.
    s = generate_string(n)
    string_result = core_string_algorithm(s)

    # Print results so that runtime is visible and deterministic
    # print(numeric_result)
    pass
    # print(string_result)
    pass
if __name__ == "__main__":
    main(1000)