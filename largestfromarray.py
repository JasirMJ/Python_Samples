#Program to find n th largest element in an array
def find_nth_largest(arr,n):
    return sorted(arr)[-n]

arr = [1,2,3,4,5,6,7,8,9,10]
n = 3
print(find_nth_largest(arr,n))
