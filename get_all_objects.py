#program to return all objects from array matching by name
def find_object(arr,name):
    object_list = []
    for i in arr:
        if i['name'] == name:
            print("Object found at ",i)
            object_list.append(i)
    return object_list

data=[
    {'id':1,'name':'John',},
    {'id':2,'name':'Peter',},
    {'id':3,'name':'James',},
    {'id':4,'name':'ali',},
    {'id':5,'name':'parker',},
    {'id':6,'name':'ali',},
]
name = "ali"
objs = find_object(data,name)
print("objects : ",objs)
