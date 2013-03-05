def findkeyCoordinate(mmap, i):
    for j in range(0,len(mmap)):
        for k in range(0,len(mmap[0])):
            if str(i) in str(mmap[j][k]):
                return (j, k)

def follow(mmap, x, y):
    if x != 0:
        if str(mmap[y][x-1]) == "+" or str(mmap[y][x-1]) == "-":
            return followkey(mmap, x-1,y,"links")
        if str(mmap[y][x-1]).isalnum():
            return str(mmap[y][x-1])
    if x!= len(mmap[y])-1:
        if str(mmap[y][x+1]) == "+" or str(mmap[y][x+1]) == "-":
            return followkey(mmap, x+1,y,"rechts")
        if str(mmap[y][x+1]).isalnum():
            return str(mmap[y][x+1])
    if y!=0:
        if str(mmap[y-1][x]) == "+" or str(mmap[y-1][x]) == "|":
            return followkey(mmap, x, y-1,"boven")
        if str(mmap[y-1][x]).isalpha():
            return str(mmap[y-1][x])
    if y!= len(mmap)-1:
        if str(mmap[y+1][x]) == "+" or str(mmap[y+1][x]) == "|":
            return followkey(mmap, x, y+1, "onder")
        if str(mmap[y+1][x]).isalpha():
            return str(mmap[y+1][x])
    
def horizontalcheck(mmap,x,y):
    if x != len(mmap[0])-1:
        if (str(mmap[y][x+1]) == "-" or str(mmap[y][x+1]) == "+"):
            return followkey(mmap,x+1,y,"rechts")
    if x != 0:
        if (str(mmap[y][x-1]) == "-" or str(mmap[y][x-1]) == "+"):
            return followkey(mmap,x-1,y,"links")
    if x != 0:
        if str(mmap[y][x-1]).isalpha():
            return str(mmap[y][x-1])
    if x != len(mmap[0])-1:
        if str(mmap[y][x+1]).isalpha():
            return str(mmap[y][x+1])

def verticalcheck(mmap, x, y):
    if y!= 0 and (str(mmap[y-1][x]) == "|" or str(mmap[y-1][x]) == "+"):
        return followkey(mmap,x,y-1,"boven")
    if y != len(mmap)-1 and (str(mmap[y+1][x]) == "|" or str(mmap[y+1][x]) == "+"):
        return followkey(mmap,x,y+1,"onder")
    if y!= 0 and str(mmap[y-1][x]).isalpha():
        return str(mmap[y-1][x])
    if y != len(mmap)-1 and str(mmap[y+1][x]).isalpha():
        return str(mmap[y+1][x])

def followkey(mmap, x, y, richting):
    if str(mmap[y][x]).isalpha():
        return str(mmap[y][x])
    
    if str(mmap[y][x]) == "-":
        if richting == "links":
            return followkey(mmap,x-1,y,richting)
        if richting == "rechts":
            return followkey(mmap,x+1,y,richting)
    if str(mmap[y][x]) == "|":
        if richting == "boven":
            return followkey(mmap,x,y-1,richting)
        if richting == "onder":
            return followkey(mmap,x,y+1,richting)
    if str(mmap[y][x]) == "+":
        if richting == "links" and x!=0 and x != len(mmap[0])-1:
            if str(mmap[y][x-1]) == "-" or str(mmap[y][x-1]) == "+" or str(mmap[y][x-1]).isalpha():
                return followkey(mmap,x-1,y,richting)
            else:
                return verticalcheck(mmap, x,y)
        if richting == "rechts" and x!=0 and x != len(mmap[0])-1:
            if str(mmap[y][x+1]) == "-" or str(mmap[y][x+1]) == "+" or str(mmap[y][x+1]).isalpha():
                return followkey(mmap,x+1,y,richting)
            else:
                return verticalcheck(mmap,x,y)
        if richting == "onder" and y!=0 and y != len(mmap)-1:
            if str(mmap[y+1][x]) == "|" or str(mmap[y+1][x]) == "+" or str(mmap[y+1][x]).isalpha():
                return followkey(mmap,x,y+1,richting)
            else:
                return horizontalcheck(mmap, x, y)
        if richting == "boven" and y!=0 and y != len(mmap)-1:
            if str(mmap[y-1][x]) == "|" or str(mmap[y-1][x]) == "+" or str(mmap[y-1][x]).isalpha():
                return followkey(mmap,x,y-1,richting)
            else:
                return horizontalcheck(mmap, x, y)
        if richting == "onder" or richting == "boven":
            return horizontalcheck(mmap, x, y)
        if richting == "links" or richting == "rechts":
            return verticalcheck(mmap,x,y)

def solve(mmap, key):
    ret = []
    for i in key:
        x, y = findkeyCoordinate(mmap, i)
        x = int(x)
        y = int(y)
        ret.append(str(follow(mmap,y,x))) 
    
    print ''.join(ret)

aantal = int(raw_input())
array = []
keys = []

for i in range(0,aantal):
    mmap = []
    y, x, key= str(raw_input()).split(" ")
    x = int(x)
    y = int(y)
    keys.append(str(key))
    for j in range(0,y):
        mmap.append(str(raw_input()))

    array.append(mmap)

for map in array:
    for x in map:
        if len(map[0]) != len(x):
            print "error"

for i in range(0,len(array)):
    solve(array[i], keys[i])