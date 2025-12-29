import random

def main(n):
    # 根据规模 n 生成测试数据，这里生成 n 个 1~10 的随机整数
    data = [random.randint(1, 10) for _ in range(n)]

    a = iter(data)
    prev_type = 3
    prev_res = 2
    try:
        curr_a = next(a)
    except StopIteration:
        # 无数据时按照原代码逻辑，相当于循环没有进入且无输出
        print('-1')
        return

    res = []
    for _ in range(1):
        for next_a in a:
            if next_a > curr_a:
                if prev_type == 1 or prev_res == 1:
                    prev_res += 1
                    if prev_res == 5:
                        break
                else:
                    prev_res = 1
                prev_type = 1
            elif next_a < curr_a:
                if prev_type == 2 or prev_res == 5:
                    prev_res -= 1
                    if prev_res == 1:
                        break
                else:
                    prev_res = 5
                prev_type = 2
            else:
                if prev_type == 1:
                    prev_res += 1
                elif prev_type == 2:
                    prev_res -= 1
                elif prev_res != 2:
                    prev_res = 2
                else:
                    prev_res = 3
                prev_type = 3
            res.append(prev_res)
            curr_a = next_a
        else:
            if prev_type == 1:
                res.append(prev_res + 1)
            elif prev_type == 2:
                res.append(prev_res - 1)
            elif prev_res != 1:
                res.append(1)
            else:
                res.append(2)
            print(*res)
            break
    else:
        print('-1')


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)