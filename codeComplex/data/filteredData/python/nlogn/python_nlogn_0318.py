import random

def main(n: int):
    # 生成一个 0..n-1 的随机排列
    l = list(range(n))
    random.shuffle(l)

    parity = 0
    explore = set(l)
    while len(explore) > 0:
        x = explore.pop()
        tmp = x
        found = [x]
        while l[tmp] != x:
            tmp = l[tmp]
            found.append(tmp)
        for i in found[1:]:
            explore.remove(i)
        parity ^= (len(found) - 1) % 2

    if parity == n % 2:
        print("Petr")
    else:
        print("Um_nik")


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)