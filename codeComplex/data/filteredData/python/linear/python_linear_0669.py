import random

def main(n: int):
    # 1. 生成测试数据
    # 生成 n 个距离（原程序中使用位移 << 1，即距离为偶数）
    # 为保持语义，这里生成原始“距离的一半”，再在逻辑里左移一位
    base_dis = [random.randint(1, 10) for _ in range(n)]  # 原始距离的一半
    # 生成 n 个地形字符
    choices = ['G', 'W', 'L']
    ter = ''.join(random.choice(choices) for _ in range(n))

    # 2. 原始逻辑（将 input() 替换为生成的数据）
    dis = list(map(lambda x: x << 1, base_dis))
    st, ans = 0, 0
    time = {'G': 5, 'W': 3, 'L': 1}
    delta = {'G': 1, 'W': 1, 'L': -1}
    hasWater = False
    convert = 0

    for i in range(n):
        st += dis[i] * delta[ter[i]]
        ans += dis[i] * time[ter[i]]
        if ter[i] == 'W':
            hasWater = True
        elif ter[i] == 'G':
            convert += dis[i]
        if st < 0:
            if hasWater:
                ans += (-st) * 3
            else:
                ans += (-st) * 5
            st = 0
        convert = min(convert, st // 2)

    ans -= 4 * convert
    ans -= 2 * (st // 2 - convert)

    # 输出最终结果
    print(ans // 2)


if __name__ == "__main__":
    # 示例运行：规模 n 可在此调整
    main(5)