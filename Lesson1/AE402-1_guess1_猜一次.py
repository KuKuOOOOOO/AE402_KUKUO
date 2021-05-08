import random

print('''歡迎來到猜數字遊戲

請從1~20中猜一個數字，只能猜一次''')

answer = random.randint(1, 20)


guess = input('請從1~20間猜一個數字: ')
guess = int(guess)

if guess > answer:
    print('猜錯，太大囉！')
elif guess < answer:
    print('猜錯，太小囉！')
else:
    print('恭喜，猜對了!!!')

1