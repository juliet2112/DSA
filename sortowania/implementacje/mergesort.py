def merge(l,mid,r,T):
    l_n = mid - l + 1
    r_n = r - mid
    
    left = T[l:l+l_n]
    right = T[mid+1:mid+1+r_n]

    i,j = 0,0
    k = l
    while i < l_n and j < r_n:
        if(left[i]<=right[j]):
            T[k]=left[i]
            i+=1
        else:
            T[k]= right[j]
            j+=1
        k+=1
    while i < l_n:
        T[k]=left[i]
        i+=1
        k+=1
    while j < r_n:
        T[k]=right[j]
        j+=1
        k+=1


def merge_sort(l,r,T):
    if(l < r):
        mid = (l+r)//2
        merge_sort(l,mid,T)
        merge_sort(mid + 1,r,T)
        merge(l,mid,r,T)


T = [13,2,45,5,32,4]
merge_sort(0,len(T)-1,T)
print(T)