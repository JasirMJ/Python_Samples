#Program to find greatest duplicate in an array
def find_greatest_duplicate(arr):
    # Create a dictionary to store the count of each element
    count = {}
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    # Create a list to store the duplicate elements
    duplicate = []
    for i in count:
        if count[i] > 1:
            duplicate.append(i)
    # Return the greatest duplicate element
    print("Duplicates : ",duplicate)
    return max(duplicate)

data = [5,2,3,4,1,2,3]
print(find_greatest_duplicate(data))
