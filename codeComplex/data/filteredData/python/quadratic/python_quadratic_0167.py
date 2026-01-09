def main(n):
    # Interpret n as the length of p and also as the max value in p (0..n-1)
    # Generate deterministic input:
    # k is chosen as max(1, n//4) so that it's linked to n but deterministic
    if n <= 0:
        return
    k = max(1, n // 4)
    # p is a permutation-like but deterministic sequence in [0, n-1]
    # Example pattern: p[i] = (i*2) % n
    p = [(i * 2) % n for i in range(n)]

    # Original algorithm logic preserved, with generated n, k, p
    ans = [-1] * (max(p) + 1)
    ans[0] = 0
    for i in range(n):
        if ans[p[i]] < 0:
            position = p[i] - k + 1
            for j in range(max(0, p[i] - k + 1), p[i] + 1):
                if ans[j] < 0:
                    position = j
                    break
            j = max(0, position - 1)
            key = ans[j]
            count = 0
            while j >= 0:
                if ans[j] != key:
                    position1 = j + 1
                    break
                j -= 1
                count += 1
            if count + p[i] + 1 - position > k:
                key = position
            for j in range(position, p[i] + 1):
                ans[j] = key

    for i in range(n):
        if i != len(p) - 1:
            wk1 = " "

        else:
            wk1 = "\n"
        # print(ans[p[i]], end=wk1)
        pass
if __name__ == "__main__":
    main(10)