def main(n):
    # Interpret n as length of string s; fix k to a small deterministic value
    k = 3
    if n <= 0:
        # print("")
        pass
        return

    # Deterministically generate a string s of length n over 'a'..'z'
    s = "".join(chr(ord('a') + (i % 26)) for i in range(n))

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
    # print(ans)
    pass
if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(10)