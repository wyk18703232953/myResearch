def main(n):
    # Generate deterministic digit lists a and b of length n
    # Digits cycle 0-9 in different phases to avoid trivial equality
    a = [(i % 10) for i in range(n)]
    b = [((i * 3 + 1) % 10) for i in range(n)]

    ans = []
    la, lb = len(a), len(b)
    if la != lb:
        # print(*sorted(a, reverse=True), sep="")
        pass

    else:
        for i in range(lb):
            if b[i] in a:
                ans.append(b[i])
                a.remove(b[i])

            else:
                ma = -1
                for j in a:
                    if j < b[i]:
                        ma = max(ma, j)
                if ma != -1:
                    ans.append(ma)
                    a.remove(ma)

                else:
                    i -= 1
                    while ans:
                        a.append(ans.pop())
                        ma = -1
                        for j in a:
                            if j < b[i]:
                                ma = max(ma, j)
                        if ma != -1:
                            ans.append(ma)
                            a.remove(ma)
                            break
                        i -= 1
                a.sort()
                while a:
                    ans.append(a.pop())
                break
        # print("".join(str(i) for i in ans))
        pass
if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(20)