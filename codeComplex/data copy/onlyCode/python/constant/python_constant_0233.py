def req_num(a, b, x, y, z):
    req_a = (x * 2) + y
    req_b = (z * 3) + y
    if (req_a - a) <= 0:
        ans_a = 0
    else:
        ans_a = req_a - a
    if (req_b - b) <= 0:
        ans_b = 0
    else:
        ans_b = req_b - b
    return ans_a + ans_b

a, b = list(map(int, input().strip().split()))
x, y, z = list(map(int, input().strip().split()))
print(req_num(a, b, x, y, z))
