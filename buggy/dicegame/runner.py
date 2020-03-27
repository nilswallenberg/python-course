from .die import Die

class GameRunner:

    def __init__(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def dice(self):
        self.dice = Die.create_dice(5)

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        c = 0   # Consecutive wins
        runner = cls()
        while True:

            runner.dice = Die.create_dice(5)

            print("Round {}\n".format(runner.round))

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            while True:
                try:
                    guess = int(guess)
                    break
                except ValueError:
                    guess = input("Please input an integer")
                    continue


            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
                c += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
                c = 0
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            runner.round += 1

            if c == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")

                prompt = input("Would you like to play again?[y/n]: ")

                #if prompt == 'y':# or prompt == 'n':
                    #c = 0
                    #runner = cls()
                #elif prompt == 'n':
                    #break
                #else:
                while True:
                    if (prompt != "y") & (prompt != "n"):
                        prompt = input("Please press [y/n]:")
                    else:
                        break

                if prompt == "y":
                    c = 0
                    runner = cls()
                elif prompt == "n":
                    break

