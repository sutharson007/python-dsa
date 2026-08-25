a=int(input())
arr=list(map(int,input().split()))

for i in range(a):
    swapped=False
    for j in range(a-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swapped=True
    if not swapped:
        break
print("Ascending order:",arr)

# 6
# 5 1 4 2 8 3
# Ascending order: [1, 2, 3, 4, 5, 8]