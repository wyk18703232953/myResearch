import random
import string

def generate_test_data(n: int):
    """
    生成 n 个字符串测试数据。
    为了尽量满足“子串链”的需求，构造方式为：
    s0 是随机字符串，后面的 si 在前一个字符串基础上随机插入或追加字符。
    """
    if n <= 0:
        return []

    # 初始字符串长度在 [1, 5] 之间
    base_len = random.randint(1, 5)
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(base_len))
    arr = [s]

    for _ in range(1, n):
        # 在前一个字符串基础上插入/追加 1~3 个字符
        cur = arr[-1]
        cur_list = list(cur)
        add_len = random.randint(1, 3)
        for _ in range(add_len):
            ch = random.choice(string.ascii_lowercase)
            pos = random.randint(0, len(cur_list))  # 可在任意位置插入
            cur_list.insert(pos, ch)
        arr.append(''.join(cur_list))

    # 为了增加随机性，把顺序打乱，让算法去排序
    random.shuffle(arr)
    return arr

def main(n: int):
    # 生成 n 个测试字符串
    arr = generate_test_data(n)

    # 按长度排序
    arr = sorted(arr, key=lambda x: len(x))

    # 校验每个字符串是否为下一个字符串的子串
    for i in range(n - 1):
        if arr[i] not in arr[i + 1]:
            print('NO')
            return

    print('YES')
    for pal in arr:
        print(pal)


if __name__ == "__main__":
    # 示例：可在这里指定规模
    main(5)