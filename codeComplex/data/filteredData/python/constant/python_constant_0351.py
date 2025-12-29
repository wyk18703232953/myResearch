import random

def main(n: int):
    # 原始字典
    d = {
        "purple": "Power",
        "green": "Time",
        "blue": "Space",
        "orange": "Soul",
        "red": "Reality",
        "yellow": "Mind",
    }

    # 生成测试数据：从已有颜色中随机删除 n 个（不超过字典长度）
    n = min(n, len(d))
    colors = list(d.keys())
    remove_keys = random.sample(colors, n)

    # 模拟原逻辑：依次 pop 掉生成的测试颜色
    for key in remove_keys:
        d.pop(key, None)

    # 输出结果（与原程序行为一致）
    print(len(d))
    for v in d.values():
        print(v)


if __name__ == "__main__":
    # 示例：可根据需要调整 n
    main(3)