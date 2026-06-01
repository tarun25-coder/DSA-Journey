# Two sum with hash and with time complexity of O(n) and space complexity of O(n)

def two_sum(nums, target):
    seen={}
    for i, num in enumerate(nums):
        complement=target- num
        if complement in seen:
            return [seen[complement], i]
        seen[num]=i
    return None