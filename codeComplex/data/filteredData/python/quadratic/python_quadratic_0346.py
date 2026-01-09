def main(n):
    # Deterministic data generation
    # s and d are permutations of lowercase letters, length n
    # s is ascending pattern, d is descending pattern (wrapped)
    s = [chr(ord('a') + (i % 26)) for i in range(n)]
    d = [chr(ord('a') + ((n - 1 - i) % 26)) for i in range(n)]

    if sorted(s) != sorted(d):
        # print(-1)
        pass
        return

    else:
        ans = []
        for i in range(n):
            if s[i] != d[i]:
                ind = -1
                for u in range(i + 1, n):
                    if s[u] == d[i]:
                        ind = u
                        break

                if ind == -1:
                    # This should not happen with our deterministic construction,
                    # but keep original logic behavior consistent.
                    # print(-1)
                    pass
                    return

                cnt = abs(ind - i)
                s.pop(ind)
                s.insert(i, d[i])
                for _ in range(cnt):
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
if __name__ == "__main__":
    # Example call; adjust n for different input scales
    main(10)