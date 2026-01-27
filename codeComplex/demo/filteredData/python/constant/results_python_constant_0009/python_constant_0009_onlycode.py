a, v = list(map(int, input().split(" ")))
l, d, w = list(map(int, input().split(" ")))
 
if(v <= w or w * w > 2 * a * d):
    if(v * v > 2 * a * l):
        print((2 * l / a) ** 0.5)
    else:
        print(l / v + v / 2 / a)
else:
    u = (w * w / 2 + a * d) ** 0.5
    if(u > v):
        m =  v / a + (v - w) / a + (d - (v * v / 2 / a) - (v * v - w * w) / 2 / a) / v
    else:
        m = (2 * u - w) / a
        
    if(v * v > 2 * a * (l - d + w * w / 2 / a)):
        print(m - w / a + (2 * (l - d + (w * w / 2 / a)) / a) ** 0.5)
    else:
        print(m - w / a + (l - d + w * w / 2 / a) / v + v / 2 / a)