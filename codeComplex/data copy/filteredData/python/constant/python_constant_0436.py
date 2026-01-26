import math

def main(n):
    types_of_toy = n
    toy_pair = n // 2 + 1
    if toy_pair <= types_of_toy:
        result = math.floor((toy_pair - 1) / 2)
    elif toy_pair <= 2 * types_of_toy - 1:
        result = math.floor((types_of_toy + 1 - (toy_pair - types_of_toy)) / 2)

    else:
        result = 0
    # print(result)
    pass
if __name__ == "__main__":
    main(10)