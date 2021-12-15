#program to find object from array
def find_object(arr,obj):
    for i in arr:
        if i == obj:
            print("Object found at ",i)
            return True
    return False

data=[
    {'id':1,'name':'John',},
    {'id':2,'name':'Peter',},
    {'id':3,'name':'James',},
    {'id':4,'name':'ali',},
    {'id':5,'name':'parker',},
]
obj = {'name':'ali','id':4,}

if find_object(data,obj):
    print("Object found")
else:
    print("Object not found")
