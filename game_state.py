GAME_STATE = {

    # Player's current position. This is the most important key for driving the display.
    # The value should always match a key in the GAME_TEXT dictionary.
    "player_location": "welcome_screen",

    # --- World Information ---
    # Tracks global information about the game world.
    "world": {
        "day": 1,
        "time_of_day": "morning",  # Could be 'morning', 'afternoon', 'evening', 'night'
    },

    # --- Quest and Story Tracking ---
    # A dictionary to track the status of every quest.
    # The key is a unique quest ID, and the value is its current stage.
    "quests": {
        "main_quest_01": "not_started",
        "find_lost_cat": "not_started",
    },

    # --- Flags ---
    # Simple True/False switches for tracking specific events or discoveries.
    # This is extremely powerful for checking if the player has done something.
    "flags": {
        "met_the_innkeeper": False,
        "unlocked_fast_travel": False,
        "bridge_to_ashwood_repaired": False,
    },
    
    # --- Available Locations ---
    # A list of location keys that the player is allowed to travel to.
    # This will grow as the player discovers new places.
    "unlocked_locations": [
        "golga_city" 
    ]
}