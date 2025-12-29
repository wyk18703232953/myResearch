import random

def main(n):
    # 初始字典
    my_list = {
        "purple": "Power",
        "green": "Time",
        "blue": "Space",
        "orange": "Soul",
        "yellow": "Mind",
        "red": "Reality"
    }

    # 生成测试数据：从 key 中随机选择要删除的 n 个（可能重复）
    keys = list(my_list.keys())
    for _ in range(n):
        key_to_remove = random.choice(keys)
        # 若键仍存在则删除
        my_list.pop(key_to_remove, None)

    # 输出结果
    print(len(my_list))
    for key in my_list:
        print(my_list[key])


if __name__ == "__main__":
    # 示例：规模为 3，可按需修改
    main(3)