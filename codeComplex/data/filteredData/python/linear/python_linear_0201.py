import random

def main(n: int):
    # 随机生成 s（休息时间），范围可根据需要调整
    s = random.randint(0, 10)

    # 生成 n 个随机时间点（小时 0~23，分钟 0~59），按时间升序
    times = []
    for _ in range(n):
        h = random.randint(0, 23)
        m = random.randint(0, 59)
        times.append(60 * h + m)
    times.sort()

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
    # 示例：规模为 5
    main(5)