#Prompt: Write a program to find the largest number in a list
import random
#Creating a list w/ random entries from 1-1000 to avoid hard coding
def createList():
    numList = []
    for i in range(10):
        numList.append(random.randrange(1,1000))
    print("List: ", *numList)
    return numList

def findGreatest():
    numList = createList()
    greatest = numList[0]
    for num in numList:
        if num > greatest:
            greatest = num
    return greatest

if __name__ == '__main__':
    print("Greatest Number: ", findGreatest())