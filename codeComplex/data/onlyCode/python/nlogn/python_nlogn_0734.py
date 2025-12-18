import math

n, m, k = list(map(lambda i: int(i), input().split(sep=' ')))
p = list(map(lambda i: int(i), input().split(sep=' ')))
p.sort()
page_max = k
action_count = 0
index = 0
while index < m:
    while index < m and p[index] <= page_max:
        count = 0
        while index < m and p[index] <= page_max:
            index += 1
            count += 1
        if count > 0:
            action_count += 1
        page_max += count

    pc = 1 if index >= m else math.ceil((p[index] - page_max) / k)
    page_max += k * pc

print(action_count)
