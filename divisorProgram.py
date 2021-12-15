b=[]

def divideBy2(a):
    # print("a = ",a)
     
    if a<=1:
        return
    
    if a%2!=0:
        b.append(a)
        if((a//2 )%2!=0):
            print(f"Plus ({a} / {2}) % {2} = {(a//2)%2}")    
            a=a-1
        else:
            print(f"Minus ({a} / {2}) % {2} = {(a//2)%2}")    
            a=a+1
        
    if a>0:  
        a = a//2 
        divideBy2(a)


# def divideBy2(a):
#     d = str(bin(a))[2:]
#     return (d.count('1'))+1
# divideBy2(1+1*10**309)
divideBy2(15)
print (b)
print (len(b))