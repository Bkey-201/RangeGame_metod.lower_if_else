# Mетод . lower () гарантирует, что такие варианты ввода, как "Basketball" или "BasketBall ",будут интерпретироваться
# одинаково.
sport = input ( "Enter а sport: ")# Запрашивает название игры
p1_score=int(input("Enter player 1 score: ")) # Запрашивает ввод счета первого игрока
p2_score = int(input("Enter player 2 score: "))# Запрашивает ввод счета второго игрока
# 1
if sport.lower() == "basketball":# приравниваем Верхний регистр к нижнему с помощью метода lower
# 2
    if p1_score == p2_score:
        print("The game is а draw.")
    elif p1_score > p2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.") # 
elif sport.lower() == "golf":
# 3
    if p1_score == p2_score:
        print("The game is а draw.")
    elif p1_score > p2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
else:
    print("Unknown sport")
