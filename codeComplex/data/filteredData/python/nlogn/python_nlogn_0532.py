import random

def main(n):
    # 生成规模为 n 的测试数据
    # 随机生成 k 和数组 v
    # 保证 k > 0 且不过大
    k = random.randint(1, 10**9)
    v = [random.randint(0, 10**9) for _ in range(n)]

    d = {}
    ans = 0

    for x in v:
        num_d, mod_k = len(str(x)), x % k
        d.setdefault(num_d, {}).setdefault(mod_k, []).append(x)

    for x in v:
        num_d, mod_k = len(str(x)), x % k
        for add, mods in d.items():
            val_mod = (mod_k * pow(10, add, k)) % k
            need_mod = (k - val_mod) % k
            ans += len(mods.get(need_mod, []))
            if need_mod == mod_k and add == num_d:
                ans -= 1

    print(ans)


if __name__ == "__main__":
    # 可在此修改 n 的测试规模
    main(10)