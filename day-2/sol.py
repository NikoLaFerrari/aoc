def sol():
    f = open('input.txt','r')
    safe = 0
    for x in f:
        cood = [int(i) for i in x.split()]
        if cood == []: break
        if all(i<j and 0<=abs(i-j)<=3 for i,j in zip(cood,cood[1:])):
            safe+=1
        elif all(i>j and 0<=abs(i-j)<=3 for i,j in zip(cood,cood[1:])):
            safe+=1
        else: continue

    print('Safe: ',safe)
    return None

def sol2():
    f = open('input.txt','r')

    def helper(cood):
        return (all(i<j and 0<=abs(i-j)<=3 for i,j in zip(cood,cood[1:])) or
            all(i>j and 0<=abs(i-j)<=3 for i,j in zip(cood,cood[1:])))
    
    safe = 0
    for x in f:
        cood = [int(i) for i in x.split()]
        if cood == []: break
        if helper(cood): safe+=1 
        else:
            for i in range(len(cood)):
                if helper(cood[:i]+cood[i+1:]):
                    safe+=1
                    break
                
    print('Safe: ',safe)
    return None

if __name__ == "__main__":
    sol() # 510
    sol2() # 553
