f, d, s = [int(i) for i in input().split()]
filters = [int(i) for i in input().split()]
filters.sort(reverse=True)

freeSockets = s
usedFilters = 0
for i in range(len(filters)):
    if freeSockets >= d:
        break
    usedFilters += 1
    freeSockets += filters[i]-1

if freeSockets >= d:
    print(usedFilters)
else:
    print(-1)

