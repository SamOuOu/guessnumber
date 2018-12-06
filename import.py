import random

r = random.randint(1, 100)

while True:
    game = input('猜數字遊戲！請輸入數字：')
    game = int(game)
    if game == r:
        print('猜對囉66666')
        break
    elif game > r:
        print('太大囉，猜小一點，你剛猜的是', game)
    elif game < r:
        print('太小囉，猜大一點，你剛猜的是', game)
