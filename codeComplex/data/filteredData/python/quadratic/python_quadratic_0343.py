def main(n):
    # Generate deterministic test data based on n
    # s and t are permutations of same multiset of characters
    # Use lowercase letters in a simple pattern
    alphabet = [chr(ord('a') + (i % 26)) for i in range(n)]
    s = ''.join(alphabet)
    # Construct t as a deterministic rearrangement of s
    # For scalability and still some work: reverse, then rotate by 1
    if n > 0:
        t_list = list(reversed(alphabet))
        # rotate left by 1 (deterministically)
        t_list = t_list[1:] + t_list[:1]
        t = ''.join(t_list)

    else:
        t = s

    sl = [i for i in s]
    tl = [i for i in t]
    ans = []
    if ''.join(sorted(s)) != ''.join(sorted(t)):
        # print(-1)
        pass

    else:
        for i in range(n):
            if sl[i] != tl[i]:
                for j in range(i + 1, n):
                    if sl[j] == tl[i]:
                        break
                for k in range(j - 1, i - 1, -1):
                    sl[k], sl[k + 1] = sl[k + 1], sl[k]
                    ans.append(k + 1)
        # print(len(ans))
        pass
        for i in ans:
            # print(i, end=' ')
            pass
        if ans:
            # print()
            pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for scaling experiments
    main(10)