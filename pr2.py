
def largest(arr,n):
    max = arr[0]
  
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    print ("Largest in given array is",max)

arr = [10, 324, 45, 90, 9808,22222,3,44]
c=0
for i in arr:
    c=c+1
largest(arr,c)
