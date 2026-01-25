import sys

def build_string(n, k):
    # Deterministically generate a string of length n over 'a'..'z'
    if n <= 0:
        return ""
    chars = []
    for i in range(n):
        # simple periodic pattern
        chars.append(chr(ord('a') + (i % 26)))
    return "".join(chars)

def solve(n, k):
    s = build_string(n, k)
    ans = ""
    for i in range(len(s) + 1, 0, -1):
        res = s
        end = s[-i:]
        for _ in range(k - 1):
            res += end
        cnt = 0
        for j in range(len(res) - len(s) + 1):
            if res[j:j + len(s)] == s:
                cnt += 1
        if cnt == k:
            ans = res
    return ans

def main(n):
    # Interpret n as the length of the base string; choose a deterministic k.
    # Ensure k >= 1 and grows slowly with n.
    k = max(1, n // 5 + 1)
    result = solve(n, k)
    sys.stdout.write(result + ("\n" if result else ""))

if __name__ == "__main__":
    # Example call for deterministic experiment
    main(10)