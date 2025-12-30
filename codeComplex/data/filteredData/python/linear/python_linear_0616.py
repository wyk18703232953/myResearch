import random

def main(n):
    # 生成测试数据：
    # a 为 [1..n] 的一个随机排列
    # b 为 [1..n] 的一个随机排列
    a = list(range(1, n + 1))
    b = list(range(1, n + 1))
    random.shuffle(a)
    random.shuffle(b)

    # 与原逻辑一致
    max_val = 2 * 10**5
    pos_of = [-1] * (max_val + 1)

    for i, ele in enumerate(a):
        pos_of[ele] = i + 1

    current_pos = 0
    ans = []
    for x in b:
        if pos_of[x] > current_pos:
            ans.append(pos_of[x] - current_pos)
            current_pos = pos_of[x]
        else:
            ans.append(0)

    print(' '.join(map(str, ans)))


if __name__ == "__main__":
    # 示例：n 可以根据需要修改
    main(10)