merge_count=0

def merge(arr,l,m,r):
    global merge_count
    i=j=0
    k=l
    left=arr[l:m+1]
    right=arr[m+1:r+1]

    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1
    merge_count += 1
    print("Merge :",merge_count)


    print("Left Array :",left)
    print("Right Array :",right)
    print("Merged Array :",left+right)

def merge_sort(arr,l,r):
    if l<r:
        m=(l+r)//2
        merge_sort(arr,l,m)
        merge_sort(arr,m+1,r)
        merge(arr,l,m,r)

a=int(input())
arr=list(map(int,input().split()))
merge_sort(arr,0,a-1)
