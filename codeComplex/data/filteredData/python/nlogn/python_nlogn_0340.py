import random
import string

def comp(arr):    
    for i in range(len(arr) - 1):    
        for j in range(0, len(arr) - i - 1):
            if arr[j] in arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr[::-1]


def generate_test_data(n):
    # 生成一个“链式包含”的字符串列表：
    # s0 in s1 in s2 ... in s_{n-1}
    arr = []
    # 从一个随机基础串开始
    base_len = random.randint(1, 5)
    base = ''.join(random.choices(string.ascii_lowercase, k=base_len))
    arr.append(base)
    cur = base
    for _ in range(1, n):
        # 在当前串左右或中间拼接随机串，保证前一个是后一个的子串
        extra_len = random.randint(1, 5)
        extra = ''.join(random.choices(string.ascii_lowercase, k=extra_len))
        pos = random.randint(0, len(cur))
        new_s = cur[:pos] + extra + cur[pos:]
        arr.append(new_s)
        cur = new_s
    # 打乱顺序以测试排序逻辑
    random.shuffle(arr)
    return arr


def main(n):
    # 生成规模为 n 的测试数据
    arr = generate_test_data(n)

    # 调用原逻辑
    sorted_arr = comp(arr)

    ans = 1
    for j in range(0, n - 1):
        if sorted_arr[j] not in sorted_arr[j + 1]:
            ans = 0
            break

    if ans == 0:
        print("NO")
    else:
        print("YES")
        for s in sorted_arr:
            print(s)


if __name__ == "__main__":
    # 示例：调用 main(5) 进行测试
    main(5)