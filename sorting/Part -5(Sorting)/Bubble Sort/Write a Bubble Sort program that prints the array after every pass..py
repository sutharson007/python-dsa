a=int(input())
arr=list(map(int,input().split()))

for i in range(a):
    for j in range(a-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

    print(f"After Pass {i}",arr)

    # 5
    # 5
    # 1
    # 4
    # 2
    # 8
    # After
    # Pass
    # 0[1, 4, 2, 5, 8]
    # After
    # Pass
    # 1[1, 2, 4, 5, 8]
    # After
    # Pass
    # 2[1, 2, 4, 5, 8]
    # After
    # Pass
    # 3[1, 2, 4, 5, 8]
    # After
    # Pass
    # 4[1, 2, 4, 5, 8]
