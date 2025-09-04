import random

print("Wecome to Game: ")

num_1 = int(input("Enter the starting range: "))
num_2 = int(input("Enter the ending range: "))

num_3 = random.randint(num_1, num_2)

count = 0

while True:
    num_4 = int(input(f"Enter the number here in range {num_1} to {num_2}: "))
    count += 1   
    
    if num_4 == num_3:
        print("You got it in", count, "tries!")
        break
    elif num_4 > num_3:
        print("Too High! Try again")
    else:
        print("Too Low! Try again")
