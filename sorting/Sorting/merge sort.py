def merge(arr,l,m,r):
    right=arr[m+1:r+1]
    left=arr[l:m+1]

    i=j=0
    k=l

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
    print(*arr)

def merge_sort(arr,l,r):

    if l<r:
        mid=(l+r)//2
        merge_sort(arr,l,mid)
        merge_sort(arr,mid+1,r)

        merge(arr,l,mid,r)
n=int(input())
arr=list(map(int,input().split()))

merge_sort(arr,0,n-1)
