a=int(input())
arr=list(map(int,input().split()))

for i in range(1,a):
    key=arr[i]
    j=i-1

    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
    print("Pass",i)
    print("key",key)
    print("shifts",i-j-1)
    print(f"After Pass {i}",arr)


# 5
# 12 11 13 5 6
# Pass 1
# key 11
# shifts 1
# After Pass 1 [11, 12, 13, 5, 6]
# Pass 2
# key 13
# shifts 0
# After Pass 2 [11, 12, 13, 5, 6]
# Pass 3
# key 5
# shifts 3
# After Pass 3 [5, 11, 12, 13, 6]
# Pass 4
# key 6
# shifts 3
# After Pass 4 [5, 6, 11, 12, 13]