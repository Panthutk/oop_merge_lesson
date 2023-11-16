import random


class Mastermind:
    def __init__(self):
        self._secret = int(random.randint(1, 50))
        self._guesses = 0
        self._status = False

    def play(self):
        while self._guesses <= 10:
            guess = int(input("Enter your guess: "))
            if guess == "quit":
                break
            self._guesses += 1
            if self._secret == guess:
                print("You guessed correctly!")
                self._status = True
                break
            else:
                print("You guessed incorrectly!")
                self._status = False
                self._clues(guess)
        print("The secret number was " + str(self._secret))
        print("You took " + str(self._guesses) + " guesses.")
        if self._status:
            print("You won!")
        else:
            print("You lost!")

    def _clues(self, guess):
        if guess < self._secret:
            print("Your guess is too low!")
        else:
            print("Your guess is too high!")


game = Mastermind()
game.play()
