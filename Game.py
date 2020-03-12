
print("Let's Play Rock Paper Scissors game!")

player_1 = str( input("Player 1: please type 'rock', 'paper', or 'scissors'. "))
player_2 = str( input("Player 2: please type 'rock', 'paper', or 'scissors'. "))
    

if (player_1 == "rock" and player_2 == "scissors") or (player_1 == "scissors" and player_2 == "paper") or (player_1 == "paper" and player_2 == "rock"):
   print ("Player 1 wins!")
        
        
if (player_2 == "rock" and player_1 == "scissors") or (player_2 == "scissors" and player_1 == "paper") or (player_2 == "paper" and player_1 == "rock"):
    print ("Player 2 wins!")
       

if (player_1 == "rock" and player_2 == "rock") or (player_1 == "scissors" and player_2 == "scissors") or (player_1 == "paper" and player_2 == "paper"):
   print ("It's a tie!")
       