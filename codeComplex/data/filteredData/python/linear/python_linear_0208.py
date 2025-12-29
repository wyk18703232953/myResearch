from itertools import count
import random

def main(n):
    # 规模参数 n：生成 n 个随机时间点，以及随机的安全间隔 s（分钟）
    # 为了可重复，可根据需要固定随机种子
    random.seed(0)

    # 生成随机的安全间隔 s，范围 0~59 分钟
    s = random.randint(0, 59)

    # 生成 n 个随机时间（分钟数），范围 0~1439，即一天以内
    times = []
    for _ in range(n):
        h = random.randint(0, 23)
        m = random.randint(0, 59)
        times.append(h * 60 + m)

    # 排序原有时间
    times.sort()

    # 原逻辑：从 t=0 开始找一个时间，使得与所有已有 times 的差值都大于 s
    for t in count():
        if all(abs(u - t) > s for u in times):
            h, m = divmod(t, 60)
            print(h, m)
            break

if __name__ == "__main__":
    # 示例调用：n 可根据需要调整
    main(5)