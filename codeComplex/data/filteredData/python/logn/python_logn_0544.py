import bisect
import random

def solve_k(k: int) -> str:
    xzy = [
        10,
        190,
        2890,
        38890,
        488890,
        5888890,
        68888890,
        788888890,
        8888888890,
        98888888890,
        1088888888890,
        11888888888890,
    ]
    digits = bisect.bisect_left(xzy, k)
    if k == 10:
        return "1"
    elif k > 10:
        apu = k - xzy[digits - 1]
        modulo = apu % (digits + 1)
        dlj = apu // (digits + 1)
        output = 10 ** digits + dlj
        list1 = [ch for ch in str(output)]
        return list1[modulo]
    else:
        return str(k)

def main(n: int):
    # 根据规模 n 生成 n 个测试数据 k，并输出结果
    # 这里生成 1 到 n 之间的随机整数作为测试数据
    random.seed(0)
    for _ in range(n):
        k = random.randint(1, max(20, n * 2))
        print(f"k={k} -> {solve_k(k)}")

if __name__ == "__main__":
    # 示例：当作为脚本运行时，可以手动设置规模
    main(10)