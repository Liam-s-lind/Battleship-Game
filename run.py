import random

class BattleshipGame:
    def __init__(self, player_name):
        self.grid_size = 5  # Size of the grid
        self.player_grid = [['-' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.computer_grid = [['-' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.computer_display_grid = [['-' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.player_name = player_name
        self.shots_limit = 20  # Total shots limit for both player and computer

    def place_ships_randomly(self, grid):
        # Place 3 ships randomly on the given grid
        for _ in range(3):
            while True:
                x, y = random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)
                if grid[x][y] == '-':  # Check if cell is empty
                    grid[x][y] = 'S'  # Place ship
                    break

    def print_grid(self, grid):
        # Print the given grid
        for row in grid:
            print(' '.join(row))
        print()

    def make_guess(self, grid, display_grid, x, y):
        # Make a guess on the given grid and update the display grid
        if grid[x][y] in ['H', 'X']:
            # Cell has already been targeted
            print("Already targeted. Choose another coordinate.")
            return -1
        elif grid[x][y] == 'S':
            # Hit a ship
            grid[x][y] = 'H'
            display_grid[x][y] = 'H'
            print("Hit!")
            return 1
        else:
            # Missed
            grid[x][y] = 'X'
            display_grid[x][y] = 'X'
            print("Miss.")
            return 0

    def get_valid_coordinate(self, prompt):
        # Get valid coordinate input from the user
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
        # Computer's turn to make a guess
        while True:
            x, y = random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)
            result = self.make_guess(self.player_grid, self.player_grid, x, y)
            if result != -1:
                return result

    def player_turn(self):
        # Player's turn to make a guess
        while True:
            x = self.get_valid_coordinate("Enter X coordinate for your guess: ")
            y = self.get_valid_coordinate("Enter Y coordinate for your guess: ")
            result = self.make_guess(self.computer_grid, self.computer_display_grid, x, y)
            if result != -1:
                return result

    def start_game(self):
        # Start the game
        self.place_ships_randomly(self.computer_grid)
        self.place_ships_randomly(self.player_grid)

        player_score = 0  # Player's score
        computer_score = 0  # Computer's score
        total_shots = 0  # Total number of shots made

        # Main game loop
        while total_shots < self.shots_limit:
            print(f"\n{self.player_name}'s Grid:")
            self.print_grid(self.player_grid)
            print("Computer's Grid (Your Guesses):")
            self.print_grid(self.computer_display_grid)

            player_score += self.player_turn()
            total_shots += 1
            if total_shots >= self.shots_limit:
                break

            computer_score += self.computer_turn()
            total_shots += 1
            if total_shots >= self.shots_limit:
                break

        # End of the game - determining the winner
        print(f"\nFinal Score: {self.player_name} {player_score} - Computer {computer_score}")
        if player_score > computer_score:
            print(f"{self.player_name} wins!")
        elif player_score < computer_score:
            print("Computer wins.")
        else:
            print("It's a draw.")

# Start the game
player_name = input("Enter your name: ")
game = BattleshipGame(player_name)
game.start_game()
