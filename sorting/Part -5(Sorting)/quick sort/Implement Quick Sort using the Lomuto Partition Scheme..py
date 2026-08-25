def partition(arr,low,high):
    pivot=arr[low]
    j=high
    i=low+1

    while True
        while i<=high and arr[i]<=pivot:
            i+=1
        while pivot>arr[j]:
            j+=1
        if i>j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[low],arr[j]=arr[j],arr[low]
    return j
def quicksort(arr,low,high):
    if low<high:

        p=partition(arr,low,high,)
        quicksort(arr,low,p-1)
        quicksort(arr,p+1,high)
n= int(input())
arr=list(map(int,input().split()))
quicksort(arr,0,n-1)
print("Sorted arr:",*arr)