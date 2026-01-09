import math

def minPut(n):
    return math.ceil((-1 + math.sqrt(1 - 4 * (-n * 2))) / 2)

def nCandies(n):
    return int(n * (n + 1) / 2)

def core_logic(actions, candies):
    put = minPut(candies)
    putCandies = nCandies(put)
    eat = putCandies - candies
    while put + eat < actions:
        eat += put + 1
        put += 1
    return eat

def main(n):
    actions = 2 * n
    candies = n
    result = core_logic(actions, candies)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)