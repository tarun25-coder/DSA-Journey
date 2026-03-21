# duplicates in an array

def duplicate(arr):
    seen = set()
    duplicate=set()
    for num in arr:
        if num in seen:
            duplicate.add(num)
        seen.add(num)
    return list(duplicate)


print(duplicate([1,1,1,2,1,2,2,4,5,6]))
        