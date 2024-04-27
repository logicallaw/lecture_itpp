def getWinner(player1, player2):
    if (player1 == "가위"):
        if (player2 == "바위"):
            print("player2")
        elif (player2 == "보"):
            print("player1")
        else:
            print("draw")
    elif (player1 == "바위"):
        if (player2 == "가위"):
            print("player1")
        elif (player2 == "보"):
            print("player2")
        else:
            print("draw")
    else:
        if (player2 == "바위"):
            print("player1")
        elif (player2 == "가위"):
            print("player2")
        else:
            print("draw")



player1 = "가위"
player2 = "바위"
getWinner(player1, player2)
player1 = "보"
player2 = "바위"
getWinner(player1, player2)

