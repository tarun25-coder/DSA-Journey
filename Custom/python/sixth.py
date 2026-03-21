# slicing for reverse

def reverse(str):
    words= str.split()
    return " ".join(words[::-1])
       

print(reverse("hai bro"))