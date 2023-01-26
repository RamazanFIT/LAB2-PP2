import random 
rand_num = random.randrange(1, 21)

name = str(input("Hello! What is your name?: "))
txt_1 = "Well, {}, I am thinking of a number between 1 and 20."
print(txt_1.format(name))
cnt = 0
while(True):
    cnt += 1
    print("Take a guess.")
    numb = int(input())
    if numb == rand_num:
        txt_2 = "Good job, {}! You guessed my number in {} guesses!"
        print(txt_2.format(name, cnt))
        exit()


