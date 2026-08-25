a=int(input())
arr=list(map(int,input().split()))

for i in range(a):
    swapped=False
    for j in range(a-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swapped=True


    if not swapped and i==0:
        print(f"After Pass {i+1}", arr)
        print("Array is already Sorted")
        break
    elif not swapped:
        print(f"After Pass {i+1}", arr)


# 5
# 1 2 3 4 5
# After Pass 0 [1, 2, 3, 4, 5]
# Array is already Sorted
