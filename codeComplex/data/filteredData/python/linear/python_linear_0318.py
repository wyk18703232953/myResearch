import random

def main(n: int):
    # 预定义所有尺码
    key = []
    for i in ['S', 'M', 'L']:
        for j in range(4):
            key.append(j * 'X' + i)

    # 随机生成测试数据：两个长度为 n 的尺寸序列
    prev_list = [random.choice(key) for _ in range(n)]
    now_list = [random.choice(key) for _ in range(n)]

    # 计数
    prev = dict().fromkeys(key, 0)
    now = dict().fromkeys(key, 0)
    for s in prev_list:
        prev[s] += 1
    for s in now_list:
        now[s] += 1

    # 抵消相同的尺码
    for k in key:
        temp = min(prev[k], now[k])
        prev[k] -= temp
        now[k] -= temp

    # 计算需要更换的数量（即剩余 now 中的数量之和）
    ans = 0
    for k in key:
        ans += now[k]

    print(ans)


if __name__ == "__main__":
    # 示例运行：可以自行修改 n 测试规模
    main(10)