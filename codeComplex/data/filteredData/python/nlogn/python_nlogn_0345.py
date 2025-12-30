import random
import string

def comp(arr):
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if arr[j] in arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr[::-1]

def generate_test_data(n):
    # 生成 n 个随机字符串，长度在 1~10 之间
    res = []
    for _ in range(n):
        length = random.randint(1, 10)
        s = ''.join(random.choices(string.ascii_lowercase, k=length))
        res.append(s)
    return res

def main(n):
    arr = generate_test_data(n)
    t = n

    arr = comp(arr)

    ans = 1
    for j in range(0, t - 1):
        if arr[j] not in arr[j + 1]:
            ans = 0
            break

    if ans == 0:
        print("NO")
    else:
        print("YES")
        for j in arr:
            print(j)

if __name__ == "__main__":
    # 示例：规模为 5
    main(5)