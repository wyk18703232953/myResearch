import random

def main(n: int):
    # 3. 根据 n 生成测试数据：生成 n 个非负整数
    # 这里示例用 0~(2n) 的随机数，可按需要调整生成策略
    arr = [random.randint(0, 2 * n) for _ in range(n)]

    solved = False
    s = sum(arr)
    if s == 0:
        print("cslnb")
        solved = True

    if not solved:
        n_num = {}

        for item in arr:
            if item in n_num:
                n_num[item] += 1
            else:
                n_num[item] = 1

        if 0 in n_num and n_num[0] >= 2:
            print('cslnb')
            solved = True

        if not solved:
            for key in n_num.keys():
                if n_num[key] >= 3:
                    print("cslnb")
                    solved = True

            ind_pairs = []
            if not solved:
                for key in n_num.keys():
                    if n_num[key] == 2:
                        ind_pairs.append(key)

                if len(ind_pairs) >= 2:
                    print("cslnb")
                    solved = True
                elif len(ind_pairs) == 1 and (ind_pairs[0] - 1) in n_num:
                    print("cslnb")
                    solved = True
                else:
                    sum_targ = n * (n - 1) // 2
                    dif_sum = s - sum_targ
                    if dif_sum % 2 == 0:
                        print("cslnb")
                    else:
                        print("sjfnb")


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)