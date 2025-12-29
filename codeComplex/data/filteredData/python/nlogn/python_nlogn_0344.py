import random
import string

def generate_test_data(n):
    """
    生成规模为 n 的测试数据列表 arr
    构造方式：从短字符串开始，每个后续字符串在前一个字符串基础上随机扩展，
    从而保证存在一个按长度递增、且前缀包含关系较多的集合，适合原逻辑测试。
    """
    arr = []
    # 基础字符串，避免空串
    base = ''.join(random.choices(string.ascii_lowercase, k=1))
    arr.append(base)

    for _ in range(1, n):
        # 随机选择已有字符串作为前缀
        prefix = random.choice(arr)
        # 在前缀基础上增加 1~3 个随机字符
        extra_len = random.randint(1, 3)
        extra = ''.join(random.choices(string.ascii_lowercase, k=extra_len))
        new_str = prefix + extra
        arr.append(new_str)

    return arr

def main(n):
    # 生成测试数据
    arr = generate_test_data(n)

    # 原始逻辑
    arr.sort(key=lambda x: len(x))
    flag = False
    for i in range(n - 2, -1, -1):
        if arr[i] not in arr[i + 1]:
            flag = True
            break

    if flag:
        print("NO")
    else:
        print("YES")
        for s in arr:
            print(s)


if __name__ == "__main__":
    # 示例：n = 5，可按需要修改
    main(5)