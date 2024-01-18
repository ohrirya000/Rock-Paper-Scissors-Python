print("Type 1 for rock, 2 for paper, and 3 for scissors.")
pmove = int(input("Player 1 move: "))
moveOrMode = int(input("Player 2 move: "))
    
if(pmove == moveOrMode):
    print("Draw")
elif(pmove == 3 and moveOrMode == 1):
    print("Player 2 wins!")
elif(pmove == 1 and moveOrMode == 3):
    print("Player 1 wins!")
elif(pmove < moveOrMode):
    print("Player 2 wins!")
else:
    print("Player 1 wins!")
    
