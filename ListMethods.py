#Prompt: Write a program to remove the duplicates in a list

def findUniques():
    list = [1,2,3,4,5,4,6,1,2,7]
    unique_list = []
    for num in list:
        if num not in unique_list:
            unique_list.append(num)
    print(*list)
    print(*unique_list)

if __name__ == '__main__':
    findUniques()