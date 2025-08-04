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
# from character import Character
from character_state import CHARACTER_STATE
from main_menu import start_main_menu, display_scene
from character_creation import create_new_character
from utility import clear_screen

# --- INITIALIZATION ---
# This should be the first thing that runs.
init(autoreset=True)

# --- GAME LOGIC ---
def run_game():
    """The main game loop and all logic that happens after the menu."""
    CHARACTER_STATE['player'] = create_new_character()
    GAME_STATE['player_location'] = "golga_city"
    
    # --- THE MAIN GAME LOOP ---
    while True:
        if CHARACTER_STATE['player'] is None:
            print(Fore.RED + "Error: No player character found. Exiting.")
            break

        display_scene(GAME_STATE['player_location'])
                
        print("-" * 50)
        action = input(f"{Fore.CYAN}> {Style.RESET_ALL}").lower().strip()
        
        if action in ["quit", "exit"]:
            break

        elif action in ['stats', 'char', 'character']:
            clear_screen()
            player = CHARACTER_STATE['player']
            player.display_character_sheet()
            input(f"{Fore.CYAN}Press enter to continue...{Style.RESET_ALL}")
        
        else:
            print(Fore.YELLOW + "Command not yet implemented. Type 'quit' to exit.")
            time.sleep(2)


# --- MAIN PROGRAM EXECUTION ---
if __name__ == "__main__":
    
    should_start_game = start_main_menu()
    
    if should_start_game:
        run_game()

    print(Fore.RED + "\nThank you for playing!")
    sys.exit()