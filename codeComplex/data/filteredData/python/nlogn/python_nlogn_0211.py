def solve(n, t, tasks):
    lo = 0
    hi = n

    res = []
    curr_res = 0

    tasks.sort(key=lambda x: x[1])

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        valid_tasks = []
        for i in tasks:
            if i[0] >= mid:
                valid_tasks.append(i)
        
        can_do = False

        curr_sum = 0
        total_used = 0
        r = []
        for i in valid_tasks:
            curr_sum += i[1]
            total_used += 1
            r.append(i[2])
            if curr_sum > t:
                break
            elif total_used >= mid:
                can_do = True
                curr_res = mid
                res = r
                break
        if can_do:
            lo = mid + 1
        else:
            hi = mid - 1
    return curr_res, res


def main(n):
    # n: number of tasks (input scale)
    # Deterministic construction of t and tasks based on n
    t = n * n  # total allowed time grows quadratically with n

    tasks = []
    for idx in range(1, n + 1):
        a_i = (idx % n) + 1  # requirement parameter, in [1, n]
        t_i = (idx * 2) % (n + 1)
        if t_i == 0:
            t_i = 1
        tasks.append((a_i, t_i, idx))

    res, res_array = solve(n, t, tasks)
    print(res)
    print(res)
    if res_array:
        print(" ".join(map(str, res_array)))
    else:
        print()


if __name__ == "__main__":
    main(10)