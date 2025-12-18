import sys
from collections import defaultdict
# import logging
# logging.root.setLevel(level=logging.INFO)


exist_num,new_width = map(int,sys.stdin.readline().strip().split())
buildings = []
for _ in range(exist_num):
    center, width = map(int,sys.stdin.readline().strip().split())
    buildings.append((center-width/2,center+width/2))
buildings.sort()
possible_loc = 2
for left,right in zip(buildings,buildings[1:]):
    gap=right[0] - left[1]
    if gap == new_width:
        possible_loc += 1
    elif gap > new_width:
        possible_loc += 2
# print(buildings)
print(possible_loc)

