def main(n):
    # Deterministically generate data based on n
    # s and d are permutations of the same multiset to avoid -1 trivial case
    # We create a base list of characters and then a rotated version
    if n <= 0:
        # print(0)
        pass
        # print()
        pass
        return

    base_chars = [chr(ord('a') + (i % 26)) for i in range(n)]
    shift = n // 3  # deterministic shift based on n
    d_chars = base_chars[shift:] + base_chars[:shift]

    s = base_chars[:]  # copy
    d = d_chars

    # Core logic from original program
    if sorted(s) != sorted(d):
        # print(-1)
        pass

    else:
        ans = []
        for i in range(n):
            if s[i] != d[i]:
                for u in range(i + 1, n):
                    if s[u] == d[i]:
                        ind = u
                        break
                cnt = abs(ind - i)
                s.pop(ind)
                s.insert(i, d[i])
                for k in range(cnt):
                    if ind > 0:
                        ans.append(ind)

                    else:
                        ans.append(1)
                    ind -= 1
        # print(len(ans))
        pass

        if ans:
            # print(*ans)
            pass

        else:
            # print()
            pass
if __name__ == "__main__":
    main(10)