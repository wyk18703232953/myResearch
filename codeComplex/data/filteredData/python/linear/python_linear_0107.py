import random
import string

def main(n: int):
    # 生成测试数据：str1 长度为 n，str2 为随机长度（至少 1）
    # 字符集使用小写字母
    letters = string.ascii_lowercase

    # 保证 n >= 1，否则生成一个最小规模
    n = max(1, n)

    str1 = ''.join(random.choice(letters) for _ in range(n))
    str2_len = random.randint(1, max(1, n // 2))  # 自定义：str2 长度不超过 n/2
    str2 = ''.join(random.choice(letters) for _ in range(str2_len))

    # 以下为原逻辑移植
    lst = []
    lst_ans = []
    l_count = 0  # 原代码中未使用，但保留
    count = 0

    for i in str2:
        if count < 1:
            lst.append(i)
        else:
            break

    for i in str1:
        if count == 0:
            lst_ans.append(i)
            count += 1
        elif ord(i) < ord(lst[0]):
            lst_ans.append(i)
        else:
            lst_ans.append(lst[0])
            break
    else:
        lst_ans.append(lst[0])

    # 输出结果
    print('str1:', str1)
    print('str2:', str2)
    print('result:', ''.join(lst_ans))


if __name__ == "__main__":
    # 示例运行，可根据需要修改 n
    main(10)