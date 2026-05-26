import random

def number_guessing_game():
    while True:
        number = random.randint(1, 1000)
        guess = None
        correct = False
        tries = 0
        while correct == False:
            guess = int(input("Guess a number between 1 and 1000: "))
            tries += 1
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            elif guess == number:
                print("Correct!")
                correct = True
        print(f"Congrats! It took you {tries} tries to guess the number.")
        play_again = input("Do you want to play again (yes/no)? ")
        if play_again.lower() != "yes":
            break

def rock_paper_scissors():
    games_played = 0
    wins = 0
    losses = 0
    ties = 0
    while True:
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        player_choice = input("Choose rock, paper, or scissors: ").lower()
        print(f"The computer chose {computer_choice}.")
        if player_choice == computer_choice:
            print("It's a tie!")
            ties += 1
        elif player_choice == "rock" and computer_choice == "scissors":
            print("You win!")
            wins += 1
        elif player_choice == "paper" and computer_choice == "rock":
            print("You win!")
            wins += 1
        elif player_choice == "scissors" and computer_choice == "paper":
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1
        games_played += 1
        play_again = input("Do you want to play again (yes/no)? ")
        if play_again.lower() != "yes":
            print(f"Out of {games_played} game(s), you won {wins} time(s), lost {losses} time(s), and tied {ties} time(s).")
            break

def trivia():
    while True:
        questions = {
            "How many players are on the pitch during a scooer match?": "22",
            "What is the largest organ in the human body?": "Skin",
            "What galaxy do we live in?": "Milky Way",
            "How many wives did Henry VIII have?": "6",
            "Where did the Olympics originate?": "Greece",
            "How many bones are in the human body?": "206",
            "How many time zones are there in the world?": "24",
            "What is the closest planet to the sun?": "Mercury",
            "What is Baby Yoda's real name?": "Grogu",
            "What is the real name of Batman's first sidekick?": "Dick Grayson"
        }
        correct = 0
        incorrect = 0
        total = len(questions)
        for question, answer in questions.items():
            print(question)
            user_answer = input("Your answer: ").lower()
            if user_answer == answer.lower():
                print("Correct!")
                correct += 1
            else:
                print(f"Incorrect, the correct answer is {answer}")
                incorrect += 1
        print(f"Out of {total} questions, you got {correct} correct and {incorrect} incorrect.")
        play_again = input("Do you want to play again (yes/no)? ")
        if play_again.lower() != "yes":
            break

def main():
    games = ["number guessing game", "rock paper scissors", "trivia"]
    while True:
        game = input(f"What game would you like to play? Your options are {games}. ")
        game = game.lower()
        if game == "number guessing game":
            number_guessing_game()
        elif game == "rock paper scissors":
            rock_paper_scissors()
        elif game == "trivia":
            trivia()
        else:
            print("Invalid game.")
        play_again = input("Do you want to play another game (yes/no)? ")
        if play_again.lower() != "yes":
            break

main()