def linear_search(data, search):
    for i in range(len(data)):
        if search == data[i]:
            return i
def binary_search(data,search):
    print(data)
    index = len(data)//2
    index3 = len(data)// 2
    index2 = len(data) -1
    
    if data[index] == search:
         return index
    if(data[index] < search):
        while True:
            if data[index] == search:
                return index
            if(data[index] < search):
                index = (index2+index)//2
            if(data[index] > search):
                index = (index+index3)//2
    if(data[index] > search):
        while True:
            if data[index] == search:
                return index
            if(data[index] < search):
                index = (index3+index)//2
            if(data[index] > search):
                index = (index)//2
                
                
def binary_search2(data ,search):
    low = 0
    high = len(data) -1
    
    while low <= high:
        index = (high-low)//2
        
        if data[index] == search:
            return index
        if data[index] < search:
            low = index
        if data[index] > search:
            high = index
            
            """ add exception for when number does not exist """
    

        
lista = [1,1,6,7,7,8,8,9,9,10]

print(linear_search(lista[:],5))
print(binary_search2(lista[:],5))
