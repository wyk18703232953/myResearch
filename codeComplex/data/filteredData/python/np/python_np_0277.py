import math

p2 = [1] * 64
for i in range(1, 64):
    p2[i] = p2[i - 1] * 2

def find_level(x, max_level):
    x0 = 1
    for i in range(max_level + 1):
        if (x - x0) % (x0 * 2) == 0:
            return i
        x0 *= 2
    return max_level

def move_U(number, max_level):
    cur_lv = find_level(number, max_level)
    if cur_lv == max_level:
        return number
    x0 = p2[cur_lv]
    seg = x0 * 2
    index = (number - x0) // seg
    return (x0 * 2) + (index // 2) * (seg * 2)

def move_L(number, max_level):
    cur_lv = find_level(number, max_level)
    if cur_lv == 0:
        return number
    x0 = p2[cur_lv]
    seg = x0 * 2
    index = (number - x0) // seg
    return (x0 // 2) + (index * 2) * (seg // 2)

def move_R(number, max_level):
    cur_lv = find_level(number, max_level)
    if cur_lv == 0:
        return number
    x0 = p2[cur_lv]
    seg = x0 * 2
    index = (number - x0) // seg
    return (x0 // 2) + (index * 2 + 1) * (seg // 2)

def move(s, num, max_level):
    if s == 'U':
        return move_U(num, max_level)
    if s == 'L':
        return move_L(num, max_level)
    return move_R(num, max_level)

def process(S, num, max_level):
    for s in S:
        num = move(s, num, max_level)
    return num

def main(n):
    if n < 1:
        return ""
    max_level = int(math.log2(n + 1)) - 1
    if max_level < 0:
        max_level = 0
    q = n
    lines = []
    for i in range(q):
        num = (i % n) + 1
        length = max_level + 1
        pattern = "ULR"
        S = "".join(pattern[j % 3] for j in range(length))
        res = process(S, num, max_level)
        lines.append(str(res))
    ans = "\n".join(lines)
    print(ans)
    return ans

if __name__ == "__main__":
    main(15)