# palindrome string check using two pointer

def is_palindrome(arr):
    arr= arr.lower().replace(" " , "")
    left , right =0, len(arr)-1
    while left< right:
        if arr[left]!=arr[right]:
            return False
        left +=1
        right -=1
    return True

print(is_palindrome("Hai bro"))
print(is_palindrome("waw"))