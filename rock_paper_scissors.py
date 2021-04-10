from random import randint

# seçeneklerin listesi
elements = ["Rock", "Paper", "Scissors"]

# bilgisayarın hangi aralıklarda seçeceğini tanımlamak
computer = elements[randint(0, 2)]

# biz başlayana kadar oyunun başlamaması için player = false olarak atıyoruz
player = False

while player != True:
    player = input("Please select one: Rock, Paper, Scissors\n")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")

# oyuncuyu loop durması için tekrar false olarak atıyoruz
    player = False
    computer = elements[randint(0, 2)]
