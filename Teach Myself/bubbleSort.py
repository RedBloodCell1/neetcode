arr = [5,3,4,6,8,9,6,5,3,2,2,3,4,6,9,0,7,5,32,45,5,6,8,1,2,3,1,3,3,3,2,2,12,23,32]

# for i in range(len(arr)):
#     for j in range(1,len(arr)-i):
#         if arr[j-1] > arr[j]:
#             temp = arr[j-1]
#             arr[j-1] = arr[j]
#             arr[j] = temp
            
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[j] < arr[i]:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp

print(arr)