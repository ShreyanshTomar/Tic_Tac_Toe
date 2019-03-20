class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   
board = [1,2,3,4,5,6,7,8,9]
count = 0
def Board():
    print ("+-----------+")
    print ("| {} | {} | {} |".format(board[0],board[1],board[2]))
    print ("+-----------+")
    print ("| {} | {} | {} |".format(board[3],board[4],board[5]))
    print ("+-----------+")
    print ("| {} | {} | {} |".format(board[6],board[7],board[8]))
    print ("+-----------+")
   
def userdata():
    Position = int(input("Enter the position you want to mark your symbol on:"))
    Marker = input("Enter your Symbol: 'X' or 'O':")
    if(Marker == 'X' or Marker == 'O'):
        board[Position-1] = Marker
        Board()
    else:
        print ("Please Re-enter the valid inputs")
        userdata()
    
    
def start_tic_tac_toe():
    global count
    global board
    print ("Welcome to Tic_Tac_Toe!")
    Board()
    for turn in range(1,10):
        if turn%2 == 1:
            print ("Player 1 it's your turn")
            print ("Your symbol is 'X'")
            userdata()
            if(board[0]==board[1]==board[2] or board[0]==board[3]==board[6] or board[2]==board[5]==board[8] or board[6]==board[7]==board[8] or board[3]==board[4]==board[5] or board[0]==board[4]==board[8] or board[2]==board[4]==board[6]):
                print ("Player 1 wins")
                
                print ("Player 2 loses")
                break
            else:
                count += 1
                pass
        elif turn%2 == 0:
            print ("Player 2 it's your turn")
            print ("Your symbol is 'O'")
            userdata()
            if(board[0]==board[1]==board[2] or board[0]==board[3]==board[6] or board[2]==board[5]==board[8] or board[6]==board[7]==board[8] or board[3]==board[4]==board[5] or board[0]==board[4]==board[8] or board[2]==board[4]==board[6]):
                print ("Player 2 wins")
                print ("＼（＾○＾）人（＾○＾）／")
                print ('Player 1 loses ⊙﹏⊙')
                break
            else:
                count += 1
                pass
    
    
    if(count == 9):
        board = [1,2,3,4,5,6,7,8,9]
        count = 0
        print ("Ohh!")
        print ("It's a tie!  o(〃＾▽＾〃)o")
        print ("Want to play again?\nY for Yes or N for No ")
        tie = input()
        if tie == 'Y':
            start_tic_tac_toe()
        else:
            print ("Thanks for Playing! :)")
            pass
    else:
        board = [1,2,3,4,5,6,7,8,9]
        count = 0
