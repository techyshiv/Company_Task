import random
def Print_Random_Number(arr):
    random.shuffle(arr)
    for i in arr:
        print(i,end=" ")
num = int(input("Enter How many number you want in array:"))
Print_Random_Number([int(i) for i in range(num)])