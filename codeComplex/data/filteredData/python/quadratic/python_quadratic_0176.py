def main(n):
    # Determine k as a function of n for scalable experiments
    # Ensure k >= 1 and reasonably sized relative to 256
    k = max(1, min(50, n // 2))

    # Generate ns deterministically within [0, 255]
    # Repeat pattern 0..255 as needed, truncated to length n
    ns = [(i * 7 + 13) % 256 for i in range(n)]

    done = [None] * 256
    ans = [None] * n

    for i in range(n):
        c = ns[i]
        if done[c] is None:
            j = c
            while True:
                if j < 0 or c - j >= k or (done[j] is not None and done[j] != -1):
                    break
                j -= 1
            j += 1
            for kk in range(k):
                if kk + j >= 256 or (done[kk + j] is not None and done[kk + j] != -1):
                    break
                if kk + j <= c:
                    done[kk + j] = j

                else:
                    done[kk + j] = -1
        elif done[c] == -1:
            j = c
            while True:
                if done[j] is not None and done[j] != -1:
                    break
                j -= 1
            a = done[j]
            for kk in range(j, c + 1):
                done[kk] = a
        ans[i] = done[c]

    ans_str = [str(x) for x in ans]
    # print(" ".join(ans_str))
    pass
if __name__ == "__main__":
    # Example scalable call; adjust n for experiments
    main(1000)