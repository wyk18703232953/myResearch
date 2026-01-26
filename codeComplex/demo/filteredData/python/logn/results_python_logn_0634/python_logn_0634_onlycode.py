#!/usr/bin/env python
# coding: utf-8

# In[166]:


n, k = [int(i) for i in input().split()]


# In[167]:


def split_k(x):
    t = x + 1
    addition = t*(t+1)//2
    #print(addition)
    
    return(addition - (n- x -1) - k, n - x - 1 )


# In[170]:


j = 0

while split_k(j)[0] != 0:
    j += 1
    
print(split_k(j)[1])


# In[122]:


#polozh = [i + 1 for i in range(n)]
#vin = [-1 for i in range(1,n)]

#for j in range(n):
#    hod_list = polozh[0:n-j] + vin[0:j]
#    if sum(hod_list) == k:
#        break
#out = 0
#for i in hod_list:
#    if i == -1:
#        out +=1

