def find(moves, candiesAtTheEnd):
    start = 0
    end = moves - 1
    while True:
        mid = ((end - start + 1) // 2) + start
        pluses = moves - mid
        minuses = mid
        result = ((pluses + 1) / 2) * pluses
        result = result - minuses
        if result == candiesAtTheEnd:
            return minuses
        elif result > candiesAtTheEnd:
            start = mid

        else:
            end = mid

def main(n):
    moves = max(1, n)
    candiesAtTheEnd = moves // 2
    result_final = find(moves, candiesAtTheEnd)
    # print(result_final)
    pass
if __name__ == "__main__":
    main(10)