def main(n):
    # 映射 n 为输入规模
    # n: 约会次数
    if n <= 0:
        return

    # 确定性生成参数 s（等待时间），随 n 变化但可重复
    s = (n * 3) % 60

    # 生成 n 组时间 (h, m)，确保递增且在一天之内
    # 基本思路：从 0 分钟开始，每个时间间隔为 2 + 2*s 分钟，保证有足够空档
    times = []
    base = 0
    step = max(1, 2 + 2 * s)
    for i in range(n):
        t = base + i * step
        # 限制在一天内循环（确定性取模）
        t = t % (24 * 60)
        times.append(t)

    result = 0
    need = True

    if n == 1:
        if 0 + s + 1 <= times[0]:
            need = False

    for i in range(n - 1):
        if 0 + s + 1 <= times[0]:
            need = False
            break
        if times[i + 1] - times[i] >= 2 + 2 * s:
            result = times[i] + 1 + s
            break

    if result == 0 and need:
        result = times[n - 1] + 1 + s

    hour = result // 60
    minute = result % 60

    print(hour, minute)


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(5)