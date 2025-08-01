"""
Main menu.

Handles all logic for displaying and interacting with the main menu.
"""

import sys
import time
from colorama import Fore, Style

from game_text import GAME_TEXT
from utility import clear_screen

# --- Shared display engine ---
def display_title(title):
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
        formatted_text = text.format(bright=Style.BRIGHT, reset=Style.RESET_ALL + color)
        print(color + formatted_text)
        print()

def display_scene(location_key):
    """A reusable function to render a full scene."""
    clear_screen()
    scene_data = GAME_TEXT.get(location_key, GAME_TEXT["error"])
    display_title(scene_data["title"])
    display_description(scene_data["description"])

   # --- MENU LOGIC ---
def display_main_menu_options():
    """Displays the welcome screen and menu options."""
    display_scene("welcome_screen")
    print(Fore.CYAN + " " + "─" * 28)
    print(f"  {Fore.CYAN}│{Style.RESET_ALL} {Style.BRIGHT}1.{Style.RESET_ALL} {Fore.YELLOW}New Game{Fore.CYAN}                 │")
    print(f"  {Fore.CYAN}│{Style.RESET_ALL} {Style.BRIGHT}2.{Style.RESET_ALL} {Fore.WHITE}Load Game {Fore.RED}(Not Implemented){Fore.CYAN} │")
    print(f"  {Fore.CYAN}│{Style.RESET_ALL} {Style.BRIGHT}3.{Style.RESET_ALL} {Fore.WHITE}Options {Fore.RED}(Not Implemented){Fore.CYAN}   │")
    print(f"  {Fore.CYAN}│{Style.RESET_ALL} {Style.BRIGHT}4.{Style.RESET_ALL} {Fore.YELLOW}Quit{Fore.CYAN}                     │")
    print(Fore.CYAN + " " + "─" * 28)
    prompt = f"\n{Fore.CYAN}> {Style.RESET_ALL}"
    return input(prompt).strip()

def start_main_menu():
    """The controller for the main menu. Returns True if a new game should start."""
    while True:
        choice = display_main_menu_options()
        if choice == '1':
            return True # Signal to start the game
        elif choice == '2' or choice == '3':
            print(Fore.RED + "\nThis feature is not yet implemented.")
            time.sleep(2)
        elif choice == '4':
            return False # Signal to quit
        else:
            print(Fore.RED + f"\n'{choice}' is not a valid option. Please choose 1-4.")
            time.sleep(2)