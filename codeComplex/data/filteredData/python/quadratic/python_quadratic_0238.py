from math import inf


def main(n):
    if n <= 0:
        # print(-1)
        pass
        return

    # Deterministic generation of s_list and c_list based on n
    s_list = [i % 7 + (i // 3) for i in range(n)]
    c_list = [i % 5 + 1 for i in range(n)]

    total_min = inf
    for j in range(n):
        min_i = inf
        for i in range(0, j):
            if s_list[i] < s_list[j]:
                if c_list[i] < min_i:
                    min_i = c_list[i]

        min_k = inf
        for k in range(j + 1, n):
            if s_list[k] > s_list[j]:
                if c_list[k] < min_k:
                    min_k = c_list[k]

        current = min_i + c_list[j] + min_k
        if current < total_min:
            total_min = current

    if total_min != inf:
        # print(total_min)
        pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    main(10)