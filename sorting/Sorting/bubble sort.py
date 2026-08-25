a=int(input())
arr=list(map(int,input().split()))

for i in range(a):
    for j in range(0,a-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
    print(*arr)

