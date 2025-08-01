"""
main.py

The main entry point for the game.
Its primary responsibilities are:
- Initializing the application (like colorama).
- Starting the main menu.
- Running the main game loop if the player chooses to start a new game.
"""
import sys
import time
from colorama import Fore, Style, init

# Import our game components
from game_state import GAME_STATE
from character import Character
from character_state import CHARACTER_STATE
from main_menu import start_main_menu, display_scene

# --- INITIALIZATION ---
# This should be the first thing that runs.
init(autoreset=True)

# --- GAME LOGIC ---
def run_game():
    """The main game loop and all logic that happens after the menu."""
    # --- CHARACTER CREATION & GAME START (Placeholder) ---
    print(Fore.GREEN + "Starting a new adventure...")
    time.sleep(2)

    # Placeholder character creation - this is our next big task!
    CHARACTER_STATE["player"] = Character(name="Hero")
    GAME_STATE["player_location"] = "golga_city"
    
    # --- THE MAIN GAME LOOP ---
    while True:
        display_scene(GAME_STATE["player_location"])
        
        print("-" * 50)
        action = input(f"{Fore.CYAN}> {Style.RESET_ALL}").lower().strip()
        
        if action in ["quit", "exit"]:
            break 
        else:
            print(Fore.YELLOW + "Command not yet implemented. Type 'quit' to exit.")
            time.sleep(1.5)

# --- MAIN PROGRAM EXECUTION ---
if __name__ == "__main__":
    
    should_start_game = start_main_menu()
    
    if should_start_game:
        run_game()

    print(Fore.RED + "\nThank you for playing!")
    sys.exit()