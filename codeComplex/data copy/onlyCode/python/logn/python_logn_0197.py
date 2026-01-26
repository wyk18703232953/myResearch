def find(curr_pos, max_pos, curr_s, choose):
    if curr_pos == 0:
        if curr_s <= 0:
            return True
        else:
            return False
    if curr_pos == max_pos:
        low = 1
    else:
        low = 0
    high = 9
    for d in range(low, high + 1):
        curr_val = d * (10 ** curr_pos -  1)
        if curr_val + p[curr_pos - 1] < curr_s:
            continue
        choose[curr_pos] = d
        return find(curr_pos - 1, max_pos, curr_s - curr_val, choose)
    return False


n, s = map(int, input().split())
p = [0]
for i in range(1, 19):
    p.append(p[-1] + 9 * (10 ** i - 1))
choose = [0] * 19
ans = n + 1
for num_digit in range(1, 19):
    for i in range(1, num_digit + 1):
        choose[i] = 0
    if find(num_digit, num_digit, s, choose):
        res = 0
        for i in range(num_digit, -1, -1):
            res = res * 10 + choose[i]
        ans = min(ans, res)
        break
print(n - ans + 1)