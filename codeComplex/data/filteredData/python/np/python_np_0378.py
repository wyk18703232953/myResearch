def solve(k, n, a):
    asum, sums = calc_sums(k, n, a)
    if asum % k != 0:
        return False, None, None
    tsum = asum // k
    num_map = build_num_map(k, n, a)
    masks = [None] * (1 << k)
    answer = [False] * (1 << k)
    left = [0] * (1 << k)
    right = [0] * (1 << k)
    for i in range(k):
        for j in range(n[i]):
            found, mask, path = find_cycle(i, j, i, j, k, n, a, sums, tsum, num_map, 0, dict())
            if found:
                answer[mask] = True
                masks[mask] = path
    for mask_right in range(1 << k):
        if not masks[mask_right]:
            continue
        zeroes_count = 0
        for u in range(k):
            if (1 << u) > mask_right:
                break
            if (mask_right & (1 << u)) == 0:
                zeroes_count += 1
        for mask_mask in range(1 << zeroes_count):
            mask_left = 0
            c = 0
            for u in range(k):
                if (1 << u) > mask_right:
                    break
                if (mask_right & (1 << u)) == 0:
                    if (mask_mask & (1 << c)) != 0:
                        mask_left |= (1 << u)
                    c += 1
            joint_mask = mask_left | mask_right
            if answer[mask_left] and not answer[joint_mask]:
                answer[joint_mask] = True
                left[joint_mask] = mask_left
                right[joint_mask] = mask_right
                if joint_mask == ((1 << k) - 1):
                    return build_answer(k, masks, left, right)
    if answer[(1 << k) - 1]:
        return build_answer(k, masks, left, right)
    return False, None, None


def build_answer(k, masks, left, right):
    c = [-1] * k
    p = [-1] * k
    pos = (1 << k) - 1
    while not masks[pos]:
        for key, val in masks[right[pos]].items():
            c[key] = val[0]
            p[key] = val[1]
        pos = left[pos]
    for key, val in masks[pos].items():
        c[key] = val[0]
        p[key] = val[1]
    return True, c, p


def build_num_map(k, n, a):
    result = dict()
    for i in range(k):
        for j in range(n[i]):
            result[a[i][j]] = (i, j)
    return result


def find_cycle(i_origin, j_origin, i, j, k, n, a, sums, tsum, num_map, mask, path):
    if (mask & (1 << i)) != 0:
        if i == i_origin and j == j_origin:
            return True, mask, path
        else:
            return False, None, None
    mask |= (1 << i)
    a_needed = tsum - (sums[i] - a[i][j])
    if a_needed not in num_map:
        return False, None, None
    i_next, j_next = num_map[a_needed]
    path[i_next] = (a[i_next][j_next], i)
    return find_cycle(i_origin, j_origin, i_next, j_next, k, n, a, sums, tsum, num_map, mask, path)


def calc_sums(k, n, a):
    sums = [0] * k
    for i in range(k):
        for j in range(n[i]):
            sums[i] += a[i][j]
    asum = 0
    for i in range(k):
        asum += sums[i]
    return asum, sums


def main(n):
    if n < 1:
        n = 1
    k = n
    n_list = [i % 5 + 1 for i in range(k)]
    a = []
    for i in range(k):
        ni = n_list[i]
        ai = [(i + 1) * 10**6 + j * 7 for j in range(ni)]
        a.append(ai)
    total_sum, sums = calc_sums(k, n_list, a)
    target = total_sum // k if k > 0 else 0
    adjust = 0
    for i in range(k):
        for j in range(n_list[i]):
            if adjust < k:
                diff = target - sums[i]
                a[i][j] += diff
                total_sum, sums = calc_sums(k, n_list, a)
                adjust += 1
    answer, c, p = solve(k, n_list, a)
    if answer:
        for i in range(k):
            _ = c[i]
            _ = p[i] + 1
    else:
        pass


if __name__ == "__main__":
    main(4)