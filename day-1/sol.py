'''
Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so open

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances.
'''

def sol():
    f = open('input.txt','r')
    x,y,diff = [],[],[]
    for n in f:
        cood = n.split()
        if cood != []:
            x.append(int(cood[0]))
            y.append(int(cood[1]))

    while x!=[]:
        minx,miny = min(x),min(y) 
        diff.append(abs(minx-miny))
        x.remove(minx)
        y.remove(miny)
    print('Sum: ',sum(diff))
    return None

def sol2():
    f = open('input.txt','r')
    x,y,sim = [],[],[]
    for n in f:
        cood = n.split()
        if cood != []:
            x.append(int(cood[0]))
            y.append(int(cood[1]))

    for i in x:
        count = 0
        for j in y:
            if j == i: count +=1
        sim.append(i*count)

    print('Similarity: ',sum(sim))
    return None

if __name__ == '__main__':
    sol() # Sum: 1873376
    sol2() # Similarity: 18997088
