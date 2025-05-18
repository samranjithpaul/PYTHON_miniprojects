import random

def rock_paper_scissor():

    print("\nWelcome to Rock Paper Scissor Game")
    print("\nChoose: Rock, Paper or Scissor")

    # take input from user
    user = input("\n\n what is your choice?? 'r' is for rock,'s' is for scissor,'p'is for paper:\n\n ").lower()
    computer = random.choice(['r','p','s'])

    if user == computer:
        return '\nwe both choose same,lol'
    
    if is_win(user,computer):
        return '\nYou won!'
    print("\nthe computer chose:",computer.upper())
    
    if is_win(computer,user):
        return '\nYou lost!'
    print("\nthe computer chose: ",computer.upper())

    
def is_win(player,computer):
    # return true if player wins
    # r > s, s > p, p > r

    if (player == 'r' and computer == 's') or (player == 's'and computer == 'p') or (player == 'p' and computer == 'r'):
        return True
    
print(rock_paper_scissor())   