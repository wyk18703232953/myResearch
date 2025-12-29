from math import inf
from functools import lru_cache
import random


def to_bits(l):
    ans = 0
    for i in l:
        ans |= (1 << (i - 1))
    return ans


def main(n):
    # n: problem scale, we use it to generate test data
    # We will generate:
    #   n_users = n
    #   n_pizzas = n
    # ingredient indices in [1,10]
    # each user: random non-empty subset of ingredients
    # each pizza: random non-empty subset of ingredients and random cost

    max_ingredients = 10
    n_users = n
    n_pizzas = n

    # global-like structures recreated per call
    user_masks = [0 for _ in range(1 << max_ingredients)]
    pizzas = [[] for _ in range(1 << max_ingredients)]

    @lru_cache()
    def count_sat_users(mask):
        ans = 0
        cmask = mask
        while cmask:
            ans += user_masks[cmask]
            cmask = (cmask - 1) & mask
        return ans

    # -------- generate users --------
    for _ in range(n_users):
        # choose random non-empty subset of {1..10}
        k = random.randint(1, max_ingredients)
        a = random.sample(range(1, max_ingredients + 1), k)
        bits = to_bits(a)
        user_masks[bits] += 1

    # -------- generate pizzas --------
    for i in range(n_pizzas):
        c = random.randint(1, 1000)  # random cost
        k = random.randint(1, max_ingredients)
        a = random.sample(range(1, max_ingredients + 1), k)
        bits = to_bits(a)
        pizzas[bits].append((c, i + 1, bits))  # (price, index, mask)
        pizzas[bits].sort()
        while len(pizzas[bits]) > 2:
            pizzas[bits].pop()

    ans = (float(-inf), float(inf), -1, -1)

    # original loops use 0..(1<<9)-1, i.e. only 9 bits; we keep it
    for mask_F in range(1 << 9):
        for mask_S in range(1 << 9):
            if len(pizzas[mask_F]) and len(pizzas[mask_S]) and mask_F != mask_S:
                mask = mask_F | mask_S
                satisfied_users = count_sat_users(mask)

                f_pizza = pizzas[mask_F][0]
                s_pizza = pizzas[mask_S][0]

                summary_cost = f_pizza[0] + s_pizza[0]

                ans = max(
                    ans,
                    (
                        satisfied_users,
                        -summary_cost,
                        s_pizza[1],
                        f_pizza[1],
                    ),
                )

                # redundant brute in original code (kept to preserve structure)
                bmask = mask
                while bmask:
                    satisfied_users += user_masks[bmask]
                    bmask = (bmask - 1) & mask

            if len(pizzas[mask_F]) == 2:
                satisfied_users = count_sat_users(mask_F)
                f_pizza, s_pizza = pizzas[mask_F][0], pizzas[mask_F][1]
                summary_cost = f_pizza[0] + s_pizza[0]
                ans = max(
                    ans,
                    (
                        satisfied_users,
                        -summary_cost,
                        s_pizza[1],
                        f_pizza[1],
                    ),
                )

            if len(pizzas[mask_S]) == 2:
                satisfied_users = count_sat_users(mask_S)
                f_pizza, s_pizza = pizzas[mask_S][0], pizzas[mask_S][1]
                summary_cost = f_pizza[0] + s_pizza[0]
                ans = max(
                    ans,
                    (
                        satisfied_users,
                        -summary_cost,
                        s_pizza[1],
                        f_pizza[1],
                    ),
                )

    aans = [ans[2], ans[3]]
    aans.sort()
    print(*aans, sep=' ')


if __name__ == "__main__":
    # example run with n = 10
    main(10)