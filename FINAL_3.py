def func(arr):
    two=[]
    for element in arr:
        if element not in two:
            two.append(element)
        else:
            return True
    return False
nums=list(map(int,input().split()))
print(func(nums))