import math

types_of_toy , toy_pair = map(int,input().split())

if(toy_pair <= types_of_toy ):
    print(math.floor( ( toy_pair - 1 ) /2))
elif( toy_pair <= 2*types_of_toy - 1):
    print(math.floor( ( types_of_toy +1 -(toy_pair - types_of_toy) )/ 2)) 
else:
    print(0)


