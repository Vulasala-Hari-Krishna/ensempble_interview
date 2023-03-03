#bubble sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j+1]<arr[j]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
    return arr

print(bubble_sort([4,2,5,1,-1,3,56,2]))