import random
import string

def main(n: int):
    # 生成测试数据：长度为 n 的宝可梦类型串
    # 用小写字母表示不同类型，类型种类数为 min(26, max(1, n))
    k = min(26, max(1, n))
    types = string.ascii_lowercase[:k]
    pokemons = ''.join(random.choice(types) for _ in range(n))

    last = {}
    start_of_all = 0
    for i in range(n):
        ty = pokemons[i]
        if ty not in last:
            start_of_all = i
        last[ty] = 0

    minlen = 100001
    for i in range(n):
        ty = pokemons[i]
        last[ty] = i
        length = i + 1 - min(last.values())
        if i >= start_of_all and length < minlen:
            minlen = length

    print(minlen)


if __name__ == "__main__":
    # 示例：可在此处修改规模 n
    main(10)