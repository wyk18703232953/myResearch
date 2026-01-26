# cook your dish here
import math
 
no_of_moves , no_of_candy = map(int,input().split())
 
total_candy = now_candy = 1 
now_moves = 1 


if(no_of_moves == 0 or (no_of_moves ==1 and no_of_candy == 1)):
    print(0)
else:
    while True:
    
        now_candy = now_candy + 1 
        total_candy += now_candy 
        now_moves += 1 
        if(total_candy -(no_of_moves - now_moves) == no_of_candy):
            break 
    
    print(no_of_moves - now_moves)