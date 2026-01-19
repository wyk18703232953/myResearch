#!/usr/bin/env python3 

import itertools

element_to_value = {
  'H':1, 'He':2, 'Li':3, 'Be':4, 'B':5, 'C':6, 'N':7, 'O':8, 'F':9, 'Ne':10,
  'Na':11, 'Mg':12, 'Al':13, 'Si':14, 'P':15, 'S':16, 'Cl':17, 'Ar':18, 'K':19, 'Ca':20,
  'Sc':21, 'Ti':22, 'V':23, 'Cr':24, 'Mn':25, 'Fe':26, 'Co':27, 'Ni':28, 'Cu':29, 'Zn':30,
  'Ga':31, 'Ge':32, 'As':33, 'Se':34, 'Br':35, 'Kr':36, 'Rb':37, 'Sr':38, 'Y':39, 'Zr':40,
  'Nb':41, 'Mo':42, 'Tc':43, 'Ru':44, 'Rh':45, 'Pd':46, 'Ag':47, 'Cd':48, 'In':49, 'Sn':50,
  'Sb':51, 'Te':52, 'I':53, 'Xe':54, 'Cs':55, 'Ba':56, 'La':57, 'Ce':58, 'Pr':59, 'Nd':60,
  'Pm':61, 'Sm':62, 'Eu':63, 'Gd':64, 'Tb':65, 'Dy':66, 'Ho':67, 'Er':68, 'Tm':69, 'Yb':70,
  'Lu':71, 'Hf':72, 'Ta':73, 'W':74, 'Re':75, 'Os':76, 'Ir':77, 'Pt':78, 'Au':79, 'Hg':80,
  'Tl':81, 'Pb':82, 'Bi':83, 'Po':84, 'At':85, 'Rn':86, 'Fr':87, 'Ra':88, 'Ac':89, 'Th':90,
  'Pa':91, 'U':92, 'Np':93, 'Pu':94, 'Am':95, 'Cm':96, 'Bk':97, 'Cf':98, 'Es':99, 'Fm':100
}
value_to_element = dict()
for (element, value) in element_to_value.items():
  value_to_element[value] = element

def solve_instance(n, k, products_start_str, products_end_str):
  products_start = [element_to_value[elem] for elem in products_start_str]
  products_end = [element_to_value[elem] for elem in products_end_str]

  products_start.sort()
  ingredient_value = []
  ingredient_count = []
  for (key, lst) in itertools.groupby(products_start):
    ingredient_value.append(key)
    ingredient_count.append(len(list(lst)))
  nr_ingredients = len(ingredient_value)

  construction_options = [[] for _ in range(k)]
  for combination in itertools.product(*[range(l+1) for l in ingredient_count]):
    value = sum(combination[i] * ingredient_value[i] for i in range(nr_ingredients))
    if value in products_end:
      for i in range(k):
        if products_end[i] == value:
          construction_options[i].append(combination)

  solution = [None for _ in range(k)]

  def find_solution(used=None, nxt=0):
    if used is None:
      used_local = [0 for _ in range(nr_ingredients)]
    else:
      used_local = used
    if nxt == k:
      return all(used_local[i] == ingredient_count[i] for i in range(nr_ingredients))
    else:
      for option in construction_options[nxt]:
        usage = [used_local[i] + option[i] for i in range(nr_ingredients)]
        if all(usage[i] <= ingredient_count[i] for i in range(nr_ingredients)):
          possible = find_solution(usage, nxt + 1)
          if possible:
            solution[nxt] = option
            return True
    return False

  possible = find_solution()

  if not possible:
    return ["NO"]

  def combination_to_recipe(combination):
    recipe = []
    for i in range(nr_ingredients):
      for _ in range(combination[i]):
        recipe.append(value_to_element[ingredient_value[i]])
    return recipe

  output_lines = []
  output_lines.append("YES")
  for i in range(k):
    recipe = combination_to_recipe(solution[i])
    output_lines.append("%s->%s" % ("+".join(recipe), products_end_str[i]))
  return output_lines

def generate_data(n):
  if n < 1:
    n = 1
  k = n
  start_len = 2 * n
  elements = list(element_to_value.keys())
  m = len(elements)
  products_start_str = [elements[i % m] for i in range(start_len)]
  products_end_values = []
  for i in range(k):
    base = (i + 1)
    val = (base * (base + 1)) // 2
    val = (val % 100) + 1
    products_end_values.append(val)
  products_end_str = [value_to_element[v] for v in products_end_values]
  return n, k, products_start_str, products_end_str

def main(n):
  n_in, k, products_start_str, products_end_str = generate_data(n)
  lines = solve_instance(n_in, k, products_start_str, products_end_str)
  for line in lines:
    print(line)

if __name__ == "__main__":
  main(5)