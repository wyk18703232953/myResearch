point = {}

def main(n):
    point = {}
    # 确定性生成 n 个区间 [l, r]
    # 这里设定：l = i, r = i + (i % 5) + 1，保证 r >= l
    for i in range(n):
        l = i
        r = i + (i % 5) + 1
        r += 1
        if l not in point:
            point[l] = 0
        if r not in point:
            point[r] = 0
        point[l] += 1
        point[r] -= 1

    line = []
    for key in point:
        line.append((key, point[key]))
    line.sort()
    ans = [0] * (n + 1)

    last_index = 0
    last_value = 0

    for index, value in line:
        ans[last_value] += index - last_index
        last_index = index
        last_value += value

    # 为了时间复杂度实验，返回结果而不是打印
    return ans[1:]


if __name__ == "__main__":
    # 示例调用，规模可按需修改
    res = main(10)
    print(*res)