import csv

def task_2_1(filename):
    with open(filename, "r") as f:
        s = f.read()
        s = s.split(", ")
        #s = list(csv.reader(f))
        #print(s)
    ascii = list(map(lambda x: chr(int(x)), s))
    return ascii


def task_2_3(char_lst):
    n = len(char_lst)**0.5
    array = [[None for _ in range(n)] for _ in range(n)]

    i = 0
    while i!=n:
        for r in range(i, n-i):
            array[r][i] = char_lst[0]
            char_lst.pop(0)
        for c in range(i, n-i):
            array[n-i][c] = char_lst[0]
            char_lst.pop(0)
        
        array = array[::-1]
        array = list(map(lambda x: x[::-1], array))
        for r in range(1, n-i):
                    array[r][i] = char_lst[0]
                    char_lst.pop(0)
        for c in range(n-i):
            array[n-i][c] = char_lst[0]
            char_lst.pop(0)
        i+=1
            
        
    
print(list("#abcdefghijklmn@"))
#print(task_2_3("#abcdefghijklmn@"))