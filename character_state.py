"""
This file holds the state for all "living" characters in the game world,
most importantly, the player's character object.
"""

# We initialize the player as None. This is a common and powerful pattern.
# It means "we have a space reserved for the player, but no character has
# been created or loaded yet."
CHARACTER_STATE = {

    "player": None,

    # A list to hold the character objects of any companions in the player's party.
    "party_members": [],
    
    # A reference to the character object the player is currently targeting in combat.
    "active_target": None

}