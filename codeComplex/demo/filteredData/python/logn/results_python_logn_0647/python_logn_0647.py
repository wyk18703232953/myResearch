def find(moves, candiesAtTheEnd):
    result = -1
    start = 0
    end = moves - 1
    while result != candiesAtTheEnd and start <= end:
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
    return -1

def main(n):
    moves = n
    candiesAtTheEnd = (n * (n + 1)) // 4
    result_final = find(moves, candiesAtTheEnd)
    print(result_final)

if __name__ == "__main__":
    main(10)