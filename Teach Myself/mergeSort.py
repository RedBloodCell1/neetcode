arr = [8,7,6,5,4,3,2,1]

def mergeSort(arr):
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    
    return merge(left, right)
    
def merge(arr1, arr2):
    
    temp = []
    l,r = 0,0
    
    while l < len(arr1) and r < len(arr2):
        if arr1[l] <= arr2[r]:
            temp.append(arr1[l])
            l+=1
        else:
            temp.append(arr2[r])
            r+=1
    
    if l < len(arr1): temp.extend(arr1[l:])
    if r < len(arr2): temp.extend(arr2[r:])
    
    return temp

print(mergeSort(arr))