"""
character_creation.py
Handles the step-by-step process of creating a new player character.
"""
import time

from colorama import Fore, Style

from utility import clear_screen
from main_menu import display_title
from character import Character

# --- DATA FOR RACES AND CLASSES (Easily Scalable) ---
# ... (no changes to RACE_DATA or CLASS_DATA) ...
RACE_DATA = {
    "human" : {
        "name" : "Human",
        "description" : "Adaptable and ambitious, humans are a balanced choice for any path, and natural leaders and learners.",
        "stat_mods" : {"strength" : 1, "dexterity" : 1, "constitution" : 1, "intelligence" : 1, "wisdom" : 1, "charisma" : 1}
    },
    "elf": {
        "name": "Elf",
        "description" : "Graceful and wise, with a natural affinity for magic and archery.",
        "stat_mods" : {"dexterity" : 2, "intelligence" : 1}
    },
    "dwarf" : {
        "name" : "Dwarf",
        "description" : "Sturdy and resolute, known for their resilience and smithing skills.",
        "stat_mods" : {"strength": 1, "constitution": 2}
    }
}

CLASS_DATA = {
    "warrior" : {
        "name" : "Warrior",
        "description" : "Masters of martial combat, relying on strength and steel to overcome their foes.",
        "stat_mods" : {"strength": 2, "constitution" : 2}
    },
    "mage": {
        "name": "Mage",
        "description": "Scholars of the arcane who wield powerful magics to control the battlefield.",
        "stat_mods": {"intelligence": 2, "wisdom": 1}
    },
    "rogue": {
        "name": "Rogue",
        "description": "Cunning and agile, they strike from the shadows and excel at skills requiring a delicate touch.",
        "stat_mods": {"dexterity": 2, "charisma": 1}
    }
}


# --- HELPER FUNCTIONS ---
# ... (no changes to _present_choice) ...
def _present_choice(header_title: str, prompt_text: str, options_data: dict) -> str:
    """
    A reusable function to display options and get a valid choice from the user.
    Returns the key of the chosen option (e.g., 'human', 'warrior'.)
    """
    clear_screen()
    display_title(header_title)

    # Create a list of the keys to make indexing easy
    option_keys = list(options_data.keys())

    # Display the options
    for i, key in enumerate(option_keys, 1):
        option = options_data[key]
        print(f"  {Style.BRIGHT}{i}. {option['name']}{Style.RESET_ALL}")
        print(f"     {Fore.YELLOW}{option['description']}{Style.RESET_ALL}\n")

    # Get User Input
    while True:
        choice = input(f"{Fore.CYAN}{prompt_text} > {Style.RESET_ALL}").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(option_keys):
            return option_keys[int(choice) - 1]
        else:
            print(Fore.RED + f"Invalid choice. Please enter a number between 1 and {len(option_keys)}")


# --- MAIN CHARACTER CREATION FUNCTION ---

def create_new_character() -> Character:
    """
    The main function that guides the player through character creation.
    Returns a fully initialized Character object.
    """
    # --- NAME ---
    clear_screen()
    display_title("NAME YOUR CHARACTER")
    while True:
        name = input(f"{Fore.CYAN}What is your name? > {Style.RESET_ALL}").strip()
        if name:
            break
        print(Fore.RED + "A name cannot be empty.")

    # --- RACE & CLASS ---
    chosen_race_key = _present_choice("CHOOSE YOUR RACE", "Enter the number for your race:", RACE_DATA)
    # --- RESTORED: Class selection is now active ---
    chosen_class_key = _present_choice("CHOOSE YOUR CLASS", "Enter the number for your class:", CLASS_DATA)

    # --- CALCULATE FINAL STATS ---
    base_stats = {
        "strength": 10, "dexterity": 10, "constitution": 10,
        "intelligence": 10, "wisdom": 10, "charisma": 10
    }

    # Get the dictionaries of stat modifiers
    race_mods = RACE_DATA[chosen_race_key].get("stat_mods", {})
    # --- RESTORED: Get class modifiers ---
    class_mods = CLASS_DATA[chosen_class_key].get("stat_mods", {})

    # Combine the stats
    final_stats = base_stats.copy()
    for stat, value in race_mods.items():
        final_stats[stat] += value
    # --- RESTORED: Apply class stat modifiers ---
    for stat, value in class_mods.items():
        final_stats[stat] += value

    # --- INSTANTIATE CHARACTER ---
    player = Character(
        name=name,
        # --- RESTORED: Pass the chosen race and class names ---
        race=RACE_DATA[chosen_race_key]["name"],
        class_name=CLASS_DATA[chosen_class_key]["name"],
        strength=final_stats["strength"],
        dexterity=final_stats["dexterity"],
        constitution=final_stats["constitution"],
        intelligence=final_stats["intelligence"],
        wisdom=final_stats["wisdom"],
        charisma=final_stats["charisma"]
    )

    # --- CONFIRMATION SCREEN ---
    clear_screen()
    display_title("YOUR ADVENTURER IS READY")
    print(f"  Name:       {Style.BRIGHT}{player.name}{Style.RESET_ALL}")
    print(f"  Race:       {Style.BRIGHT}{player.race}{Style.RESET_ALL}")
    # --- RESTORED: Display the chosen class ---
    print(f"  Class:      {Style.BRIGHT}{player.class_name}{Style.RESET_ALL}\n")
    print(f"  {Fore.GREEN}--- Attributes ---{Style.RESET_ALL}")
    print(f"  Strength:     {player.strength}")
    print(f"  Dexterity:    {player.dexterity}")
    print(f"  Constitution: {player.constitution}")
    print(f"  Intelligence: {player.intelligence}")
    print(f"  Wisdom:       {player.wisdom}")
    print(f"  Charisma:     {player.charisma}\n")
    print(f"{Fore.CYAN}Your journey is about to begin...{Style.RESET_ALL}")
    time.sleep(5) # Give the player time to read their new stats

    return player