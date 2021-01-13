from random import randint

random_num = randint(1, 9)
tries = 1

for _ in range(6):
    guess = int(input("Enter a number between (1-9) and try guessing :): "))
    if tries == 5:
        print(f"Oh, No you ran out of tries :(\nThe number was {random_num}")
        break
    if guess == random_num:
        print("CONGRATS YOU WON!!!!!")
        break
    if guess < random_num:
        print("The number is greater")
    if guess > random_num:
        print("The number is lesser")
    tries+=1
