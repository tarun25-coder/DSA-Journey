# K rotation through slicing approach

def left_rotate(arr, k):
    if not arr:
        return []
    k=k%len(arr)
    return arr[k:] + arr[:k]

arr= [1,2,3,4,5]
k=2
print(left_rotate(arr, k))