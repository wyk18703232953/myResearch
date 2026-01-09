def main(n):
    # Interpret n as the number of test cases q
    q = n

    # Deterministic generation of test cases
    # For test case t (0-based):
    #   n_t = 5 + t
    #   k_t = 3 + (t % 3), ensure k_t <= n_t
    #   s_t: string of length n_t over 'R','G','B' generated deterministically
    for t in range(q):
        n_t = 5 + t
        k_t = 3 + (t % 3)
        if k_t > n_t:
            k_t = n_t

        # Generate string s_t deterministically
        chars = ['R', 'G', 'B']
        s_list = [chars[(i + t) % 3] for i in range(n_t)]
        s = "".join(s_list)

        min_ans = 10 ** 9
        for i in range(n_t - k_t + 1):
            count1 = 0
            count2 = 0
            count3 = 0
            for j in range(k_t):
                idx = i + j
                mod = idx % 3
                ch = s[idx]
                if mod == 0:
                    if ch != "R":
                        count1 += 1
                    if ch != "G":
                        count2 += 1
                    if ch != "B":
                        count3 += 1
                elif mod == 1:
                    if ch != "G":
                        count1 += 1
                    if ch != "B":
                        count2 += 1
                    if ch != "R":
                        count3 += 1
                else:  # mod == 2
                    if ch != "B":
                        count1 += 1
                    if ch != "R":
                        count2 += 1
                    if ch != "G":
                        count3 += 1
            if count1 < min_ans:
                min_ans = count1
            if count2 < min_ans:
                min_ans = count2
            if count3 < min_ans:
                min_ans = count3
        # print(min_ans)
        pass
if __name__ == "__main__":
    main(5)