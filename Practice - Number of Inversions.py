#!/usr/bin/env python
# coding: utf-8

# In[1]:


## IMPLEMENTATION
## function call for mergeProcedures
##TC T(n/2)+T(n/2) + N -> 2T(n/2)+N
def mergeProcedure(arr,i,mid,j):
    
    ## get the number of left subarray
    n1 = mid - i + 1
    ## get the number of right subarray
    n2 = j - mid
    
    ## new array
    ## initialise the leftsubarray, rightsubarray
    leftsubarray,rightsubarray = [0] * n1, [0] * n2
    
    ## store left side tree into leftsubarray
    for m in range(n1):
        leftsubarray[m] = arr[m+i]
    ## store right side tree into rightsubarray
    for n in range(n2):
        rightsubarray[n] = arr[mid+1+n]
    
    p = 0
    q = 0
    k = i
    inv_count = 0
    
    while p < n1 and q < n2:
        
        if leftsubarray[p] <= rightsubarray[q]:
            
            arr[k] = leftsubarray[p]
            p += 1
            k += 1
        else:
            arr[k] = rightsubarray[q]
            inv_count += len(leftsubarray) - p
            k += 1
            q += 1
    
    while p < n1:
        arr[k] = leftsubarray[p]
        k += 1
        p += 1
        
    while q < n2:
        arr[k] = rightsubarray[q]
        k += 1
        q += 1
    
    return inv_count

## function call for number of Inversions
def numInversions(arr,i,j):
    
    invt_count = 0
    if i < j:
        mid = i + (j-i)//2
        invt_count += numInversions(arr,i, mid)
        invt_count += numInversions(arr,mid+1,j)
        invt_count += mergeProcedure(arr,i,mid,j)
    return invt_count
    
## DRIVER CODE
arr = [70,50,60,10,20,30,80,15]
i = 0
j = len(arr) - 1
result = numInversions(arr, i, j)
print(result)


# In[ ]:




