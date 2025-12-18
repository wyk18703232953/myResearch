n = input()
seat_rows = [int(x) for x in input().strip().split()]
aliens = input().strip()

eldian = "0"
marleyan = "1"

empty = sorted(enumerate(seat_rows), key=lambda x: x[1], reverse=True)
non_empty = []

result = []
for alien in aliens:
    if alien == eldian:
        row = empty.pop()
        non_empty.append(row)
    else:
        row = non_empty.pop()

    result.append(row[0] + 1)

print(' '.join(map(str, result)))