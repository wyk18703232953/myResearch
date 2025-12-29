from sys import stdout
import random

def solve(n, t, tasks):
    lo = 0
    hi = n

    res = []
    curr_res = 0

    tasks.sort(key=lambda x: x[1])

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        # check if we can make mid.
        valid_tasks = []
        for i in tasks:
            if i[0] >= mid:
                valid_tasks.append(i)

        can_do = False

        curr_sum = 0
        total_used = 0
        r = []
        for i in valid_tasks:
            curr_sum += i[1]
            total_used += 1
            r.append(i[2])
            if curr_sum > t:
                break
            elif total_used >= mid:
                can_do = True
                curr_res = mid
                res = r
                break
        if can_do:
            lo = mid + 1
        else:
            hi = mid - 1
    return curr_res, res


def main(n):
    # 根据规模 n 生成测试数据
    # 生成总时间限制 t
    # 这里简单设置为 n * 10，您可以根据需要调整
    t = n * 10

    tasks = []
    idx = 1
    for _ in range(n):
        # 随机生成 a_i 和 t_i
        # a_i: 任务“价值”或要求的最小数量（原逻辑中需 >= mid）
        # t_i: 完成该任务的时间
        a_i = random.randint(1, n)
        t_i = random.randint(1, 10)
        tasks.append((a_i, t_i, idx))
        idx += 1

    res, res_arry = solve(n, t, tasks)
    print(res)
    print(res)
    stdout.write(" ".join(map(str, res_arry)))
    stdout.write("\n")


if __name__ == "__main__":
    # 示例：调用 main(5) 进行测试
    main(5)