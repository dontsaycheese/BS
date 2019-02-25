import random

def BS(x,y):
    centre = abs(int((x+y+1)/2))
    print(centre)
    if(obsarray[centre]==tosearch):
        return centre
    elif(obsarray[centre]>tosearch):
        return BS(0,centre-1)
    elif(obsarray[centre]<tosearch):
        return BS(centre+1,len(obsarray)-1)

obsarray = list(random.randint(0, 1000) for r in range(20))

obsarray.sort()

print(obsarray)

#tosearch = random.choice(obsarray)
tosearch = int(input())

print(tosearch)
index = BS(0,len(obsarray))
print("Number found at: ", index+1)

