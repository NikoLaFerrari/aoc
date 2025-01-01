def helper(char):
    open,close,comma = 0,0,0
    for i in char:
        if i == '(' and open==0: open=char.index(i)
        if i == ')' and close==0: close=char.index(i)
        if i == ',' and comma==0: comma=char.index(i)
    try:
        n1 = int(char[open+1:comma]) 
        n2 = int(char[comma+1:close])
        return (True,n1*n2)
    except ValueError:
        return (False,0)


def sol():        
    f = open('input.txt','r')
    line = f.read()
    mul = []   
    for i in range(len(line)):
        if line[i:i+3] == 'mul': 
            res = helper(line[i:i+12])
            if res[0]: mul+=[res[1]]
    print('Part 1:',sum(mul))
    return None

def sol2():
    f = open('input.txt','r')
    line = f.read()
    mul,do = 0,True
    for i in range(len(line)): 
        if line[i:i+4]=='do()': 
            do = True
            i+=3
        elif line[i:i+7]=="don't()": 
            do = False
            i+=6
        elif line[i:i+4]=='mul(' and do:
            res = helper(line[i:i+12])
            if res[0]: mul+=res[1]
            i+=3
        else: continue 
    print('Part 2:',mul)    
    return None

if __name__ == "__main__": 
    sol() # 170068701
    sol2() # 78683433
