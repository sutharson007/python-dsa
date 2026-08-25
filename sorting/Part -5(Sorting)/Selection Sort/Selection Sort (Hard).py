a=int(input())
arr=list(map(int,input().split()))

for i in range(a):

    min_idx=i
    for j in range(i+1,a):
        if arr[min_idx]>arr[j]:
            min_idx=j
    minimum=arr[min_idx]
    arr[min_idx],arr[i]=arr[i],arr[min_idx]
    print("Pass",i)
    print("Minimum element",minimum)
    print("Index",min_idx)
    print(f"Arr =",*arr)

    # 5
    # 64
    # 25
    # 12
    # 22
    # 11
    # Pass
    # 0
    # Minimum
    # element
    # 64
    # Index
    # 4
    # Arr = 11
    # 25
    # 12
    # 22
    # 64
    # Pass
    # 1
    # Minimum
    # element
    # 25
    # Index
    # 2
    # Arr = 11
    # 12
    # 25
    # 22
    # 64
    # Pass
    # 2
    # Minimum
    # element
    # 25
    # Index
    # 3
    # Arr = 11
    # 12
    # 22
    # 25
    # 64
    # Pass
    # 3
    # Minimum
    # element
    # 25
    # Index
    # 3
    # Arr = 11
    # 12
    # 22
    # 25
    # 64
    # Pass
    # 4
    # Minimum
    # element
    # 64
    # Index
    # 4
    # Arr = 11
    # 12
    # 22
    # 25
    # 64