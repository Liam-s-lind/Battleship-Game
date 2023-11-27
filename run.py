import random

class BattleshipGame:
    def __init__(self, player_name):
        self.grid_size = 5
        self.player_grid = [['-' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.computer_grid = [['-' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.computer_display_grid = [['-' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.player_name = player_name
        self.shots_limit = 10
        self.ships_count = 3

    def place_ships_randomly(self, grid):
        for _ in range(self.ships_count):
            while True:
                x, y = random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)
                if grid[x][y] == '-':
                    grid[x][y] = 'S'
                    break

    def print_grid(self, grid):
        for row in grid:
            print(' '.join(row))
        print()

    def make_guess(self, grid, display_grid, x, y):
        if grid[x][y] == 'S':
            grid[x][y] = 'H'
            display_grid[x][y] = 'H'
            print("Hit!")
            return 1
        elif grid[x][y] == '-':
            grid[x][y] = 'X'
            display_grid[x][y] = 'X'
            print("Miss.")
            return 0
        else:
            print("Already targeted. Choose another coordinate.")
            return -1

    def get_valid_coordinate(self, prompt):
        while True:
            try:
                coord = int(input(prompt))
                if 0 <= coord < self.grid_size:
                    return coord
                else:
                    print(f"Enter a number between 0 and {self.grid_size - 1}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def computer_turn(self):
        while True:
            x, y = random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)
            result = self.make_guess(self.player_grid, self.player_grid, x, y)
            if result != -1:
                return result

    def player_turn(self):
        while True:
            x = self.get_valid_coordinate("Enter X coordinate for your guess: ")
            y = self.get_valid_coordinate("Enter Y coordinate for your guess: ")
            result = self.make_guess(self.computer_grid, self.computer_display_grid, x, y)
            if result != -1:
                return result

    def check_game_over(self, grid):
        return all(cell != 'S' for row in grid for cell in row)

    def start_game(self):
        self.place_ships_randomly(self.computer_grid)
        self.place_ships_randomly(self.player_grid)

        player_score = 0
        computer_score = 0

        while player_score < self.ships_count and computer_score < self.ships_count:
            print(f"\n{self.player_name}'s Grid:")
            self.print_grid(self.player_grid)
            print("Computer's Grid (Your Guesses):")
            self.print_grid(self.computer_display_grid)

            player_score += self.player_turn()
            if self.check_game_over(self.computer_grid):
                break

            computer_score += self.computer_turn()
            if self.check_game_over(self.player_grid):
                break

        print(f"\nFinal Score: {self.player_name} {player_score} - Computer {computer_score}")
        if player_score > computer_score:
            print("You Win!")
        elif player_score < computer_score:
            print("You lose.")
        else:
            print("It's a draw.")

# Start the game
player_name = input("Enter your name: ")
game = BattleshipGame(player_name)
game.start_game()
