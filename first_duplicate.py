lst = [5,2,3,4,1,2,3]
print("List ",lst)
duplicates = {}
for item in lst:
    count = 0
    for i in lst:
        if item == i:
            count += 1
    duplicates[item] = count
print("Duplicate ", duplicates)
first_dup = ""
for firstDup in duplicates:
    # print(duplicates[firstDup])
    if duplicates[firstDup] > 1:
        first_dup = firstDup
        # print(firstDup)
        break

print("first_dup ",first_dup)