from colorama import Fore, Style

# --- DATA ---
# All our game text is stored here. This separates the "what" (content) from the "how" (code).
GAME_TEXT = {
    "golga_city": {
        "title": "Golga City",
        "description": [
            {
                "color": Fore.WHITE,
                "text": "The sprawling port city of Golga unfolds before you, a chaotic tapestry "
                        "of sights and smells. The sharp, briny scent of the sea a constant companion, "
                        "carried on a wind that whips flags and coats everything in a thin layer of salt."
            },
            {
                "color": Fore.BLUE,
                "text": "To the east, the {bright}Cobblestone Docks{reset} are a hive of activity. Hulking merchant "
                        "ships are tethered to thick, mossy pylons, their crews shouting in a dozen "
                        "different languages as they haul crates and barrels onto the creaking wooden planks."
            },
            {
                "color": Fore.MAGENTA,
                "text": "Looming over the entire city, seeming to pierce the clouds themselves, is the "
                        "{bright}Spire of the Magi{reset}. Its smooth, pearlescent surface reflects the sky, and "
                        "you can almost feel a low, humming vibration emanating from it—a testament to the "
                        "powerful and mysterious arcane energies harnessed within."
            },
            {
                "color": Fore.WHITE,
                "text": "In the city's heart, the {bright}Grand Market{reset} buzzes with a thousand voices. "
                        "Brightly colored awnings shield stalls overflowing with exotic fruits, shimmering "
                        "silks, and the wares of skilled artisans. The air here is thick with the scent of "
                        "spices, sizzling food, and sweet perfumes."
            },
            {
                "color": Fore.YELLOW,
                "text": "Tucked away on a side street, almost lost amidst the grandeur and chaos, "
                        "is a small, welcoming building. A simple wooden sign, swaying gently in the breeze, "
                        "reads: {bright}The Weary Traveler Inn{reset}. A warm, golden light spills from its windows, "
                        "promising respite from the bustling streets."
            }
        ]
    },
    "error": {
        "title": "VOID",
        "description": [
            {
                "color": Fore.RED,
                "text": "You find yourself in a formless, featureless void. A chilling "
                        "realization dawns upon you: this place should not exist."
            },
            {
                "color": Fore.MAGENTA,
                "text": "Developer Note: A non-existent location key was requested. "
                        "Check the value of GAME_STATE['player_location'] or the "
                        "argument passed to display_scene()."
            }
        ]
    },
    "welcome_screen": {
        "title": "Unnamed RPG",
        "description": [
            {
                "color": Fore.CYAN,
                "text": "Welcome, traveler, to a world brimming with choice and consequence. "
                        "The story that unfolds is not pre-written; it will be forged by your "
                        "ambitions, your blade, your wits, and your heart."
            },
            {
                "color": Fore.WHITE,
                "text": "Will you rise to power and {bright}build a kingdom{reset}, your decrees shaping the lives of "
                        "thousands? Or will the call of the unknown lead you into forgotten ruins as a famed "
                        "{bright}dungeon delver{reset}, your name whispered in taverns with tales of glory?"
            },
            {
                "color": Fore.WHITE,
                "text": "You could become a celebrated {bright}hero{reset}, a shield for the weak who saves realms from "
                        "darkness... or perhaps you will {bright}become the darkness{reset} itself, a fearsome power that "
                        "heroes are forged to stand against. The path of a cunning {bright}merchant{reset} is also yours "
                        "to walk, building an empire from a single coin."
            },
            {
                "color": Fore.CYAN,
                "text": "These paths, and many more, lie before you. Your legend is yet to be written. "
                        "What will it be?"
            }
        ]
    },
    # When you add the Inn, you'll add a new key here, like "weary_traveler_inn": { ... }
}