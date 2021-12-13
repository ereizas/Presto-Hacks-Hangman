import pygame
max_score = int(input("Enter the score needed to win:"))
p1score = 0
p2score = 0
p1 = True
hangman = ("","           \n          \n            \n    __     ","           \n   |      \n   |        \n   |__     ", "   ------, \n   |      \n   |        \n   |__     ","   ------, \n   |    o'\n   |        \n   |__     ","   ------, \n   |    o'\n   |    |   \n   |__     ","   ------, \n   |    o'\n   |  ~-|   \n   |__     ","   ------, \n   |    o'\n   |  ~-|-~ \n   |__     ","   ------, \n   |    o'\n   |  ~-|-~ \n   |__ /   ","   ------, \n   |    o'\n   |  ~-|-~ \n   |__ / \ ")
while p1score < max_score and p2score < max_score:
    print("Player 1 Score: " + str(p1score) + "     Player 2 Score: " + str(p2score) )
    answer = []
    guess = []
    hangindex = 0
    correct = False
    word = input("Player 1 enter a word or phrase:") if p1 else input("Player 2 enter a word or phrase:")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") ##prevents easy cheating
    for char in word:
        answer.append(char)
        if char != " ":
            guess.append("_")
        elif char == " ":
            guess.append(" ")
    print(hangman[0])
    print(guess)
    while not correct:
        letter_guess = ""
        while letter_guess == "" or len(letter_guess)>1:
            letter_guess = input("Player 2 guess a letter:") if p1 else input("Player 1 guess a letter:")
        if letter_guess in answer:
            index = 0
            for char in answer:
                if char==letter_guess:
                    guess[index]=letter_guess
                index+=1
            print(guess)
            if guess == answer:
                if p1:
                    p2score += 1
                    p1 = False
                else:
                    p1score += 1
                    p1 = True
                correct=True
        else:
            hangindex+=1
            print(hangman[hangindex])
        if hangindex == 9:
            if p1 == True:
                p1score+=1
                p1=False
            else:
                p2score+=1
                p1=True
            break
    print(guess)
print("Player 1 Score: " + str(p1score) + "     Player 2 Score: " + str(p2score) )
if p1score== max_score:
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
