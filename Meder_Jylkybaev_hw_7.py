def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        middle = int((low+high)/2)
        guess = list[middle]
        if guess == item:
            return middle
        if guess > item:
            high = middle-1
        else:
            low = middle+1
print(binary_search([1, 3, 5, 7, 9], 9))

def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

nlist = [14,46,43,27,57,41,45,21,70]
bubbleSort(nlist)
print(nlist)