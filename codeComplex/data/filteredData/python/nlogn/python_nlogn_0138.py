import random

def main(n):
    # 生成测试数据：
    # n_extnson: 插线板数量
    # n_dvics: 设备数量
    # n_sokts: 初始插座数量
    # extensions: 每个插线板提供的插孔数（至少2，避免无效插线板）
    #
    # 这里用 n 作为规模，控制 n_extnson 和 n_dvics 的大小
    random.seed(0)

    n_extnson = max(1, n // 2)          # 插线板数量
    n_dvics = max(1, n)                # 设备数量
    n_sokts = max(1, n // 3)           # 初始插座数量

    # 每个插线板提供 2~5 个插孔
    extensions = [random.randint(2, 5) for _ in range(n_extnson)]

    # 算法主体
    extensions.sort(reverse=True)
    devices_left = n_dvics - n_sokts
    extnson_used = 0
    i = 0

    while devices_left > 0 and n_extnson > 0 and i < len(extensions):
        devices_left += 1
        extnson_siez = extensions[i]
        devices_left -= extnson_siez
        extnson_used += 1
        n_extnson -= 1
        i += 1

    if devices_left > 0:
        print(-1)
    else:
        print(extnson_used)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)