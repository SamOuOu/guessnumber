import random
start = input('隨機數字範圍開始值')
end = input('隨機數字範圍結束值')
start = int(start)
end = int(end)

r = random.randint(start, end)
time = 0
while True:
    game = input('猜數字遊戲！請輸入數字：')
    game = int(game)
    time = time + 1
    if game == r:
        print('猜對囉66666')
        print('你剛猜的', game, '是第', time, '次',)
        break
    elif game > r:
        print('太大囉，猜小一點')
    elif game < r:
        print('太小囉，猜大一點')
    print('你剛猜的', game, '是第', time, '次',)

