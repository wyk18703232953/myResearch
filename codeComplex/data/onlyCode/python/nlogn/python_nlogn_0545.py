n = int(input())
queen_x, queen_y = list(map(int, input().strip().split()))
king_x, king_y = list(map(int, input().strip().split()))
tar_x, tar_y = list(map(int, input().strip().split()))

min_x, max_x = sorted([king_x, tar_x])
min_y, max_y = sorted([king_y, tar_y])

if max_x > queen_x > min_x or max_y > queen_y > min_y:
    print("NO")
else:
    print("YES")
