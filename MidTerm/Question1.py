#Name - Win Yu Maung
#ID - 6612054
#Section - 542

def Ticket(row, fan, empty):
    index = 0
    emptychair = 0
    for j in range(len(empty)):
        if empty[j] > emptychair:
            emptychair = empty[j]
            index = j

    total = 0
    for i in range(fan):
        total += emptychair
        emptychair -= 1
        empty[index] -= 1
        for j in range(len(empty)):
            if empty[j] > emptychair:
                emptychair = empty[j]
                index = j
                
    return total

M = 3
N = 4
X = [1,2,4]
print("The maximum ticket price: ", Ticket(M, N, X), "dollars.")
