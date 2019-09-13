import random
print ('Hello, this is a guessing game. The computer chose a number between 1-20, you need to guess what it is.')

def main():
    Computer = random.randint(1, 20)

    def raffle():
        return (random)
    raffle()

    def userguess(prompt):
        guess = input(prompt).strip().lower()
        while True:
            try:
                guess = int(guess)
                break
            except:
                print("Error! This is not a number. Try again.")
                continue
        return guess

    def checkguess():
        YouGuess = input ("What is your guess?")
        if int(Computer) == int(YouGuess):
            askagain = input('That\s right!! well done. Would you like to play again?')
            if 'y' in askagain:
                main()
            else:
                print ('OK, Goodbye')
                exit()
        elif int(Computer) > int(YouGuess):
            print ('Too low, try again ')
            checkguess()
        elif int(Computer) < int(YouGuess):
            print('Too high, try again ')
            checkguess()
        else:
            print ('This is not a number, try again ')
            checkguess()
    checkguess()
main()
