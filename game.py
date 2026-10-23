
import random
from logic import feedback


class Mastermind:
    DIFFICULTIES = {
        "1": {"name": "Easy", "length": 3, "symbols": 4, "turns": 12},
        "2": {"name": "Medium", "length": 4, "symbols": 6, "turns": 10},
        "3": {"name": "Hard", "length": 5, "symbols": 8, "turns": 8},
    }

    def __init__(self):
        self.history = []
        self.game_over = False
        self.won = False
        self.choose_difficulty()

    def choose_difficulty(self):
        print("\nChoose difficulty:")
        print("1. Easy (3 digits, symbols 1-4, 12 turns)")
        print("2. Medium (4 digits, symbols 1-6, 10 turns)")
        print("3. Hard (5 digits, symbols 1-8, 8 turns)")

        while True:
            choice = input("Enter 1, 2, or 3: ").strip()
            if choice in self.DIFFICULTIES:
                settings = self.DIFFICULTIES[choice]
                self.difficulty = settings["name"]
                self.length = settings["length"]
                self.max_symbol = settings["symbols"]
                self.turns = settings["turns"]
                self.code = [
                    str(random.randint(1, self.max_symbol))
                    for _ in range(self.length)
                ]
                return

            print("Invalid choice. Please enter 1, 2, or 3.")

   
    def run(self):
        if self.game_over:
            print("This game has already ended.")
            return

        print(f"\nMastermind - {self.difficulty}")
        print(
            f"Guess the {self.length}-digit code using symbols "
            f"1 to {self.max_symbol}."
        )

        while self.turns > 0 and not self.game_over:
            raw = input(f"{self.turns} turns left > ").strip()

            if raw.lower() == "q":
                self.game_over = True
                print("Game quit.")
                return

            valid_symbols = "12345678"[:self.max_symbol]

            if (
                len(raw) != self.length
                or any(ch not in valid_symbols for ch in raw)
            ):
                print(
                    f"Invalid guess. Enter exactly {self.length} digits "
                    f"from 1 to {self.max_symbol}."
                )
                print(f"Turns remaining: {self.turns}")
                continue

            exact, partial = feedback(self.code, list(raw))
            self.history.append((raw, exact, partial))
            self.turns -= 1

            print(f"Exact: {exact}, Partial: {partial}")

            print("\nGuess History:")
            for number, (guess, ex, part) in enumerate(
                self.history, start=1
            ):
                print(
                    f"{number}. Guess: {guess} | "
                    f"Exact: {ex} | Partial: {part}"
                )
            print()

            if exact == self.length:
                self.won = True
                self.game_over = True
                print("Cracked the code! You win!")
                return

        if not self.won:
            self.game_over = True
            print("Out of turns! The code was", "".join(self.code))
            print("Game over.")
