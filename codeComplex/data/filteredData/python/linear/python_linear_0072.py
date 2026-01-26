def main(n):
    # 在原程序中，第一行输入为 n, s，这里将 s 定义为与 n 线性相关的确定性值
    s = 2 * n + 5
    mins = s
    my_dict = {}
    mylist = []

    # 原程序中接下来读取 n 行 (person, floor)，这里用确定性规则生成
    # 生成方式：person = i，floor = n - i，对 i 从 1 到 n
    remaining = n
    i = 1
    while remaining:
        person = i
        floor = n - i
        mylist.append(person + floor)
        remaining -= 1
        i += 1

    val = max(mylist) if mylist else mins
    if val < mins:
        # print(mins)
        pass

    else:
        # print(val)
        pass
if __name__ == "__main__":
    main(5)