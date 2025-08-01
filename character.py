class Character:
    """
    Represents a character in the game, holding all their stats,
    inventory, and equipment. Can be configured at creation time.
    """
    def __init__(self, name: str,
                 # --- Optional Keyword Arguments for customization ---
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
            "head": None, "chest": None, "legs": None, "feet": None,
            "main_hand": None, "off_hand": None,
        }

    def __repr__(self) -> str:
        """
        Provides a developer-friendly string representation of the character,
        useful for debugging.
        """
        return f"Character(name='{self.name}', level={self.level}, hp={self.current_health}/{self.max_health})"

    # --- Basic Methods (Examples for future use) ---

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