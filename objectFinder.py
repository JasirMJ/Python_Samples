

GRADE = [
    {
        "id":1,
        "name":"VIP 1",
        "business_count":1,
        "margin":5,
    },
    {
        "id":2,
        "name":"VIP 2",
        "business_count":10,
        "margin":10,
    },
    {
        "id":3,
        "name":"VIP 3",
        "business_count":25,
        "margin":15,
    },
    {
        "id":4,
        "name":"VIP 4",
        "business_count":50,
        "margin":20,
    },
]

business_count = 50

#find business_count object from GRADE
for grade in GRADE:
    if business_count <= grade["business_count"]:
        print(grade["name"])
        break


#get matching object from GRADE
for grade in GRADE:
    if business_count <= grade["business_count"]:
        print(grade)
        break

