# cook your dish here

def main():
    A,B = list(map(int, input().strip().split()))
    yellow,green,blue = list(map(int, input().strip().split()))
    
    yelreq = 0
    blureq = 0
    
    # for yellow balls
    yelreq = 2*yellow
    
    # green balls 
    yelreq += green
    blureq += green
    
    # blue balls 
    blureq += 3*blue
    
    reqs = 0
    if A<yelreq:
        reqs += yelreq - A
    if B<blureq:
        reqs += blureq - B

    print(reqs)
    
main()
