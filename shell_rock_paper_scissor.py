
import random

 
def run_game (atmpt):
    print('you have only ',atmpt,' Attempt')
    
    A,B,C = 'Stone','Paper','Scissor'
    shell_List = [A,B,C]
    randInt = random.randint(0,len(shell_List)-1)

    computer = shell_List[randInt]
    output = input(f'Enter 0 for {A}, 1 for {B}, 2 for {C}:')
    
    if not output or not output.isdigit():
        print('Invalid input, please enter a number.')
        return run_game(atmpt)
    output_num = int(output)
    if output_num >= 3:
        print('Enter a number within the valid range.')
        return run_game(atmpt)
    
    player = shell_List[output_num]
    
    if player == computer:
         print("Tie!")
         return { 'computer' : 0, 'player' : 0}
    elif player == A:
        if computer == B:
         print("You lose!", computer, "covers", player)
         return { 'computer' : 1, 'player' : 0}
        else:
            print("You win!", player, "smashes", computer)
            return { 'computer' : 0, 'player' : 1}
    elif player == B:
        if computer == C:
            print("You lose!", computer, "cut", player)
            return { 'computer' : 1, 'player' : 0}
        else:
            print("You win!", player, "covers", computer)
            return { 'computer' : 0, 'player' : 1}
    elif player == C:
        if computer == A:
            print("You lose...", computer, "smashes", player)
            return { 'computer' : 1, 'player' : 0}
        else:
            print("You win!", player, "cut", computer)
            return { 'computer' : 0, 'player' : 1}
    else:
        print('Invalid Input .')
        return run_game(atmpt)
    

def shell_Game ():
    print("Welcome to the ultimate game of Rock, Paper, Scissors!")
    atmpt = 5
    Computer = Player = 0
    while atmpt > 0:
      score = run_game(atmpt)
      if score.keys():
         Computer += score['computer']
         Player += score['player']
      atmpt = atmpt-1
    else:
        print('Game over')
        if Player == Computer:print(f"Score: {Player=} , {Computer=} \n It's a deadlock! Both players are evenly matched")
        elif Player > Computer : print(f"Incredible win! Player scores {Player=} defeating computer with {Computer=}.")
        else : print(f"Defeat! The computer wins with a score of {Computer=} against your {Player=}.")
        regame = input('Did you need to play once more ?(y/n)')
        if regame.lower() != 'n':
            return shell_Game()
        
    
shell_Game()
    
    