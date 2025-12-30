#!/usr/bin/env python3
import itertools
import random

# Initialize look-up tables
element_to_value = {
    'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10,
    'Na': 11, 'Mg': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20,
    'Sc': 21, 'Ti': 22, 'V': 23, 'Cr': 24, 'Mn': 25, 'Fe': 26, 'Co': 27, 'Ni': 28, 'Cu': 29, 'Zn': 30,
    'Ga': 31, 'Ge': 32, 'As': 33, 'Se': 34, 'Br': 35, 'Kr': 36, 'Rb': 37, 'Sr': 38, 'Y': 39, 'Zr': 40,
    'Nb': 41, 'Mo': 42, 'Tc': 43, 'Ru': 44, 'Rh': 45, 'Pd': 46, 'Ag': 47, 'Cd': 48, 'In': 49, 'Sn': 50,
    'Sb': 51, 'Te': 52, 'I': 53, 'Xe': 54, 'Cs': 55, 'Ba': 56, 'La': 57, 'Ce': 58, 'Pr': 59, 'Nd': 60,
    'Pm': 61, 'Sm': 62, 'Eu': 63, 'Gd': 64, 'Tb': 65, 'Dy': 66, 'Ho': 67, 'Er': 68, 'Tm': 69, 'Yb': 70,
    'Lu': 71, 'Hf': 72, 'Ta': 73, 'W': 74, 'Re': 75, 'Os': 76, 'Ir': 77, 'Pt': 78, 'Au': 79, 'Hg': 80,
    'Tl': 81, 'Pb': 82, 'Bi': 83, 'Po': 84, 'At': 85, 'Rn': 86, 'Fr': 87, 'Ra': 88, 'Ac': 89, 'Th': 90,
    'Pa': 91, 'U': 92, 'Np': 93, 'Pu': 94, 'Am': 95, 'Cm': 96, 'Bk': 97, 'Cf': 98, 'Es': 99, 'Fm': 100
}
value_to_element = {v: k for k, v in element_to_value.items()}


def generate_test_data(n):
    """
    根据规模 n 生成测试数据:
    - n: 初始原料总个数
    返回:
      products_start_str: 长度为 n 的原料元素列表
      products_end_str:   k 个产物元素列表（k 在内部决定）
    """
    # 限制 n 不要过大, 避免组合爆炸
    n = max(1, min(n, 12))

    # 随机选择不同元素做原料种类
    all_elements = list(element_to_value.keys())
    random.shuffle(all_elements)

    # 原料种类数不超过 n
    nr_ingredients = random.randint(1, min(5, n))
    ingredient_elems = all_elements[:nr_ingredients]

    # 为每种原料生成数量, 总和为 n
    # 先给每种至少 1 个
    counts = [1] * nr_ingredients
    remaining = n - nr_ingredients
    for _ in range(remaining):
        i = random.randint(0, nr_ingredients - 1)
        counts[i] += 1

    products_start_str = []
    for elem, cnt in zip(ingredient_elems, counts):
        products_start_str.extend([elem] * cnt)

    # 决定产物个数 k
    k = random.randint(1, min(4, n))

    # 随机构造 k 个合法产物：从 ingredient_elems 的值做线性组合
    ingredient_values = [element_to_value[e] for e in ingredient_elems]
    products_end_values = []
    for _ in range(k):
        coeffs = [random.randint(0, c) for c in counts]
        # 避免全 0
        if all(c == 0 for c in coeffs):
            coeffs[random.randint(0, nr_ingredients - 1)] = 1
        val = sum(coeffs[i] * ingredient_values[i] for i in range(nr_ingredients))
        # 映射到一个真实元素：用值对 100 取模再映射到 1..100
        mapped_val = (val % 100) or 100
        products_end_values.append(mapped_val)

    products_end_str = [value_to_element[v] for v in products_end_values]
    return products_start_str, products_end_str


def main(n):
    # 生成测试数据
    products_start_str, products_end_str = generate_test_data(n)

    # Translate elements to their values
    products_start = [element_to_value[elem] for elem in products_start_str]
    products_end = [element_to_value[elem] for elem in products_end_str]

    # k 为产物数量
    k = len(products_end)

    # Filter out duplicates; keep track of ingredient values and their number
    products_start.sort()
    ingredient_value = []
    ingredient_count = []
    for key, lst in itertools.groupby(products_start):
        ingredient_value.append(key)
        ingredient_count.append(len(list(lst)))
    nr_ingredients = len(ingredient_value)

    # Figure out the options for constructing the final products
    construction_options = [[] for _ in range(k)]
    for combination in itertools.product(*[range(l + 1) for l in ingredient_count]):
        value = sum(combination[i] * ingredient_value[i] for i in range(nr_ingredients))
        if value in products_end:
            for i in range(k):
                if products_end[i] == value:
                    construction_options[i].append(combination)

    # Do a depth-first search on the construction options for a possible solution
    solution = [None for _ in range(k)]

    def find_solution(used=None, nxt=0):
        if used is None:
            used = [0 for _ in range(nr_ingredients)]
        if nxt == k:
            return all(used[i] == ingredient_count[i] for i in range(nr_ingredients))
        else:
            for option in construction_options[nxt]:
                usage = [used[i] + option[i] for i in range(nr_ingredients)]
                if all(usage[i] <= ingredient_count[i] for i in range(nr_ingredients)):
                    possible = find_solution(usage, nxt + 1)
                    if possible:
                        solution[nxt] = option
                        return True
        return False

    possible = find_solution()

    # Print the answer
    if not possible:
        print("NO")
        return

    def combination_to_recipe(combination):
        recipe = []
        for i in range(nr_ingredients):
            for _ in range(combination[i]):
                recipe.append(value_to_element[ingredient_value[i]])
        return recipe

    print("YES")
    for i in range(k):
        recipe = combination_to_recipe(solution[i])
        print("%s->%s" % ("+".join(recipe), products_end_str[i]))


if __name__ == "__main__":
    # 示例: n = 10
    main(10)