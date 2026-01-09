def main(n):
    results = []
    for k in range(1, n + 1):
        l = k
        r = 2 * k
        if len(bin(l)) < len(bin(r)):
            ans = 2 ** len(bin(r)[2:]) - 1

        else:
            p = bin(l)[2:]
            q = bin(r)[2:]
            rr = 0
            for i in range(len(q)):
                if p[i] != q[i]:
                    rr = len(p) - i
                    break
            ans = 2 ** rr - 1
        results.append(ans)
    return results

if __name__ == "__main__":
    # Example call for scale n=10
    out = main(10)
    for v in out:
        # print(v)
        pass