import random
import string

def main(n: int):
    # 生成测试数据：两个长度为 n 的小写字母串
    # 保证 second 是 first 经过若干相邻交换后得到的版本（这样通常有解）
    first = [random.choice(string.ascii_lowercase) for _ in range(n)]
    second = first[:]  # 从 first 拷贝
    # 随机执行若干次相邻交换来生成 second
    for _ in range(n):  # 做 n 次随机相邻交换
        if n <= 1:
            break
        i = random.randint(0, n - 2)
        second[i], second[i + 1] = second[i + 1], second[i + 1] = second[i + 1], second[i]

    # 下面是原逻辑（移除 input，对 first 和 second 使用上面生成的测试数据）
    swap = []
    can = True

    for i in range(n):
        if first[i] != second[i]:
            cont = -1
            for j in range(i, n):
                if first[j] == second[i]:
                    cont = j
                    break

            if cont != -1:
                for j in range(cont, i, -1):
                    first[j], first[j - 1] = first[j - 1], first[j]
                    swap.append(j)
            else:
                can = False
                break

    if can:
        print(len(swap))
        print(*swap, end=' ')
    else:
        print(-1)


# 示例：直接运行时可以调用 main(5) 做一次简单测试
if __name__ == "__main__":
    main(5)