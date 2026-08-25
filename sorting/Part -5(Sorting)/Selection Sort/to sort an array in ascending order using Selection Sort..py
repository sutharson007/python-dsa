a=int(input())
arr=list(map(int,input().split()))

for i in range(a):

    min_idx=i
    for j in range(i+1,a):
        if arr[min_idx]>arr[j]:
            min_idx=j
    arr[min_idx],arr[i]=arr[i],arr[min_idx]
print(*arr)