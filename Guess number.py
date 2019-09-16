import random
print ('Hello, this is a guessing game. The computer chose a number between 1-20, you need to guess what it is.')

def main():
    computer = random.randint(1, 20)

    def raffle():
        return (random)
    raffle()

    def user_guess(prompt):
        guess = input(prompt).strip().lower()
        while not guess.isdigit():
            print("Error! This is not a number. Try again. ")
            guess = input(prompt).strip().lower()
        return guess

    def check_guess():
        you_guess = input ("What is your guess? ")
        if int(you_guess) == int(computer):
            print ('That\s right!! well done')
        elif int(you_guess) > int(computer):
            print ('Too high, try again ')
            check_guess()
        elif int(you_guess) < int(computer):
            print('Too low, try again ')
            check_guess()
        else:
            print ('This is not a number, try again ')
            check_guess()
    check_guess()

    def play_again():
        while True:
            cont = input ('Would you like to play again? (Yes or No) ').strip().lower()
            if cont == 'yes'.strip().lower():
                main()
            elif cont == 'no'.strip().lower():
                print('OK, Goodbye')
                exit()
            else:
                print ('You types something else...')
                play_again()
    play_again()

main()
