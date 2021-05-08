import random

print('''歡迎來到猜數字遊戲

請從1~10中猜一個數字，猜到對。''')

answer = random.randint(1, 10)

while True:
    guess = input('請從1~10間猜一個數字: ')
    guess = int(guess)

    if guess > answer:
        print('試試小一點的數字...')
    elif guess < answer:
        print('試試大一點的數字...')
    else:
        print('恭喜，你猜對了!!!')
        break

