#program to order objects in a list

data = [
    {'value':10,'amount':90,'position':1},
    {'value':50,'amount':100,'position':2},
    {'value':500,'amount':200,'position':3},
    {'value':10,'amount':300,'position':4},
    {'value':30,'amount':400,'position':5},
]

def customSort(k):
    return k['value']


data.sort(key=customSort)
print(data)