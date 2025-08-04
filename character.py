from colorama import Fore, Style

class Character:
    """
    Represents a character in the game, holding all their stats,
    inventory, and equipment. Can be configured at creation time.
    """
    def __init__(self, name: str,
                 # --- Optional Keyword Arguments for customization ---
                 race: str = "Unknown",
                 class_name: str = "Uncalssed",
                 title: str = "The Novice",
                 level: int = 1,
                 experience: int = 0,
                 strength: int = 10,
                 dexterity: int = 10,
                 constitution: int = 10,
                 intelligence: int = 10,
                 wisdom: int = 10,
                 charisma: int = 10,
                 max_health: int = 100,
                 max_mana: int = 50):

        # --- Core Identity ---
        self.name: str = name
        self.title: str = title
        self.race: str = race
        self.class_name: str =  class_name

        # --- Leveling and Experience ---
        self.level: int = level
        self.experience: int = experience
        # You might calculate this based on level later
        self.experience_to_next_level: int = 100 

        # --- Primary Attributes ---
        self.strength: int = strength
        self.dexterity: int = dexterity
        self.constitution: int = constitution
        self.intelligence: int = intelligence
        self.wisdom: int = wisdom
        self.charisma: int = charisma

        # --- Derived Combat Stats ---
        self.max_health: int = max_health
        self.current_health: int = self.max_health # Always start at full health
        
        self.max_mana: int = max_mana
        self.current_mana: int = self.max_mana # Always start at full mana
        
        # --- Inventory and Equipment ---
        # These will always start empty for any new character instance.
        self.inventory: dict = {}
        self.equipment: dict = {
            "head": None, "chest": None, "shoulders" : None, "wrist" : None, "hands" : None, "belt" : None, "legs": None, "feet": None, "neck" : None, "ring_one" : None, "ring_two" : None, "accessory_one" : None, "accessory_two" : None, "main_hand": None, "off_hand": None,
        }

    def __repr__(self) -> str:
        """
        Provides a developer-friendly string representation of the character,
        useful for debugging.
        """
        return f"Character(name='{self.name}', level={self.level}, hp={self.current_health}/{self.max_health})"

    # --- Basic Methods (Examples for future use) ---

    def display_character_sheet(self):
        """Prints a well-formatted character sheet to the console."""
        
        # --- Helper for creating resource bars (HP/MP) ---
        def create_bar(current, maximum, color, bar_length=20):
            percent = float(current) / maximum
            filled_length = int(bar_length * percent)
            bar = '█' * filled_length + '-' * (bar_length - filled_length)
            return f"{color}[{bar}]{Style.RESET_ALL}"

        # --- Start Printing ---
        print(f"\n{Fore.YELLOW}--- CHARACTER SHEET ---{Style.RESET_ALL}")
        
        # Core Info
        print(f"  {Style.BRIGHT}{self.name}, the {self.title}{Style.RESET_ALL}")
        print(f"  Level {self.level} {self.race} {self.class_name}")
        
        # Resources
        hp_bar = create_bar(self.current_health, self.max_health, Fore.GREEN)
        mp_bar = create_bar(self.current_mana, self.max_mana, Fore.BLUE)
        print(f"\n  Health: {self.current_health:3}/{self.max_health:<3} {hp_bar}")
        print(f"  Mana:   {self.current_mana:3}/{self.max_mana:<3} {mp_bar}")
        
        # Experience
        print(f"  Exp:    {self.experience} / {self.experience_to_next_level}")
        
        # Attributes
        print(f"\n{Fore.CYAN}--- Attributes ---{Style.RESET_ALL}")
        print(f"  Strength:     {self.strength:<4}  Intelligence: {self.intelligence:<4}")
        print(f"  Dexterity:    {self.dexterity:<4}  Wisdom:       {self.wisdom:<4}")
        print(f"  Constitution: {self.constitution:<4}  Charisma:     {self.charisma:<4}")

        print(f"\n{Fore.YELLOW}-----------------------{Style.RESET_ALL}\n")

    def is_alive(self) -> bool:
        """Checks if the character's health is above 0."""
        return self.current_health > 0

    def take_damage(self, amount: int):
        """Reduces current health by a given amount."""
        self.current_health -= amount
        if self.current_health < 0:
            self.current_health = 0
        print(f"{self.name} takes {amount} damage!")

    def heal(self, amount: int):
        """Increases current health by a given amount, up to max_health."""
        self.current_health += amount
        if self.current_health > self.max_health:
            self.current_health = self.max_health
        print(f"{self.name} heals for {amount} health!")