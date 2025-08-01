import os
import time
from colorama import Fore, Style, init

# Import the data structures from our other files
from game_text import GAME_TEXT
from game_state import GAME_STATE

# --- INITIAL SETUP ---
init(autoreset=True)

def clear_screen():
    """Clears the console screen for a clean display."""
    os.system('cls' if os.name == 'nt' else 'clear')

# --- DISPLAY LOGIC ---

def display_title(title):
    """Creates a stylish, colored title box for a location."""
    title_text = f" {title} "
    width = len(title_text) + 2
    
    print(Fore.CYAN + Style.BRIGHT + "╔" + "═" * width + "╗")
    print(Fore.CYAN + Style.BRIGHT + "║" + title_text.center(width) + "║")
    print(Fore.CYAN + Style.BRIGHT + "╚" + "═" * width + "╝")
    print()

def display_description(description_list):
    """Takes a list of dictionary items and prints them with specified colors."""
    for item in description_list:
        color = item['color']
        text = item['text']
        
        formatted_text = text.format(
            bright=Style.BRIGHT,
            reset=Style.RESET_ALL + color
        )
        
        print(color + formatted_text)
        print()

def display_scene(location_key):
    """A new, reusable function to render a full scene."""
    clear_screen()
    # Get the data for the scene from our GAME_TEXT dictionary
    scene_data = GAME_TEXT[location_key]
    
    # Display the title and description
    display_title(scene_data["title"])
    display_description(scene_data["description"])

# --- MAIN PROGRAM EXECUTION ---
if __name__ == "__main__":
    
    # --- 1. ONE-TIME STARTUP SEQUENCE ---
    # This part runs only once when the game starts.
    display_scene("welcome_screen")
    input(Fore.CYAN + "\nPress Enter to begin your adventure...")
    
    # Set the player's actual starting location after the welcome screen.
    GAME_STATE["player_location"] = "golga_city" #<==== this will change depending on player's location in player object
    
    # --- 2. THE MAIN GAME LOOP ---
    # This loop runs continuously, creating the dynamic part of the game.
    while True:
        # On each loop, display the scene based on the player's current location.
        display_scene(GAME_STATE["player_location"])
        
        # For now, we will just show a simple prompt and wait for a 'quit' command.
        # This is where all your game logic will eventually go.
        print("-" * 50)
        action = input(f"{Fore.CYAN}> {Style.RESET_ALL}").lower().strip()
        
        if action in ["quit", "exit"]:
            print(Fore.RED + "Thank you for playing!")
            break
        else:
            # We'll add real commands here later.
            print(Fore.YELLOW + "Command not yet implemented. Type 'quit' to exit.")
            time.sleep(1.5) # Pause briefly so the user can read the message