


choices = list(range(9))

def board():
    board = f"""
    ----------
    |{choices[0]}|{choices[1]}|{choices[2]}|
    |{choices[3]}|{choices[4]}|{choices[5]}|
    |{choices[6]}|{choices[7]}|{choices[8]}|
    ----------
    """
    print(board)
is_winner = False
def make_move(player, choices):
    slot_choice = int(input(f"place your '{player}': "))  
    choices[slot_choice] = player
     
    
def check_winner(choices):
    is_winner = False
    winner_sequences = [(0,1,2),(0,3,6),(6,4,2),(0,4,8),(1,4,7),(2,5,8),(3,4,5),(6,7,8)]
    for slot1, slot2, slot3 in winner_sequences:
        if choices[slot1] == choices[slot2] == choices[slot3]:
            print(f"{choices[slot1]} won ")
            is_winner = True
            
            break   
    return is_winner

while True:
    new_game = input("Do want to play a game or quit?(y/n)")

    if new_game == "y":
        pass

    elif new_game == "n":
        break

    else:
        continue


    choices = list(range(9))

    for turn in range(4):
        
        board()
        make_move('X', choices)
        if check_winner(choices): 
            break 
        board()
        make_move('Y', choices)
        
        if check_winner(choices): 
            break 

    print("Starting new while loop")


        



