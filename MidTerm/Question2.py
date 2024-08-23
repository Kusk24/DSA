#Name - Win Yu Maung
#ID - 6612054
#Section - 542

def maxfinder(mylist):
    mydict = {}
    for i in mylist:
        if i in mydict:
            mydict[i] += 1
        else:
            mydict[i] = 0

    i = 0
    for key,value in mydict.items():
        if value > i:
            i = value
    return i


mylist = [3,4.5,9,2,3,4.5,2.5,-100,7,4.5]
print(f"for {mylist} , output = {maxfinder(mylist)}")

mylist2 = [1.5,1,9,1.5,1,9,2]
print(f"for {mylist2} , output = {maxfinder(mylist2)}")

mylist3 = [99.4,7.5,1.24,3]
print(f"for {mylist3} , output = {maxfinder(mylist3)}")

