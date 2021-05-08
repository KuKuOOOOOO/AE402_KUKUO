1import random

print('''歡迎來到猜數字遊戲

請從1~20中猜一個數字，只能猜五次''')

answer = random.randint(1, 20)

counter = 0

while counter<5:
    counter = counter + 1
    
    guess = input('請從1~20間猜一個數字: ')
    guess = int(guess)

    if guess > answer:
        if counter == 5:
            print("可惜！你已經猜五次了！")
        else:
            print('試試小一點的數字...')
    elif guess < answer:
        if counter == 5:
            print("可惜！你已經猜五次了！")
        else:
            print('試試大一點的數字...')
    else:
        print('恭喜，你猜對了!!!')
        break
