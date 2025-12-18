n = int(input())
 
one_seat = []
 
two_seats = []
 
j = 1
 
for item in input().split():
    two_seats.append((int(item), j))
    j += 1
 
two_seats.sort(key=lambda x: -x[0])
 
for person in input():
    if person == '0':
        q = two_seats.pop()
        print(q[1], end=' ')
        one_seat.append(q)
    else:
        print(one_seat.pop()[1], end=' ')
 	 	 	 	  		    					  			   	