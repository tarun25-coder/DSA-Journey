# second largest element in the array

# Python 3
def second_largest(arr):
    # Edge case
    if len(arr) < 2:
        return -1

    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first   # old first becomes second
            first = num
        elif num > second and num != first:
            second = num

    return second if second != float('-inf') else -1


print(second_largest([10, 5, 20, 8]))    # 10
print(second_largest([5, 5, 5]))         # -1  (no second distinct)
print(second_largest([1, 2]))            # 1