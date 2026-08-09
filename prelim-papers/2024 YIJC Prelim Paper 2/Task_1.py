import csv

#Task 1.1
def hash(address):
    temp = 9619
    for char in address:
        temp *= 37
        temp += ord(char)

    return temp%250

print(hash(str([263,'Braddell Heights',22-363,'S251398'])))

#Task 1.2 
with open("ADDRESSES.TXT", "r") as f:
    uninserted = []
    s = csv.reader(f)
    hash_table = [None]*250
    for row in s:
        index = hash(str(row))
        if hash_table[index] == None:
            hash_table[index] = row
        else:
            uninserted.append(row)

#print(hash_table[:10])
#print(len(uninserted))
    
#Task 1.3
with open("ADDRESSES.TXT", "r") as f:
    uninserted = []
    s = csv.reader(f)
    hash_table = [None]*250
    for row in s:
        index = hash(str(row))
        while hash_table[index] != None:
            index+=1
            index%=250
        hash_table[index] = row

#print(hash_table[-10::])

#Task 1.4
def hash_search(tbl, addr):
    index = hash(str(addr))
    while tbl[index] != addr:
        #print(index)
        index+=1
        index%=250
        if index==hash(str(addr)):
            return False
    return True

tbl = hash_table
print(hash_search(tbl, ['933', 'Yishun Ring Road', 'S524389']))
print(hash_search(tbl, ['263','Braddell Heights','22-363','S251398']))
        
        
    
    

